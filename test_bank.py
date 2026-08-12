from app.services.bank_santander import SantanderBank
from selenium.webdriver.common.by import By
import time

# Test the Santander bank
bank = SantanderBank()
driver = bank.login()

#check login status
current_url = driver.current_url
print(f"URL after login: {current_url}")
time.sleep(50)

filename = bank.get_latest_statements(driver)
bank.download_statement(driver, filename)