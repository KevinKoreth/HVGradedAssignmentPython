import sys
import os
import shutil
from datetime import datetime

def backup_files(source_dir:str, dest_dir:str)->None:
    """
    Copies files from a source directory to a destination directory, ensuring that
    file metadata is preserved. If a file with the same name already exists in the
    destination directory, a unique filename is generated using a timestamp.
    Args:
        source_dir (str): The path to the source directory containing files to back up.
        dest_dir (str): The path to the destination directory where files will be copied.
    Raises:
        FileNotFoundError: If the source or destination directory does not exist.
    Behavior:
        - Skips directories in the source directory.
        - Generates a unique filename with a timestamp if a file with the same name
          exists in the destination directory.
        - Preserves file metadata during the copy process.
        - Prints a success message for each file copied or an error message if the
          copy operation fails.
    """

    # Validate directories exist
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist")
    if not os.path.isdir(dest_dir):
        raise FileNotFoundError(f"Destination directory '{dest_dir}' does not exist")

    # Process each file in source directory
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        
        # Skip directories
        if not os.path.isfile(src_path):
            continue

        dest_path = os.path.join(dest_dir, filename)
        
        # Check if file exists in destination
        if os.path.exists(dest_path):
            # Generate unique filename with timestamp
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{base}_{timestamp}{ext}"
            dest_path = os.path.join(dest_dir, new_filename)

        try:
            # Copy file with metadata preservation
            shutil.copy2(src_path, dest_path)
            print(f"Successfully copied: {filename} -> {os.path.basename(dest_path)}")
        except Exception as e:
            print(f"Failed to copy {filename}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    try:
        backup_files(source, destination)
        print("\nBackup completed with above results")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)