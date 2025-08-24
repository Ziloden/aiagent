from functions.get_files_info import get_files_info

tests = [
    ("Result for current directory:", "calculator", "."),
    ("Result for 'pkg' directory:", "calculator", "pkg"),
    ("Result for '/bin' directory:", "calculator", "/bin"),
    ("Result for '../' directory:", "calculator", "../"),
    ]
for test in tests:
    print(f"{test[0]}\n{get_files_info(*test[1:])}")