# Westbrook Last Date Pulled Info
# Sebago Technics Signal Operations 2023 @Vraj Thakkar

def get_latest_file(folder_path):
    
    # Importing Libraries
    import os

    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    folder_name = os.path.basename(folder_path)

    # Filter out non-files (e.g., subfolders)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Sort the files by modification timestamp in descending order
    sorted_files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)

    if sorted_files:
        latest_file = sorted_files[0]
        print(f"\nLast file pulled for folder {folder_name}: {latest_file}\n")
        return latest_file
    else:
        print(f"No files found in the folder {folder_name}")
        return None
