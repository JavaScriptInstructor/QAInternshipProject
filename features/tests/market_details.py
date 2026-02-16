#test to check for developer tags on all three cards
from sample_script import driver

driver.find_element(By.CSS_SELECTOR, "[wized ='servicesOffersCardCientTagText']")