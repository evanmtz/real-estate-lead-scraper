from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initializing "ser" variable and assigning it the Service class with the argument being the path to the chromedriver file.
ser = Service("C:\Program Files (x86)\chromedriver.exe")

# Could've coded this, but someone already made it so might as well use it right? 
def login():
    driver.get('https://login.propstream.com/')
    # This was my addition btw
    driver.maximize_window()
    time.sleep(3)
    username = driver.find_element(By.XPATH, '//*[@id="form-content"]/form/input[1]')
    username.send_keys('USERNAME_OR_EMAIL')
    password = driver.find_element(By.XPATH, '//*[@id="form-content"]/form/input[2]')
    password.send_keys('PASSWORD')
    login_btn = driver.find_element(By.XPATH, '//*[@id="form-content"]/form/button')
    login_btn.click()
    time.sleep(3)

# WHY IS ACTIONCHAINS EVEN A THING 
driver = webdriver.Chrome(service=ser)
actions = ActionChains(driver)
login()

try:
    proceed_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[2]')
    proceed_btn.click()
    print('logged someone else out')
    time.sleep(3)
except:
    print('already logged in')

close_btn = driver.find_element(By.XPATH, '//*[@id="alert"]/div/div/div/div/div/div/div[2]/button')
close_btn.click()
time.sleep(3)

search = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[1]/div/div/div/div/input')
search.send_keys("CITY_STATE_ZIPCODE_OR_COUNTY")
time.sleep(3)
actions.send_keys(Keys.ENTER)
actions.perform()
print("Properties loaded...")

time.sleep(3)

# YES I KNOW ALL THIS COULD'VE BEEN AVOIDED EASILY IF I JUST MADE A FUNCTION, BUT MY MAIN GOAL WAS TO PULL LEADS, NOT TO CODE EFFICIENTLY (I'll make a function on my next script lol)
prefBtn = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[2]/div[1]/div/div[2]/div/button/div/div[1]/div/div/div')
prefBtn.click()


filtBtn = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div')
filtBtn.click()


propCh = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/span')
propCh.click()


clsf = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]')
clsf.click()


res = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/label/span')
res.click()


pT = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]')
pT.click()


sF = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/label/span')
sF.click()


mls = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/span')
mls.click()


No = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[3]/div/label/span')
No.click()


pFbO = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[1]/span')
pFbO.click()


dates = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div/div/input')
dates.click()

# I like pulling leads from 3 months ago to now.
dates.send_keys("03/01/23")
actions.send_keys(Keys.ENTER)
actions.perform()


own = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/span')
own.click()

ownShip = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/input')
ownShip.send_keys("3")


ownType = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/div/div[2]')
ownType.click()

Indv = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/label/span')
Indv.click()

equity = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[7]/div[1]/span')
equity.click()

eqNum = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[7]/div[2]/div[7]/div[2]/div/div/input')
eqNum.send_keys("40")

equity.click()

closeBtn = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[2]/button[1]/div[1]')
closeBtn.click()

time.sleep(5)

filt = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/section/div[2]/div/div/div/div/div[1]/div[2]/button[1]/span')
filt.click()

# There was a "next" button I was trying to click with the click() method but I kept getting a stable element error, so I just created this. Still does the job c:
listOfNums = ["51", "101", "151", "201", "251", "301", "349"]

leadList = []

# THIS IS WHAT SCRAPED 300+ PRE-FORECLOSURE LEADS!
for num in listOfNums:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    listOfProperties = soup.find_all('div', class_ = '_3WJPT__item')

    try:
        changeNum = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[1]/div/section/div[2]/div/div/div/div/div[1]/div[1]/div[2]/input[1]')
        changeNum.click()
        actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(Keys.BACKSPACE)
        actions.perform()
        changeNum.send_keys(num)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print("New properties loaded")

    except:
        print("Unable to locate changeNum path.")
        
    for property in listOfProperties:
        # I tried separating the info piece by piece, but these 2 seemed to be the only attributes in the source code. So lead is city, state, and zip all together.
        lead = property.find('div', class_ = 'ddKyu__left').text.strip()
        # xtraLeadInfo is sq ft, bed/bath, lot, etc.
        xtraLeadInfo = property.find('div', class_ = '_6n1C___right').text.strip()

        leadInfo = {
            'Location': lead,
            'Characteristics': xtraLeadInfo
        }

        leadList.append(leadInfo)
    
    time.sleep(10)

df = pd.DataFrame(leadList)

# I store the data in a file
df.to_csv('leads.csv')
print("Leads pulled :)")
