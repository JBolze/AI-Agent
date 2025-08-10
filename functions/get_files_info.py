import os


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        absolute_base = os.path.abspath(working_directory)
        abs_path = os.path.abspath(full_path)

        if not (abs_path == absolute_base or abs_path.startswith(absolute_base + os.sep)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_path):
            return f'Error: "{directory}" is not a directory'
        
        try:
            list_items = os.listdir(abs_path)
        except Exception as e:
            return f'Error: Could not list directory contents: {e}'
        
        if not list_items:
            return f'Error: Directory "{directory}" is empty.'

        result_lines = [f'Contents of "{directory}":']
        for item in list_items:
            item_path = os.path.join(abs_path, item)
            try:
                is_dir = os.path.isdir(item_path)
                size = os.path.getsize(item_path)
            except Exception as e:
                return f'Error: Could not access item "{item}": {e}'
            result_lines.append(
                f'- {item}: full_path="{item_path}", file_size={size} bytes, is_dir={is_dir}'
            )
        return "\n".join(result_lines)
    except Exception as e:
        return f'Error: An unexpected error occurred: {str(e)}'