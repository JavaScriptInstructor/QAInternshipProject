from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
##from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# get the path to the ChromeDriver executable
##driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
##service = Service(driver_path)
##driver = webdriver.Chrome(service=service)
##driver = webdriver.Chrome()
###driver.maximize_window()

##SEARCH_INPUT = (By.NAME, 'q')
##SEARCH_SUBMIT = (By.NAME, 'btnK')
def browser_init(context):
    """
    :param context: Behave context
    """

    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    #driver_path = GeckoDriverManager().install()
    ##driver = webdriver.Firefox()
    ##service = FirefoxService(executable_path=GeckoDriverManager().install())

    # Initialize the Firefox driver
    ##context.driver = webdriver.Firefox(service=service)

    ##context.driver.maximize_window()
    ##context.driver.implicitly_wait(4)
    ##context.driver.wait = WebDriverWait(context.driver, timeout=10)
    ##context.app = Application(context.driver)

### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'tiffany_rW308c'
    bs_key = 'ByA69tyS7pbqeHBvziyw'

    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        "os" : "Windows",
        "osVersion" : "11",
        "browserVersion" : "latest",
        'browserName': 'Safari',
        'sessionName': 'User can open market tab and filter',
     }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

@given('Open Reelly page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io')


@when('Log in to Reelly')
def click_login(context):
    # password input (XPATH)
    context.driver.find_element(By.XPATH, '//input[@data-name="Password"]')
    # input email
    context.driver.find_element(By.XPATH, '//input[@data-name="Email 2"]')
    context.driver.find_element(By.XPATH, '//*[@wized="loginButton"]').click()



@when('Verify the right page opens')
def verify_page(context):
#a href
#Click market button
  context.driver.find_element(By.XPATH,"//a[@href='https://soft.reelly.io']").click()

@when('Click on developer filter button')
def click_Market(context):
    context.driver.find_element(By.CSS_SELECTOR, "[wized ='servicesOffersFilterDeveloper']").click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'


#test to check for developer tags on all three cards
from selenium.webdriver.common.by import By

from sample_script import driver

#developer tag
driver.find_element(By.CSS_SELECTOR, "[wized ='servicesOffersCardCientTagText']")

#password input (XPATH)
driver.find_element(By.XPATH,'//input[@data-name="Password"]')
#input email
driver.find_element(By.XPATH,'//input[@data-name="Email 2"]')

#login button to 'click'
driver.find_element(By.XPATH,'//*[@wized="loginButton"]').click()

#a href
#Click market button
driver.find_element(By.XPATH,"//a[@href='https://soft.reelly.io']").click()

#verify correct page is shown
def verify_empty_cart_msg(self):
    self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_ACRT_MSG)

EMPTY_ACRT_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
empty_cart_msg = 'Your cart is empty'

#Offers for you
driver.find_element(By.CSS_SELECTOR,".new-market-h1")

#Click on Developer button
driver.find_element(By.CSS_SELECTOR,"[wized ='servicesOffersFilterDeveloper']").click()