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

    def navigateToMensAllOverShirts(self, browser):
        # Prerequisite: goToChooseProduct
        mensClothingButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[1]')

        mensClothingButton.click()

        allOverShirtsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[5]')

        allOverShirtsButton.click()

    def navigateToWomensAllOverShirts(self, browser):
        # Prerequisite: goToChooseProduct
        womensClothingButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[2]')

        womensClothingButton.click()

        allOverShirtsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[3]')

        allOverShirtsButton.click()

    def navigateToSweaters(self, browser):
        # Prerequisite: goToChooseProduct
        sweatersButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[1]/ul/li[3]/ul/li[2]/a')

        sweatersButton.click()

    def navigateToMensShorts(self, browser):

        shortsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[1]/ul/li[4]/ul/li[3]/a')

        shortsButton.click()

    def navigateToMensLeggings(self, browser):

        leggingsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[1]/ul/li[4]/ul/li[2]/a')

        leggingsButton.click()

    def navigateToCreateProductStyle(self, browser, productStyle):
        # Prerequisite: Must be in a category, like navigateToMensAllOverShirts
        productStyleButton = browser.find_elements_by_xpath("//*[contains(text(), '%s')]" % productStyle)[-1] #last one in the ist AKA theone in the modal

        productStyleButton.click()


    def proceedToProductDescription(self, browser):
        proceedToMockupsButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to mockups')]")

        proceedToMockupsButton.click()

        proceedToDescriptionButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to description')]")

        proceedToDescriptionButton.click()

    def proceedToPricing(self, browser):
        proceedToPricingButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to pricing')]")

        proceedToPricingButton.click()

    def clickSubmitButton(self, browser):
        submitItemButton = browser.find_element_by_xpath("//*[contains(text(), 'Submit to store')]")

        submitItemButton.click()



