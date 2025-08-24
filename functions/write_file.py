import os

def write_file(working_directory, file_path, content):
    combined_path = os.path.join(working_directory, file_path)
    path_up_to_file = os.path.split(combined_path)[0]
    if not combined_path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(path_up_to_file):
        os.makedirs(path_up_to_file)
    with open(combined_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{combined_path}" ({len(content)} characters written)'