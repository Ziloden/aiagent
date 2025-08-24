from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

# file_info_tests = [
#     ("Result for current directory:", "calculator", "."),
#     ("Result for 'pkg' directory:", "calculator", "pkg"),
#     ("Result for '/bin' directory:", "calculator", "/bin"),
#     ("Result for '../' directory:", "calculator", "../"),
#     ]
#for test in file_info_tests:
#   print(f"{test[0]}\n{get_files_info(*test[1:])}")

# file_content_tests = [
#     ("calculator", "main.py"),
#     ("calculator", "pkg/calculator.py"),
#     ("calculator", "/bin/cat"),
#     ("calculator", "pkg/does_not_exist.py"),
# ]
# for test in file_content_tests:
#     print(get_file_content(*test))

file_write_tests = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]

for test in file_write_tests:
    print(write_file(*test))