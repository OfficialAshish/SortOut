#revert_changes.py
""" It is available in the GUI also in the menu bar!"""

from pathlib import Path
from json import load
from os import renames
from shutil import move

def revert_structure(current_dir: str):
    """ Reverse the structure of a directory back to its original state
    Args: Directory path! which has to be reverted back to its previous state. ( revert_info.json file must exits there!)

    Returns: True , If successfully reverted back. Raise Exception otherwise.
    """
    try:
        print("Current directory:", current_dir)

        # Load the structure information
        revert_info_file = Path(current_dir) / "revert_info.json"
        # revert_info_file = Path(current_dir) / "revert_info.json.gz"
        if not revert_info_file.exists():
            raise ValueError("File(revert_info.json) does not exist!")
        print("Got file:", revert_info_file)

        with open(revert_info_file, "r") as json_file:
            revert_info = load(json_file)
        
        # for compressed revert_info.json.gz file
        # with open(revert_info_file, "rt", encoding="utf-8") as gzipped_json_file:
        #     revert_info = load(gzipped_json_file)
        # print(revert_info)

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
