from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

file_info_tests = [
    ("Result for current directory:", "calculator", "."),
    ("Result for 'pkg' directory:", "calculator", "pkg"),
    ("Result for '/bin' directory:", "calculator", "/bin"),
    ("Result for '../' directory:", "calculator", "../"),
    ]
#for test in file_info_tests:
#   print(f"{test[0]}\n{get_files_info(*test[1:])}")

file_content_tests = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]
for test in file_content_tests:
    print(get_file_content(*test))