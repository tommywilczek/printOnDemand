from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import configparser

parser = configparser.ConfigParser()

parser.read('config.ini')

printfulPassword = parser.get('passwords', 'printfulPassword')

browser = webdriver.Chrome('/Users/tommywilczek/Documents/Projects/chromedriver')

def main():

    loginToPrintful(printfulPassword)
    waitForPageLoad()
    goToChooseProduct()

def loginToPrintful(printfulPassword):
    browser.get("https://www.printful.com/auth/login")

    emailField = browser.find_element_by_id("customer-email")

    passwordField = browser.find_element_by_id("customer-password")

    emailField.send_keys("tommywilczek@gmail.com")

    passwordField.send_keys(printfulPassword, Keys.ENTER)

def goToChooseProduct():
    patternPopStoreId = '1354143'
    
    browser.get("https://www.printful.com/dashboard/sync?store=" + patternPopStoreId)
    
    waitForPageLoad()

    addProductButton = browser.find_element_by_xpath("//*[text()='Add product']")

    addProductButton.click()


def waitForPageLoad():
    time.sleep(1)

main()