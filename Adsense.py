import time
from turtle import heading
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


s= Service('/Users/User/OneDrive/Desktop/AdSense/chromedriver.exe')

chromeOptions = Options()
chromeOptions.headless = False
chromeOptions.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=s, options=chromeOptions)

def accept_button(): 
   try:
     consent_button = driver.find_element(by=By.XPATH, value='//button[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "accept") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "agree") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "akzeptieren") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "consent") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "alles akzeptieren") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "cookies zulassen") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "notwendige cookies zulassen")]')
     consent_button.click()
   except: 
     print("notification was not found or could not be disabled")

def isAdsense():
   try: 
     if driver.find_element(by=By.CSS_SELECTOR, value='div[id*="google_ads_iframe"]'):
         return True
   except:
        return False
   
headings = [
    "Google DE",
    "Google Us",
    "Binge DE",
    "Binge Us"
    ]

file_path = '/Users/User/OneDrive/Desktop/AdSense/urls.txt'
output_file_path = '/Users/User/OneDrive/Desktop/AdSense/output.txt'

heading_index = 0

with open(file_path, 'r') as file, open(output_file_path, 'w') as output_file:
    line_count = 0
    
    while True:
        if heading_index < len(headings):
            output_file.write(headings[heading_index] + "\n")
            heading_index += 1
        
        for _ in range(20):
            line = file.readline().strip()
            if not line:
                break
            parts = line.split(': ')
            filename = parts[0]
            if len(parts) > 1 and any(part.startswith('https') for part in parts):
                url = [part for part in parts if part.startswith('https')][0]
                print(f"{filename}: {url}")
                driver.get(url)
                driver.maximize_window()
                time.sleep(15)
                try:
                    accept_button()
                    time.sleep(10)
                    if isAdsense():
                        output_file.write(f"{filename}:Adsense is visible\n")
                    else:
                        output_file.write(f"{filename}:Adsense is not visible\n")
                except Exception as e:
                    print("The process failed", e)
                    output_file.write(f"{filename}: something went wrong\n")
            else:
                print(f"{filename}: could not find URL")
                output_file.write(f"{filename}: could not find URL\n")
            line_count += 1
        
        if not line:
            break
        
        output_file.write("\n")
        if heading_index >= len(headings):
            heading_index = 0
    output_file.write("\n")