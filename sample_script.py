from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
#driver.get('https://www.google.com/')
driver.get('https://soft.reelly.io/sign-in')

# populate search field

#search = driver.find_element(By.NAME, 'q')
#search.clear()
email = driver.find_element(By.XPATH, '//input[@data-name="Email 2"]')
password = driver.find_element(By.XPATH, '//input[@data-name="Password"]')
email.send_keys('test@gmail.com')
password.send_keys('test')

    # input email

driver.find_element(By.XPATH, '//*[@wized="loginButton"]').click()
#search.send_keys('Car')

# wait for 4 sec
sleep(4)

#click the market button
driver.find_element(By.XPATH, "//a[@href='https://soft.reelly.io']").click()

#verify right page
assert 'offers'.lower() in driver.find_element(By.CSS_SELECTOR,".new-market-h1").text.lower(), f"Expected query not in {driver.find_element(By.CSS_SELECTOR,".new-market-h1").text.lower()}"
#click developer


#verify the developer tag
developer_tag = driver.find_element(By.CSS_SELECTOR, "[wized ='servicesOffersCardCientTagText']")

assert 'developer'.lower() in developer_tag.text.lower(), f"Expected query not in {developer_tag.text.lower()}"
# click search button
#driver.find_element(By.NAME, 'btnK').click()

# verify search results
#assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
#print('Test Passed')

driver.quit()
