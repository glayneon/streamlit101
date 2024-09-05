import os
import subprocess


def analyze_code(directory):
    # List Python files in the directory
    python_files = [
        file for file in os.listdir(directory) if file.endswith('.py')
        ]

    if not python_files:
        print("No Python files found in the specified directory.")
        return

    for file in python_files:
        print(f"Analyzing file: {file}")
        file_path = os.path.join(directory, file)

        # Run pylint
        print("\nRunning pylint...")
        pylint_command = f"pylint {file_path}"
        subprocess.run(pylint_command, shell=True)

        # Run flake8
        print("\nRunning flake8...")
        flake8_command = f"flake8 {file_path}"
        subprocess.run(flake8_command, shell=True)


if __name__ == '__main__':
    directory = r"."
    analyze_code(directory)
