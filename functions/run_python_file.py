import os
import subprocess

from functions.config import PROCESS_TIMEOUT
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    command = ["python3", abs_file_path] + args
    try:
        process = subprocess.run(command, timeout=PROCESS_TIMEOUT, capture_output=True, text=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    result_string = f"STDOUT: {process.stdout if process.stdout else 'No output produced.'}"
    result_string += f"\nSTDERR: {process.stderr if process.stderr else 'No output produced.'}"
    if process.returncode != 0:
        result_string += f"\nProcess exited with code {process.returncode}"
    return result_string

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the specified python file and included arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file to execute, relative to the working directory. This parameter must be provided.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The list of arguments to be passed to the python file when executed. If this is not provided the file will be executed with no arguments.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="The individual arguments to be passed to the python file when executed."
                )
            ),
        },
    ),
)