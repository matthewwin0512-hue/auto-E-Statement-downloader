import os
from typing import List, Optional

def get_existing_statements(bank_name: str, base_dir: str = "e-statements") -> List[str]:

    folder_path = os.path.join(base_dir, bank_name)

    if not os.path.exists(folder_path):
        return []

    files = os.listdir(folder_path)
    pdf_files = [f for f in files if f.endswith(".pdf")]

def get_latest_statement_filename(bank_name: str, base_dir: str = "e_statements") -> Optional[str]:
    files = get_existing_statements(bank_name, base_dir)

    if not files:
        return None

    files.sort(reverse = True)
    return files[0]

def statement_exists(bank_name: str, statement_filename: str, base_dir: str = "e-statements") -> bool:
    files = get_existing_statements(bank_name, base_dir)
    return statement_filename in files

# below code for testing

if __name__ == "__main__":
    # Create a test folder with a dummy file
    os.makedirs("e-statements/Santander", exist_ok=True)
    
    # Create a dummy file
    with open("e-statements/Santander/2026-07-01_statement.pdf", "w") as f:
        f.write("dummy")
    
    # Test the functions
    print("Existing statements:", get_existing_statements("Santander"))
    print("Latest:", get_latest_statement_filename("Santander"))