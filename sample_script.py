from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options

##Firefox

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
##Firefox
driver_path = GeckoDriverManager().install()

driver = webdriver.Firefox()
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Initialize the Firefox driver
driver = webdriver.Firefox(service=service)


# get the path to the ChromeDriver executable
##driver_path = ChromeDriverManager().install()
##service = Service(driver_path)
##driver = webdriver.Chrome(service=service)
##driver = webdriver.Chrome()
driver.maximize_window()

#chrome_options = Options()
#chrome_options.add_argument("--headless=new") # Use "--headless" for older versions
#driver = webdriver.Chrome(options=chrome_options)




def run_headless_chrome(url):
    # Create ChromeOptions object
    options = Options()

    # Add the headless argument. Use "--headless=new" for modern Chrome versions (109+).
    # The old "--headless" flag is still supported but less capable.
    #options.add_argument("--headless=new")

    # Recommended arguments for stability and compatibility
    options.add_argument("--disable-gpu")  # Temporarily needed for Windows in some cases
    options.add_argument("--no-sandbox")  # Required when running in containers
    options.add_argument("--window-size=1920,1080")  # Set a default window size for rendering

    # Initialize the WebDriver
    # If not using webdriver_manager, ensure the chromedriver is in your system's PATH
    #driver = webdriver.Chrome(options=options)
    # or if using webdriver_manager:
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


###driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
#service = Service(driver_path)
#driver = webdriver.Chrome(service=service)
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
