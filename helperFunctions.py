from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import configparser

import printfulAutomation

parser = configparser.ConfigParser()

parser.read('config.ini')

printfulPassword = parser.get('passwords', 'printfulPassword')

class NavigationFunctions():

    def loginToPrintful(self, browser):
        browser.get("https://www.printful.com/auth/login")

        emailField = browser.find_element_by_id("customer-email")

        passwordField = browser.find_element_by_id("customer-password")

        emailField.send_keys("tommywilczek@gmail.com")

        passwordField.send_keys(printfulPassword, Keys.ENTER)

    def goToChooseProduct(self, browser):
        patternPopStoreId = '1354143'
        
        browser.get("https://www.printful.com/dashboard/sync?store=" + patternPopStoreId)

        printfulAutomation.waitForPageLoad()

        addProductButton = browser.find_element_by_xpath("//*[text()='Add product']")

        addProductButton.click()

class newClass():
    def myTestMethod(self, browser):
        print('executing Test Method')