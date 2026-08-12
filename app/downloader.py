import requests
import os
from datetime import datetime

def download_pdf(url, folder_name="e-statements"):
    """Download a PDF from a URL and save it to a folder."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    today = datetime.now().strftime("%Y-%m-%d")
    response = requests.get(url)

    if response.status_code == 200:
        filename = f"{folder_name}/statement_{today}.pdf"
        with open(filename, "wb") as file:
            file.write(response.content)
        return {"status": "success", "filename": filename}
    else:
        return {"status": "error", "code": response.status_code}
