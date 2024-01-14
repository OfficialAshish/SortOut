#revert_changes.py
""" It is available in the GUI also in the menu bar!"""

from pathlib import Path
import json
import shutil

def revert_structure(current_dir: str):
    """ Reverse the structure of a directory back to its original state
    Args: Directory path! which has to be reverted back to its previous state. ( revert_info.json file must exits there!)

    Returns: True , If successfully reverted back. Raise Exception otherwise.
    """
    try:
        print("Current directory: ", current_dir)
        # Load the structure information
        revert_info_file = Path(current_dir) / "revert_info.json"
        if not revert_info_file.exists():
            raise ValueError("File(revert_info.json) does not exist.!")
        print("Got file : ", revert_info_file)
        with open(revert_info_file, "r") as json_file:
            revert_info = json.load(json_file)

        source_dir = Path(revert_info["source_dir"])
        structure_info = revert_info["structure_info"]

        # Get all file paths from the current directory
        files_in_current_dir = [
            file_path
            for file_path in Path(current_dir).rglob('*')
            if file_path.is_file()  # and any("SortedOut" in part for part in file_path.parts)
        ]
        # print('dir:', files_in_current_dir)
        if not files_in_current_dir or len(files_in_current_dir) < 2:
            raise ValueError("No files in the current directory")

        for filename, relative_path in structure_info.items():
            # Use rglob('*') to find the source path in the current directory
            source_path = next(
                (file_path for file_path in files_in_current_dir if filename == file_path.name),
                None
            )
            if source_path is not None:
                target_path = source_dir / Path(relative_path)

                # Ensure the target directory exists
                target_path.parent.mkdir(parents=True, exist_ok=True)

                # Move files back to their original locations
                shutil.move(source_path, target_path)
                print(".",sep="")
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
