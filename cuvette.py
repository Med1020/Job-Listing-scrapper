from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pickle
import os
from config import username,password
import pdb

cookie_file = "cookies.pkl"



def load_cookies(driver, cookie_file):
    pdb.set_trace()
    if os.path.exists(cookie_file) and os.path.getsize(cookie_file) > 0:
        with open(cookie_file, 'rb') as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
        return True
    else:
        return False

def save_cookies(driver, cookie_file):
    with open(cookie_file, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)

driver = webdriver.Chrome()



#flow-> go to cuvette->click on login if not logged in ->then login ->get job listing
#                    ->opens dashboard if logged in  ---------------->get job lisitng
try:
    if not load_cookies(driver,cookie_file):
        driver.get('https://cuvette.tech/app/student/login')
        wait = WebDriverWait(driver,30)
        wait.until(EC.presence_of_element_located((By.NAME,"email")))
except TimeoutException:
    print("login element not found in specified timeout")
except Exception as e:
    print(f"Error:{e}")
uname = driver.find_element(By.NAME, "email") 
uname.send_keys(username) 
passwordF = driver.find_element(By.NAME, "password") 
passwordF.send_keys(password) 
driver.find_element(By.XPATH, "//button[@type='submit']").click()
save_cookies(driver,cookie_file)

# Open the website
# time.sleep(10)



# try:
#     wait = WebDriverWait(driver, 30)
#     element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']"))) 
# except TimeoutException:
#     print("job listing element not found in specified timeout")

# except Exception as e:
#     print(f"Error:{e}")

# driver.find_element(By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']").click()

# time.sleep(10)

# try:
#     wait = WebDriverWait(driver,30)
#     wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME,"FullTimeJobs_appliedJobs__3tCfg"))
# except TimeoutException:
#     print("Element not found in specified timeout")

# except Exception as e:
#     print(f"Error:{e}")

# jobs = driver.find_element(By.CLASS_NAME,"FullTimeJobs_appliedJobs__3tCfg")
# job_Listing=[]

# for job in jobs:

#     role = driver.find_element(By.CSS_SELECTOR,"//h3")
#     company_name = driver.find_element(By.CSS_SELECTOR,"//p")
#     job_data = {
#         "Role":role,"Company":company_name
#     }
#     job_Listing.append(job_data)

# print(job_Listing)

driver.close()

