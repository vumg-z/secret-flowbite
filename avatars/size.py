import os

def get_directory_size(directory_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    return total_size

def format_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 * 1024:
        size_in_kb = size_in_bytes / 1024
        return f"{size_in_kb:.2f} KB"
    elif size_in_bytes < 1024 * 1024 * 1024:
        size_in_mb = size_in_bytes / (1024 * 1024)
        return f"{size_in_mb:.2f} MB"
    else:
        size_in_gb = size_in_bytes / (1024 * 1024 * 1024)
        return f"{size_in_gb:.2f} GB"

directory = r'C:\Users\USER\Desktop\Flowbite_Starter\Flowbite_Starter\avatars'
size = get_directory_size(directory)

# Define the prefix
prefix = "Size of the directory: "

# Convert and print the size with the appropriate unit
print(f"{prefix}{format_size(size)}")
