 
## Introduction

Welcome to the File Organizer, a simple tool to help you organize your files effortlessly. This program provides a user-friendly interface to organize your files based on various algorithms and criteria.
 
## Using the File Organizer

### Main Window

The main window of the File Organizer provides an intuitive interface to organize your files. Here are the key components:

- **Source Directory**: Enter the path to the directory containing the files you want to organize.

- **Target Directory (optional)**: Optionally, specify a target directory where the organized files will be moved or copied.

- **Algorithm**: Choose one of the available algorithms:
  - **Organize by Extensions**: Organize files based on their extensions.
  - **Group Similar**: Group similar files together.
  - **Organize by Regex**: Organize files using a regular expression pattern.
  -
  - **(Note)** (Group Similar is Not suitable for a large number of files; choose "Organize by Extensions" if dealing with a large number of files)

- **Options**:
  - **Folders named after common file extensions**: Create folders named after common file extensions (applies to Organize by Extensions). 
  - For example, if you have numerous files with extensions like .doc, .txt, .pdf, .csv, etc., create a dedicated folder for Documents to streamline and categorize them efficiently.

  - **Include SubFolders / Files**: Include subfolders and files during organization.

- **Advanced Options (based on selected algorithm)**:
  - **Threshold (optional)**: Set a threshold for grouping similar files (applies to Group Similar).
  - **Regex Pattern**: Enter a regular expression pattern (applies to Organize by Regex).

- Click on the **Organize Files** button to initiate the organization process.

### Proposed Folder Structure Window

After clicking **Organize Files**, a new window will appear, displaying the proposed folder structure based on your selections. Here, you can:

- Toggle the **Advanced Filter** option to open an editor for custom filtering.

- Choose whether to **Move** or **Copy** files (default is copy).

- Decide whether to **consider miscellaneous files/folders** or not.

- Click **Apply Changes** to execute the proposed changes.

### Reverting Changes

If you want to revert the changes made by the File Organizer, go to **File > Revert Changes**. Select the directory for reverting its structure, and the changes will be reverted (make sure 'revert_info.json' exists in the directory).

### Create .ignore file

To Create empty .ignore file:Go to **File > Create .ignore file** Use this option to create or update a .ignore file with patterns to exclude specific files or directories from organization.

## Troubleshooting

If you encounter any issues during the organization process, the program will display informative error messages. Please double-check your inputs and ensure the source directory exists.

For additional assistance, feel free to reach out to the program's developer.
  - email: aashish06327@gmail.com

That's it! You're now ready to efficiently organize your files using the File Organizer. Happy organizing!