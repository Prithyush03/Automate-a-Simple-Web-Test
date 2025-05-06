from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Setup ===
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    # 1. Open the website
    driver.get("https://www.intervue.io")

    # 2. Click "Login" in header
    login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_btn.click()

    # Then navigate to: https://www.intervue.io/login
    driver.get("https://www.intervue.io/login")

    # 3. Enter email and password
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys("neha@intervue.io")     # <-- Replace with your email
    password_input.send_keys("Neha@567intervue")           # <-- Replace with your password

    # 4. Click "Login with email" button
    login_with_email_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Login with email →')]")
    login_with_email_btn.click()

    # 5. Navigation: Dashboard > Interview Panel
    dashboard_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Dashboard")))
    dashboard_link.click()

    interview_panel_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Interview Panel")))
    interview_panel_link.click()

    # 6. Form Fill: Enter candidate name & time
    candidate_name_input = wait.until(EC.presence_of_element_located((By.NAME, "candidateName")))
    interview_time_input = driver.find_element(By.NAME, "interviewTime")

    candidate_name_input.send_keys("John Doe")           # Example name
    interview_time_input.send_keys("12:30 PM")           # Adjust format as needed

    # 7. Click "Submit" or "Schedule"
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit') or contains(text(), 'Schedule')]")
    submit_btn.click()

    # 8. Log out
    profile_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='profile']")))
    profile_icon.click()

    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]")))
    logout_btn.click()

except Exception as e:
    print("⚠️ Error:", e)
    driver.save_screenshot("error_screenshot.png")
finally:
    time.sleep(2)
    driver.quit()
