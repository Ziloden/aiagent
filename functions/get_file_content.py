import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    combined_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(combined_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(combined_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(combined_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) < os.path.getsize(combined_path):
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    
    return file_content_string
    