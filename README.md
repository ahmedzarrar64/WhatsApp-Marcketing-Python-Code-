# 📤 WhatsApp Bulk Sender via Selenium (CSV-Based | 60-Second Delay) #
This Python script automates WhatsApp Web messaging using Selenium. It reads phone numbers and personalized messages from a .csv file and sends each message with a 60-second delay between sends to avoid detection or bans.

✅ Features:
Send messages via WhatsApp Web automation

Load contacts and messages from a CSV file

Wait 60 seconds before sending the next message

Detect and skip invalid numbers

Simple and clean script — no third-party WhatsApp API required

🧾 CSV File Format:
Your file should look like this:

csv
Copy
Edit
phone,message
923001*****,"Hello! This is your reminder."
923008****,"Good morning, hope you're well!"
🚀 How to Use:
Install required packages:

bash
Copy
Edit
pip install selenium pandas
Download the correct ChromeDriver version for your Chrome.

Run the script:

bash
Copy
Edit
python whatsapp_sender.py
Scan the QR code in the browser.

Sit back and watch messages being sent every 60 seconds!

🛠 Tech Stack:
Python

Selenium

pandas

WhatsApp Web

⚠️ Disclaimer:
This tool is for educational or business automation use only. Do not use it to spam users. Respect WhatsApp's terms of service.

