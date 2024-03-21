from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

#flow-> go to cuvette->click on login if not logged in ->then login ->get job listing
#                    ->opens dashboard if logged in  ---------------->get job lisitng
try:
    driver.get('https://cuvette.tech/app/student/login')
    wait = WebDriverWait(driver,30)
    wait.until(EC.presence_of_element_located((By.NAME,"email")))
except TimeoutException:
    print("Element not found in specified timeout")
except Exception as e:
    print(f"Error:{e}")

# Open the website
uname = driver.find_element(By.NAME, "email") 
uname.send_keys("mepiper2010@gmail.com") 
passwordF = driver.find_element(By.NAME, "password") 
passwordF.send_keys("bJ5FP#6he4dc9zv") 
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(10)




# try:
#     wait = WebDriverWait(driver, 10)
#     element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']"))) 
# except TimeoutException:
#     print("Element not found in specified timeout")

# except Exception as e:
#     print(f"Error:{e}")
# print(element)

# driver.find_element(By.XPATH,"//a[@href='/app/student/jobs/fulltimeJobs']").click()

# time.sleep(10)

# jobs = driver.find_element(By.CLASS_NAME,"FullTimeJobs_appliedJobs__3tCfg")
# soup = BeautifulSoup(jobs, 'html5lib')

# roles = soup.find_all('h3')
# print("Roles",roles)

driver.close()

