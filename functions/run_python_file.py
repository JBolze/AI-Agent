import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_base = os.path.abspath(working_directory)
        abs_path = os.path.abspath(full_path)

        if not (abs_path == absolute_base or abs_path.startswith(absolute_base + os.sep)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_path):
            return f'Error: File "{file_path}" not found.'

        if not abs_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        try:
            result = subprocess.run(
                ["python", abs_path] + args,
                capture_output=True,
                text=True,
                cwd=absolute_base,
                timeout=30
            )
        except subprocess.TimeoutExpired:
            return f'Error: Execution timed out after 30 seconds.'
        except Exception as e:
            return f'Error: executing Python file: {e}'

        output_lines = []
        if result.stdout:
            output_lines.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
            output_lines.append(f'STDERR:\n{result.stderr}')
        if result.returncode != 0:
            output_lines.append(f'Process exited with code {result.returncode}')
        if not output_lines:
            return "No output produced."
        return "\n".join(output_lines)
    except Exception as e:
        return f'Error: executing Python file: {e}'