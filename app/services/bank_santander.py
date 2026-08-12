from app.services.bank_base import BankBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SantanderBank(BankBase):
    def login(self):
        print(f"Logging into Santander as {self.username}...")

        # Set up Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        #to santander login page
        driver.get("https://retail.santander.co.uk/olb/app/logon/access/#/logon")

        #cookie consent
        try:
            time.sleep(10)
            accept_button = driver.find_element(By.ID, 'onetrust-reject-all-handler')
            accept_button.click()
            print("Cookie consent rejected")
            time.sleep(1)
        except:
            print('No cookie consent button found')

        #username
        username_field = driver.find_element(By.ID, "pid")
        username_field.send_keys(self.username)

        #password
        password_field = driver.find_element(By.ID, "securityNumber")
        password_field.send_keys(self.password)

        #locate and activate login
        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "submitbtn"))
        )
        driver.execute_script("arguments[0].click();", login_button)
        print("Login button clicked via JavaScript")

        time.sleep(5)

        print(f"URL after login: {driver.current_url}")
        print(f"Page title: {driver.title}")

        # access to the e-statement page
        statements_link = driver.find_element(By.LINK_TEXT, "Statements and documents")
        statements_link.click()
        return driver

    def get_latest_statements(self, driver):
        print("Finding latest Santander e-statement...")
        # TODO: Navigate to e-statements
        # TODO: Identify the latest one
        return "santander_statement_2026-07-01.pdf"

    def download_statement(self, driver, filename: str):
        print(f"Downloading Santander statement: {filename}")
        # TODO: Click download button
        return f"e-statements/Santander/{filename}"