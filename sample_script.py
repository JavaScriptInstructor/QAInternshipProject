from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
#chrome_options = Options()
#chrome_options.add_argument("--headless=new") # Use "--headless" for older versions
#driver = webdriver.Chrome(options=chrome_options)
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
#driver.get('https://www.google.com/')
driver.get('https://soft.reelly.io/sign-in')
print(f"Page title: {driver.title}")

# populate search field

#search = driver.find_element(By.NAME, 'q')
#search.clear()
email = driver.find_element(By.XPATH, '//input[@data-name="Email 2"]')
password = driver.find_element(By.XPATH, '//input[@data-name="Password"]')
email.send_keys('drtngraves@gmail.com')
password.send_keys('testcareerist')

    # input email

driver.find_element(By.XPATH, '//*[@wized="loginButton"]').click()
#search.send_keys('Car')

# wait for 4 sec
sleep(4)

#click the market button
driver.find_element(By.XPATH, "//a[@href='https://soft.reelly.io']").click()

sleep(4)

#Click on Developer button
driver.find_element(By.CSS_SELECTOR,"[wized ='servicesOffersFilterDeveloper']").click()

#verify right page
verify_page = driver.find_element(By.CSS_SELECTOR,".new-market-h1")
#print(verify_page.text)
assert 'offers'.lower() in driver.find_element(By.CSS_SELECTOR,".new-market-h1").text.lower(), f"Expected query not in {driver.find_element(By.CSS_SELECTOR,".new-market-h1").text.lower()}"
#click developer

sleep(5)

#verify the developer tag
developer_tag = driver.find_element(By.CSS_SELECTOR, "[wized ='servicesOffersCardCientTagText']")
#number_ofresults = driver.find_element(By.CSS_SELECTOR, '[wized="servicesOffersCard"]')
print(developer_tag.text)
#print(number_ofresults.text)
if (developer_tag.text.lower()) == 'developer':
    print(True)
else:
    print(False)

#assert 'developer' in developer_tag(), f"Expected query not in {developer_tag.text.lower()}"
# click search button
#driver.find_element(By.NAME, 'btnK').click()

# verify search results
#assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
#print('Test Passed')

driver.quit()
