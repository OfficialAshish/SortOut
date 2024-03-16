""" It is available in the GUI also in the menu bar!"""

"""You can also use this script to revert changes without including duplicate files; simply set is_allow_duplicates to False."""

from pathlib import Path
from json import load
from os import renames
from shutil import move

def revert_structure(current_dir: str, is_allow_duplicates = True):
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

        # Create a dictionary to store the mapping of filenames to target paths
        target_paths = {}
        for file_name, paths in structure_info.items():
            target_paths[file_name] = [source_dir / Path(relative_path) for relative_path in paths]

        # print("Target_paths : ",target_paths)

        files_in_current_dir = [file for file in Path(current_dir).rglob('*') if file.is_file()]
        if not files_in_current_dir:
            raise ValueError("No files in the current directory")
        # print("Files_in_current_dir : ",files_in_current_dir)

        # Iterate over the files in the current directory and move them back to their original locations
        for file_path in files_in_current_dir:
            if file_path.is_file():
                filename = file_path.name
                target_path_list = target_paths.get(filename)

                if target_path_list:
                    if not is_allow_duplicates :
                        target_path_list = target_path_list[0]
                    target_path = target_path_list.pop()

                    # Ensure the target path exists
                    if target_path:
                        target_path.parent.mkdir(parents=True, exist_ok=True)

                        # Move files back to their original locations
                        try:
                            renames(file_path, target_path)
                        except OSError:
                            move(file_path, target_path)
                        
                        # Update the target_paths dictionary with the modified list
                        target_paths[filename] = target_path_list
 
        print("Changes reverted successfully.")
        return True
 
    except Exception as e:
        print(f"Error reverting changes: {str(e)}")
        

if __name__ == "__main__":
    # Ask user for the path of the current directory where the revert_info.json file is located
    current_dir = input("Enter the path of the current directory(revert_info.json must exist): ")
    revert_structure(current_dir=current_dir)
