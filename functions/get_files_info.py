import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, directory))
    files = []
    if not os.path.abspath(abs_file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_file_path):
        return f'Error: "{directory}" is not a directory'
    for file in os.listdir(abs_file_path):
        full_path = os.path.join(abs_file_path, file)
        size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)
        file_string = f" - {file}: file_size={size}, is_dir={is_dir}"
        files.append(file_string)
    return "\n".join(files)
