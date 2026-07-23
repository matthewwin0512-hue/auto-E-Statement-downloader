import requests
import os
from datetime import datetime

folder_name = "e-statements"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Created folder: {folder_name}")


today = datetime.now().strftime("%Y-%m-%d")

pdf_url = "https://retail.santander.co.uk/EBAN_Accounts_ENS/channel.ssobto?dse_operationName=contentTemplate&opCode=00000059&iurl=%2FMSEABB_ENS%2Fchannel.ssobto%3Fdse_operationName%3DOP_SecureMessages%26obtenerMensaje_E.esContactUs%3DN"

response = requests.get(pdf_url)

if response.status_code == 200:
    filename = f"{folder_name}/statement_{today}.pdf"
    with open(filename, "wb") as file:
        file.write(response.content)
    
    print(f"✅ Downloaded successfully: {filename}")
else:
    print(f"❌ Failed to download. Status code: {response.status_code}")