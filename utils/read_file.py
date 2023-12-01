from typing import List


def read_file(file_name: str) -> List[str]:
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return []
