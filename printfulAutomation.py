from selenium import webdriver

from selenium.webdriver.common.keys import Keys

printfulPassword = input("enter printful password in quotes:")
print(printfulPassword)
    
browser = webdriver.Chrome('/Users/tommywilczek/Documents/Projects/chromedriver')

def main():

    loginToPrintful(printfulPassword)

    browser.get("https://www.printful.com/dashboard/store")

    browser.find_elements_by_xpath("//*[contains(text(), 'Add')]")

def loginToPrintful(printfulPassword):
    browser.get("https://www.printful.com/auth/login")

    emailField = browser.find_element_by_id("customer-email")

    passwordField = browser.find_element_by_id("customer-password")

    emailField.send_keys("tommywilczek@gmail.com")

    passwordField.send_keys(printfulPassword, Keys.ENTER)

main()