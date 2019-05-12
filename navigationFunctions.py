from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import configparser

import printfulAutomation

parser = configparser.ConfigParser()

parser.read('config.ini')

printfulUsername = parser.get('printful', 'printfulUsername')

printfulPassword = parser.get('printful', 'printfulPassword')

patternPopStoreId = parser.get('printful', 'patternPopStoreId')

class NavigationFunctions():

    def loginToPrintful(self, browser):
        browser.get("https://www.printful.com/auth/login")

        emailField = browser.find_element_by_id("customer-email")

        passwordField = browser.find_element_by_id("customer-password")

        emailField.send_keys(printfulUsername)

        passwordField.send_keys(printfulPassword, Keys.ENTER)

    def goToChooseProduct(self, browser):
        
        browser.get("https://www.printful.com/dashboard/sync?store=" + patternPopStoreId)

        printfulAutomation.waitForPageLoad()

        addProductButton = browser.find_element_by_xpath("//*[text()='Add product']")

        addProductButton.click()

        printfulAutomation.waitForPageLoad()

    def navigateToAllOverShirts(self, browser):
        allOverShirtsButton = browser.find_element_by_xpath("//h3[text()='All-over shirts']")

        browser.execute_script("arguments[0].scrollIntoView();", allOverShirtsButton)

        allOverShirtsButton.click()

    def navigateToMensAllOverShirts(self, browser):
        # Prerequisite: goToChooseProduct
        mensClothingButton = browser.find_element_by_xpath("//h3[text()= \"Men's clothing\"]")

        mensClothingButton.click()

        self.navigateToAllOverShirts(browser)

    def navigateToWomensAllOverShirts(self, browser):
        # Prerequisite: goToChooseProduct
        womensClothingButton = browser.find_element_by_xpath("//h3[text()= \"Women's clothing\"]")

        womensClothingButton.click()

        self.navigateToAllOverShirts(browser)

    def navigateToSweatshirts(self, browser):
        # Prerequisite: goToChooseProduct
        sweatersButton = browser.find_element_by_xpath("//a[text()= 'Sweatshirts']") # Mens is the one that shows up first i nthe DOM. Womens is second.

        sweatersButton.click()

    def navigateToMensShorts(self, browser):

        shortsButton = browser.find_element_by_xpath("//a[text()= 'Shorts']") # Mens is the one that shows up first i nthe DOM. Womens is second.

        shortsButton.click()

    def navigateToWomensShorts(self, browser):

        womensClothingButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[2]')

        womensClothingButton.click()

        womensShortsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li/ul/li[4]/ul/li[4]/a')

        womensShortsButton.click()

    def navigateToMensLeggings(self, browser):

        leggingsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[1]/ul/li[4]/ul/li[2]/a')

        leggingsButton.click()

    def navigateToWomensLeggings(self, browser):

        womensClothingButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[2]')

        womensClothingButton.click()

        leggingsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li/ul/li[4]/ul/li[2]/a')

        leggingsButton.click()

    def navigateToCreateProductStyle(self, browser, productStyle):
        # Prerequisite: Must be in a category, like navigateToMensAllOverShirts
        productStyleButton = browser.find_elements_by_xpath("//*[contains(text(), '%s')]" % productStyle)[-1] #last one in the ist AKA theone in the modal

        productStyleButton.click()

        printfulAutomation.waitForPageLoad()


    def proceedToProductDescription(self, browser):
        proceedToMockupsButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to mockups')]")

        proceedToMockupsButton.click()

        proceedToDescriptionButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to description')]")

        proceedToDescriptionButton.click()

        printfulAutomation.waitForPageLoad()

    def proceedToPricing(self, browser):
        proceedToPricingButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to pricing')]")

        proceedToPricingButton.click()

        printfulAutomation.waitForPageLoad()

    def clickSubmitButton(self, browser):
        submitItemButton = browser.find_element_by_xpath("//*[contains(text(), 'Submit to store')]")

        submitItemButton.click()



