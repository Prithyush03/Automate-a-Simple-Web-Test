This Python script automates the login, interview scheduling, and logout workflow on Intervue.io using Selenium WebDriver.

✅ Features
Logs into https://www.intervue.io

Navigates to the Interview Panel

Fills in candidate details and interview time

Schedules the interview

Logs out safely

Requirements
Python 3.x

Google Chrome browser

ChromeDriver installed and added to system PATH

Python packages:

bash
Copy
Edit
pip install selenium
📁 File Structure
Copy
Edit
intervue_automation/
├── script.py
└── README.md
🚀 How to Use
Clone the repo or copy the script.

Edit Credentials:
Open script.py and update these lines with your valid Intervue.io credentials:

python
Copy
Edit
email_input.send_keys("neha@intervue.io")
password_input.send_keys("Neha@567intervue")
Run the script:

bash
Copy
Edit
python script.py
The script will:

Open Chrome

Log into Intervue.io

Navigate to the Interview Panel

Enter John Doe as the candidate and 12:30 PM as the interview time

Schedule the interview

Log out

🛠 Error Handling
If any step fails, the script:

Prints the error in the terminal

Captures a screenshot as error_screenshot.png in the working directory for debugging

⚠️ Notes
Make sure you're using the correct field name, text, and xpath values. These may change if the website UI updates.

Adjust interview time format to match the input field’s accepted format.

Login and scheduling actions may require 2FA or additional verification depending on account settings.
