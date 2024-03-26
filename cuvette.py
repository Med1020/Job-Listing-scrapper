from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import username,password
import pdb
from selenium.webdriver.chrome.options import Options

# cookie_file = "cookies.pkl"

# def load_cookies(driver, cookie_file):
#     # pdb.set_trace()
#     if os.path.exists(cookie_file) and os.path.getsize(cookie_file) > 0:
#         with open(cookie_file, 'rb') as f:
#             cookies = pickle.load(f)
#         for cookie in cookies:
#             pdb.set_trace()
#             driver.add_cookie(cookie)    
#             print(cookie)
#         return True
#     else:
#         return False

# def save_cookies(driver, cookie_file):
#     with open(cookie_file, 'wb') as f:
#         pickle.dump(driver.get_cookies(), f)

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode

driver = webdriver.Chrome()

#flow-> go to cuvette->click on login if not logged in ->then login ->get job listing
#                    ->opens dashboard if logged in  ---------------->get job lisitng

try:
    driver.get('https://cuvette.tech/app/student/login')
    wait = WebDriverWait(driver,30)
    wait.until(EC.presence_of_element_located((By.NAME,"email")))
    uname = driver.find_element(By.NAME, "email") 
    uname.send_keys(username) 
    passwordF = driver.find_element(By.NAME, "password") 
    passwordF.send_keys(password) 
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
except Exception as e:
    print("login timedout")
    

# Open the website
# time.sleep(10)
# driver.get("https://cuvette.tech/app/student/")
# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']")))



# try:
#     wait = WebDriverWait(driver, 30)
#     element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']"))) 
# except TimeoutException:
#     print("job listing element not found in specified timeout")

# except Exception as e:
#     print(f"Error:{e}")

element = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']")))
element.click()
# driver.find_element(By.XPATH("//a[@href='/app/student/jobs/fulltimeJobs']")).click()
# time.sleep(10)

try:
    wait = WebDriverWait(driver,60)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"FullTimeJobs_appliedJobs__3tCfg")))
except TimeoutException:
    print("Element not found in specified timeout")

except Exception as e:
    print(f"Error:{e}")

jobs = driver.find_elements(By.CLASS_NAME,"StudentJobCard_container__2h__W")
job_Listing=[]

for job in jobs:
    header_div = driver.find_element(By.CLASS_NAME, "StudentJobCard_heading__3eoXb")
    role = header_div.find_element(By.TAG_NAME,"h3")
    company_name = driver.find_element(By.TAG_NAME,"p")
    job_data = {
        "Role":role.text,"Company":company_name.text
    }
    job_Listing.append(job_data)

print(job_Listing)

driver.close()  

