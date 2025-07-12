from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import urllib.parse

# ✅ Automatically manage compatible ChromeDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# ✅ Open WhatsApp Web
driver.get("https://web.whatsapp.com")
input("🔒 QR code scan karein browser mein aur ENTER press karein...")

# ✅ Load contacts
df = pd.read_csv("contacts.csv", encoding='utf-8-sig')

for index, row in df.iterrows():
    number = str(row['phone'])
    message = str(row['message'])

    encoded_msg = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_msg}"
    driver.get(url)

    print(f"⏳ Waiting to load chat with {number}...")
    time.sleep(18)  # wait extra for slower load

    # ✅ Check for invalid number
    if "Phone number shared via url is invalid" in driver.page_source:
        print(f"⚠️ Number {number} is not on WhatsApp.")
        continue

    try:
        # ✅ Try standard button
        send_btn = driver.find_element(By.XPATH, '//button[@aria-label="Send"]')
        send_btn.click()
        print(f"✅ Message sent to {number}")
    except:
        try:
            # ✅ Try fallback button
            send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            send_btn.click()
            print(f"✅ Message sent to {number} [Fallback]")
        except Exception as e:
            print(f"❌ Failed to send to {number}: {e}")

    time.sleep(60)  # ⏳ 60 second delay to avoid detection

driver.quit()
