import os

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Construct the path to the .env file in the same folder
env_file_path = os.path.join(current_dir, ".env")

# Write to the .env file
with open(env_file_path, "w") as f:
    try:
        launcher_path = input("Enter the Epic Games launcher path: ")
        email = input("Enter your Epic Games email: ")
        password = input("Enter your Epic Games password: ")
        
        f.write(f"LAUNCHER_PATH=\"{launcher_path}\"\n")
        f.write(f"EPIC_EMAIL={email}\n")
        f.write(f"EPIC_PASSWORD={password}\n")
    except Exception as e:
        print("Error writing to file:", str(e))

# Read the .env file and print its contents
with open(env_file_path, "r") as f:
    try:
        print("File Contents:")
        print(f.read())
    except Exception as e:
        print("Error reading file:", str(e))
