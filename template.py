# template.py
import os

# Define project structure
structure = {
    "agents": ["travel_agent.py", "flight_agent.py", "hotel_agent.py","train_agent.py"],
    "config": ["settings.py"],
    "utils": ["helpers.py"],
}

# Base files in root
base_files = [
    "main.py",
    "streamlit_app.py",
    "requirements.txt",
    "README.md",
    ".env",
    ".gitignore",
    ".dockerignore",
    "Dockerfile",
]

def create_structure():
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Create folders and their files
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            open(os.path.join(folder_path, file), "w").close()

    # Create base files
    for file in base_files:
        open(os.path.join(base_path, file), "w").close()

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
