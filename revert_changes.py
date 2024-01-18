#revert_changes.py
""" It is available in the GUI also in the menu bar!"""

from pathlib import Path
from json import load
from os import renames
from shutil import move

def revert_structure(current_dir: str):
    try:
        print("Current directory:", current_dir)

        # Load the structure information
        revert_info_file = Path(current_dir) / "revert_info.json"
        if not revert_info_file.exists():
            raise ValueError("File(revert_info.json) does not exist!")
        print("Got file:", revert_info_file)

        with open(revert_info_file, "r") as json_file:
            revert_info = load(json_file)

        source_dir = Path(revert_info["source_dir"])
        structure_info = revert_info["structure_info"]

        # Get all file paths from the current directory
        files_in_current_dir = {file_path.name: file_path for file_path in Path(current_dir).rglob('*') if file_path.is_file()}

        if not files_in_current_dir:
            raise ValueError("No files in the current directory")

        for filename, relative_path in structure_info.items():
            source_path = files_in_current_dir.get(filename)

            if source_path:
                target_path = source_dir / Path(relative_path)

                target_path.parent.mkdir(parents=True, exist_ok=True)

                # Move files back to their original locations
                try:
                    renames(source_path, target_path)
                except OSError:
                    move(source_path, target_path)
            else:
                print(f"File '{filename}' not found in the current directory.")

        print("Changes reverted successfully.")
        return True

    except Exception as e:
        print(f"Error reverting changes: {str(e)}")
        raise

if __name__ == "__main__":
    # Ask user for the path of the current directory where the revert_info.json file is located
    current_dir = input("Enter the path of the current directory(revert_info.json must exist): ")
    revert_structure(current_dir=current_dir)
