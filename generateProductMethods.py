from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import keywordLookup
import printfulAutomation
import navigationFunctions
import itemClasses

class generateProductMethods():

    def createSleevedShirt(self, browser, newItem):
        # Prerequisite: navigateToMensAllOverShirts

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        navigationFunctionsObject.navigateToCreateProductStyle(browser, newItem.productStyle)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.clickColorRadioButton(self, browser, 'white')

        generateProductMethods.chooseColor(self, browser, newItem.colorName)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseBackOfItemColor(self, browser, newItem)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseSleeveColors(self, browser, newItem)

        printfulAutomation.waitForPageLoad()

        navigationFunctionsObject.proceedToProductDescription(browser)

        printfulAutomation.waitForPageLoad()
        
        generateProductMethods.createProductDescription(self, browser, newItem)

        navigationFunctionsObject.proceedToPricing(browser)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.upchargeByPercentage(self, browser)

        submitItemButton = browser.find_element_by_xpath("//*[contains(text(), 'Submit to store')]")

        ########## For Testing
        print('Creating product of color:', newItem.colorName)
        navigationFunctionsObject.goToChooseProduct(browser)

        #########################
        # submitItemButton.click()
        printfulAutomation.waitForPageLoad()

    def clickColorRadioButton(self, browser, color):
        whiteRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % color)

        whiteRadioButton.send_keys(Keys.SPACE) # click radio button


    def chooseBackOfItemColor(self, browser, newShirt):
        backOfItemTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[2]/a/span')

        backOfItemTab.click()

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

    def chooseSleeveColors(self, browser, newShirt):
        rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[3]/a/span')

        rightSleeveTab.click()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

        rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[4]/a/span')

        rightSleeveTab.click()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

    def chooseColor(self, browser, colorName):
        uploadFileButton = browser.find_element_by_xpath("//*[contains(text(), 'Upload file')]")

        uploadFileButton.click()

        printfulAutomation.waitForPageLoad()

        colorSearch = browser.find_elements_by_xpath("//input[contains(@id,'library-search')]")[-1]

        colorSearch.send_keys(colorName)

        colorSearch.send_keys(Keys.ENTER)

        printfulAutomation.waitForPageLoad()

        frontColorChooserButton = browser.find_element_by_xpath('//*[@title="%s.png"]' % colorName)

        frontColorChooserButton.click()

    def createProductDescription(self, browser, newShirt):
        productDescription = generateProductMethods.generateProductDescription(self, browser, newShirt)

        productNameField = browser.find_element_by_class_name('form-control')

        productNameField.clear()

        productNameField.send_keys(productDescription)

        productNameField.send_keys(Keys.ENTER)

    def generateProductDescription(self, browser, newItem):
        if newItem.gender == 'unisex':
            genderDescription = 'Mens Womens Unisex'
        elif newItem.gender == None:
            genderDescription = ''
        else:
            genderDescription = newItem.gender

        colorName = newItem.colorName.replace('-', ' ')

        productKeywords = keywordLookup.keywordDict[newItem.productType]

        companyName = 'Pattern Pop'

        return companyName, ' ', colorName, ' ' , newItem.productStyle, ' ' ,productKeywords, ' ', genderDescription 

    def upchargeByPercentage(self, browser, ):
        # Must be in 'pricing' stage of create product
        dollarOrPercentageDropdown = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/table/thead/tr[2]/td[4]/span[2]/select/option[1]') 

        dollarOrPercentageDropdown.click()

        numberToIncreaseField = browser.find_element_by_class_name('profit-amount')

        numberToIncreaseField.clear()

        numberToIncreaseField.send_keys('15')
