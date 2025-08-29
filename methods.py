import os

def save_to_dotenv(key, value):
    env_path = '.env'
    lines = []
    
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            lines = f.readlines()
    

    found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f"{key}={value}\n"
            found = True
            break
    if not found:
        lines.append(f"{key}={value}\n")
        
    with open(env_path, 'w') as f:
        f.writelines(lines)

def clean_terminal():
    if os.name == "posix":
        os.system("clear")
    else: # windows
        os.system("cls")

