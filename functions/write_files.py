import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_base = os.path.abspath(working_directory)
        abs_path = os.path.abspath(full_path)

        if not (abs_path == absolute_base or abs_path.startswith(absolute_base + os.sep)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure parent directories exist
        parent_dir = os.path.dirname(abs_path)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir)
            except Exception as e:
                return f'Error: Could not create parent directories for "{file_path}": {e}'

        try:
            with open(abs_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            return f'Error: Could not write to file "{file_path}": {e}'

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'