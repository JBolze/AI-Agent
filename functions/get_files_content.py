import os
from functions.config import MAX_FILE_CHARACTERS

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_base = os.path.abspath(working_directory)
        abs_path = os.path.abspath(full_path)

        if not (abs_path == absolute_base or abs_path.startswith(absolute_base + os.sep)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return f'Error: Could not read file "{file_path}": {e}'

        if len(content) > MAX_FILE_CHARACTERS:
            content = content[:MAX_FILE_CHARACTERS] + f'\n[...File "{file_path}" truncated at {MAX_FILE_CHARACTERS} characters].'

        return content
    except Exception as e:
        return f'Error: {e}'

from functions.get_files_content import get_file_content

if __name__ == "__main__":
    print("Running get_file_content test...")
    result = get_file_content("calculator", "lorem.txt")
    print(f"Result:\n{result}")