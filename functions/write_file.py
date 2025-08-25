import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    path_up_to_file = os.path.split(abs_file_path)[0]
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(path_up_to_file):
        os.makedirs(path_up_to_file)
    with open(abs_file_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{abs_file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the specified content to the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to, relative to the working directory. This parameter must be provided.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The actual content to write to the file specified. This parameter must be provided.",
            ),
        },
    ),
)