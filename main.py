import os
import sys

from dotenv import load_dotenv
from functions.call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("You must provide a prompt.")
        exit(1)
    
    verbose = False
    if len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            verbose = True

    user_prompt = sys.argv[1]
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

Do not respond with your plan.
Do not respond with what you need.
You do not need to ask the user for any file paths.
Only respond with the final result.

Bugs should not be fixed by simply replacing all the code with just a print statement that satisfies the requirement.
All tests should pass.

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(0, 20):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[available_functions]
                )
            )

            for candidate in response.candidates:
                messages.append(candidate.content)

            if response.function_calls:
                for function_call in response.function_calls:
                    function_call_result = call_function(function_call, verbose=verbose)
                    if function_call_result.parts[0].function_response.response:
                        if verbose:
                            print(f"-> {function_call_result.parts[0].function_response.response}")
                    else:
                        raise Exception("No result response in function call result.")
                    messages.append(
                        types.Content(role="user", parts=[types.Part(text=function_call_result.parts[0].function_response.response['result'])])
                    )
            if response.text:
                print(response.text)
                if verbose:
                    print(f"User prompt: {user_prompt}")
                    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                break
        except Exception as e:
            print(f"ERROR: {e}")
            exit(1)


if __name__ == "__main__":
    main()
