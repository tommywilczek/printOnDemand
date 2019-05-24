from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

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

        # printfulAutomation.waitForPageLoad()

        # addProductButton = browser.find_element_by_xpath("//*[text()='Add product']")

        addProductButton = self.waitUntilElementLocatedByXpath(browser, "//*[text()='Add product']")

        addProductButton.click()

        printfulAutomation.waitForPageLoad()

    def navigateToWomensClothing(self, browser):
        womensClothingButton = browser.find_element_by_xpath("//h3[text()= \"Women's clothing\"]")

        womensClothingButton.click()

    def navigateToKidsClothing(self, browser):
        kidsClothingButton = browser.find_element_by_xpath("//h3[text()= \"Kids & youth clothing\"]")

        browser.execute_script("arguments[0].scrollIntoView();", kidsClothingButton)

        kidsClothingButton.click()


    def navigateToAllOverShirts(self, browser):
        # allOverShirtsButton = browser.find_element_by_xpath("//h3[text()='All-over shirts']")

        allOverShirtsButton = self.waitUntilElementLocatedByXpath(browser, "//h3[text()='All-over shirts']")

        browser.execute_script("arguments[0].scrollIntoView();", allOverShirtsButton)

        allOverShirtsButton.click()

    def navigateToMensAllOverShirts(self, browser):
        # Prerequisite: goToChooseProduct
        # mensClothingButton = browser.find_element_by_xpath("//h3[text()= \"Men's clothing\"]")

        mensClothingButton = self.waitUntilElementLocatedByXpath(browser, "//h3[text()= \"Men's clothing\"]")

        mensClothingButton.click()

        self.navigateToAllOverShirts(browser)

    def navigateToWomensAllOverShirts(self, browser):
        # Prerequisite: goToChooseProduct
        self.navigateToWomensClothing(browser)

        self.navigateToAllOverShirts(browser)

    def navigateToSweatshirts(self, browser):
        # Prerequisite: goToChooseProduct
        sweatersButton = browser.find_element_by_xpath("//a[text()= 'Sweatshirts']") # Mens is the one that shows up first i nthe DOM. Womens is second.

        sweatersButton.click()

    def navigateToMensShorts(self, browser):

        shortsButton = browser.find_element_by_xpath("//a[text()= 'Shorts']") # Mens is the one that shows up first i nthe DOM. Womens is second.

        shortsButton.click()

    def navigateToMensLeggings(self, browser):

        leggingsButton = browser.find_element_by_xpath("//a[text()= 'Leggings']") # Mens is the one that shows up first i nthe DOM. Womens is second.

        leggingsButton.click()
    
    def navigateToLeggings(self, browser):

        leggingsButton = browser.find_element_by_xpath("//h3[text()= 'Leggings']")

        browser.execute_script("arguments[0].scrollIntoView();", leggingsButton)

        printfulAutomation.waitForPageLoad()

        leggingsButton.click()

    def navigateToWomensLeggings(self, browser):

        self.navigateToWomensClothing(browser)

        self.navigateToLeggings(browser)

    def navigateToSwimwear(self, browser):
        swimwearButton = browser.find_element_by_xpath("//h3[text()= 'Swimwear']")

        browser.execute_script("arguments[0].scrollIntoView();", swimwearButton)

        printfulAutomation.waitForPageLoad()

        swimwearButton.click()


    def navigateToWomensSwimwear(self, browser):

        self.navigateToWomensClothing(browser)

        self.navigateToSwimwear(browser)

    def navigateToKidsAllOverShirts(self, browser):

        self.navigateToKidsClothing(browser)

        self.navigateToAllOverShirts(browser)

    def navigateToKidsLeggings(self, browser):

        self.navigateToKidsClothing(browser)

        self.navigateToLeggings(browser)

    def navigateToKidsSwimwear(self, browser):

        self.navigateToKidsClothing(browser)

        self.navigateToSwimwear(browser)

    def navigateToAccessories(self, browser):

        accessoriesButton = self.waitUntilElementLocatedByXpath(browser, "//h3[text()= 'Accessories']")

        # accessoriesButton = browser.find_element_by_xpath("//h3[text()= 'Accessories']")

        accessoriesButton.click()


    def navigateToBags(self, browser):

        self.navigateToAccessories(browser)

        bagsButton = self.waitUntilElementLocatedByXpath(browser, "//a[text()= 'Bags']")

        # bagsButton = browser.find_element_by_xpath("//a[text()= 'Bags']")

        browser.execute_script("arguments[0].scrollIntoView();", bagsButton)

        bagsButton.click()

    def navigateToFlipFlops(self, browser):

        self.navigateToAccessories(browser)

        flipFlopsButton = browser.find_element_by_xpath("//a[text()= 'Flip flops']")

        browser.execute_script("arguments[0].scrollIntoView();", flipFlopsButton)

        printfulAutomation.waitForPageLoad()

        flipFlopsButton.click()



    def navigateToCreateProductStyle(self, browser, productStyle):
        # Prerequisite: Must be in a category, like navigateToMensAllOverShirts
        productStyleButton = browser.find_elements_by_xpath("//*[contains(text(), '%s')]" % productStyle)[-1] #last one in the ist AKA theone in the modal

        # productStyleButton = self.waitUntilElementLocatedByXpath(browser, "//*[contains(text(), '" + productStyle + "')]")

        productStyleButton.click()

        printfulAutomation.waitForPageLoad()


    def proceedToProductDescription(self, browser):
        # proceedToMockupsButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to mockups')]")

        proceedToMockupsButton = self.waitUntilElementLocatedByXpath(browser, "//*[contains(text(), 'Proceed to mockups')]")

        proceedToMockupsButton.click()

        # proceedToDescriptionButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to description')]")

        proceedToDescriptionButton = self.waitUntilElementLocatedByXpath(browser, "//*[contains(text(), 'Proceed to description')]")

        proceedToDescriptionButton.click()

        printfulAutomation.waitForPageLoad()

    def proceedToPricing(self, browser):
        # proceedToPricingButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to pricing')]")

        proceedToPricingButton = self.waitUntilElementLocatedByXpath(browser, "//*[contains(text(), 'Proceed to pricing')]")

        proceedToPricingButton.click()

        printfulAutomation.waitForPageLoad()

    def clickSubmitButton(self, browser):
        # submitItemButton = browser.find_element_by_xpath("//*[contains(text(), 'Submit to store')]")

        submitItemButton = self.waitUntilElementLocatedByXpath(browser, "//*[contains(text(), 'Submit to store')]")

        submitItemButton.click()

    def waitUntilElementLocatedByXpath(self, browser, xpath):
        wait = WebDriverWait(browser, 10)

        elementToInteractWith = wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))

        return elementToInteractWith

