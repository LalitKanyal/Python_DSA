import os

# Get the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Define the new directory path inside the current directory
new_dir_name = "a_directory"
new_dir_path = os.path.join(current_dir, new_dir_name)

# Create the new directory
try:
    os.mkdir(new_dir_path)
    print(f"Directory '{new_dir_name}' created at {new_dir_path}")
except FileExistsError:
    print(f"Directory '{new_dir_name}' already exists.")

# Change to the newly created directory
os.chdir(new_dir_path)

# List files in the new directory
files = os.listdir()
print("Files in newly created directory:", files)
