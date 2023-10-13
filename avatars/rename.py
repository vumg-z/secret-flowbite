import os

directory = r'C:\Users\USER\Desktop\Flowbite_Starter\Flowbite_Starter\avatars'

# Function to rename files
def rename_jfif_files(directory):
    count = 2  # Start counting from 2
    for filename in os.listdir(directory):
        if filename.endswith('.jfif'):
            new_name = f'avatar{count}.jfif'
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            count += 1

# Rename the .jfif files in the specified directory
rename_jfif_files(directory)
