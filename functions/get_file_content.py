import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.abspath(abs_file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(abs_file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) < os.path.getsize(abs_file_path):
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    
    return file_content_string
    