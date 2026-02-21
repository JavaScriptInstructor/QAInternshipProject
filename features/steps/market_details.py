from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
driver.maximize_window()

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


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