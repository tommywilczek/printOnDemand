from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from pprint import pprint
import json

import keywordLookup
import printfulAutomation
import navigationFunctions
import itemClasses

class generateProductMethods():
    # TODO: don't make a shirt subclass, just item... or maybe make more specific create methods?
    def createAllSleevedShirts(self, browser, sleevedShirtTypeList, color, genderParameter):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        for index in range(len(sleevedShirtTypeList)):

            newItem = itemClasses.item(sleevedShirtTypeList[index], 'shirt', color, True, gender=genderParameter)

            navigationFunctionsObject = navigationFunctions.NavigationFunctions()

            navigationFunctionsObject.navigateToCreateProductStyle(browser, newItem.productStyle)

            printfulAutomation.waitForPageLoad()

            generateProductMethods.clickColorRadioButtonIfAvailable(self, browser, 'white')

            generateProductMethods.chooseFirstColor(self, browser, newItem.colorName)

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

            generateProductMethods.clickSubmit(self, browser, newItem)



            navigationFunctionsObject.goToChooseProduct(browser)

            printfulAutomation.waitForPageLoad()

            lastIndex = len(sleevedShirtTypeList) - 1

            if index is not lastIndex:
                print('not last index')
                if genderParameter == 'Mens':
                    navigationFunctionsObject.navigateToMensAllOverShirts(browser)
                elif genderParameter == 'Womens':
                    navigationFunctionsObject.navigateToWomensAllOverShirts(browser)
            
            printfulAutomation.waitForPageLoad()

    def createFrontBackItem(self, browser, productCategory, frontBackItemList, color, genderParameter):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        for index in range(len(frontBackItemList)):

            newItem = itemClasses.item(frontBackItemList[index], productCategory, color, False, gender=genderParameter)

            navigationFunctionsObject = navigationFunctions.NavigationFunctions()

            navigationFunctionsObject.navigateToCreateProductStyle(browser, newItem.productStyle)

            printfulAutomation.waitForPageLoad()

            generateProductMethods.clickColorRadioButtonIfAvailable(self, browser, 'white')

            generateProductMethods.chooseFirstColor(self, browser, newItem.colorName)

            printfulAutomation.waitForPageLoad()

            generateProductMethods.chooseBackOfItemColor(self, browser, newItem)
            printfulAutomation.waitForPageLoad()

            printfulAutomation.waitForPageLoad()

            navigationFunctionsObject.proceedToProductDescription(browser)

            printfulAutomation.waitForPageLoad()
            
            generateProductMethods.createProductDescription(self, browser, newItem)

            navigationFunctionsObject.proceedToPricing(browser)

            printfulAutomation.waitForPageLoad()

            generateProductMethods.upchargeByPercentage(self, browser)

            generateProductMethods.clickSubmit(self, browser, newItem)

            navigationFunctionsObject.goToChooseProduct(browser)

            printfulAutomation.waitForPageLoad()

            lastIndex = len(frontBackItemList) - 1

            if index is not lastIndex:
                if genderParameter == 'Mens':
                    navigationFunctionsObject.navigateToMensAllOverShirts(browser)
                elif genderParameter == 'Womens':
                    navigationFunctionsObject.navigateToWomensAllOverShirts(browser)
            
            printfulAutomation.waitForPageLoad()

    def createFrontItem(self, browser, productCategory, frontItemList, color, genderParameter):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        for index in range(len(frontItemList)):

            newItem = itemClasses.item(frontItemList[index], productCategory, color, True, gender=genderParameter)

            navigationFunctionsObject = navigationFunctions.NavigationFunctions()

            navigationFunctionsObject.navigateToCreateProductStyle(browser, newItem.productStyle)

            printfulAutomation.waitForPageLoad()

            generateProductMethods.clickColorRadioButtonIfAvailable(self, browser, 'white')

            generateProductMethods.chooseFirstColor(self, browser, newItem.colorName)

            printfulAutomation.waitForPageLoad()

            navigationFunctionsObject.proceedToProductDescription(browser)

            printfulAutomation.waitForPageLoad()
            
            generateProductMethods.createProductDescription(self, browser, newItem)

            navigationFunctionsObject.proceedToPricing(browser)

            printfulAutomation.waitForPageLoad()

            generateProductMethods.upchargeByPercentage(self, browser)

            generateProductMethods.clickSubmit(self, browser, newItem)

            navigationFunctionsObject.goToChooseProduct(browser)

            printfulAutomation.waitForPageLoad()

            lastIndex = len(frontItemList) - 1

            if index is not lastIndex:
                if genderParameter == 'Mens':
                    navigationFunctionsObject.navigateToMensAllOverShirts(browser)
                elif genderParameter == 'Womens':
                    navigationFunctionsObject.navigateToWomensAllOverShirts(browser)
            
            printfulAutomation.waitForPageLoad()


    def clickColorRadioButtonIfAvailable(self, browser, color):

        try:
            browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % color)
        except NoSuchElementException:
            return 

        whiteRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % color)

        whiteRadioButton.send_keys(Keys.SPACE) # click radio button


    def chooseBackOfItemColor(self, browser, newShirt):
        backOfItemTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[2]/a/span')

        backOfItemTab.click()

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseFirstColor(self, browser, newShirt.colorName + '_mirror')

    def chooseSleeveColors(self, browser, newShirt):
        rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[3]/a/span')

        rightSleeveTab.click()

        generateProductMethods.chooseFirstColor(self, browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

        rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[4]/a/span')

        rightSleeveTab.click()

        generateProductMethods.chooseFirstColor(self, browser, newShirt.colorName + '_mirror')

    def chooseFirstColor(self, browser, colorName):
        uploadFileButton = browser.find_element_by_xpath("//*[contains(text(), 'Upload file')]")

        browser.execute_script("arguments[0].scrollIntoView();", uploadFileButton)

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
        if newItem.gender == 'Unisex':
            genderDescription = 'Mens Womens' # Usually says unisex in product style
        elif newItem.gender == None:
            genderDescription = ''
        else:
            genderDescription = newItem.gender

        colorName = newItem.colorName.replace('-', ' ')

        productKeywords = keywordLookup.keywordDict[newItem.productCategory]

        companyName = 'Pattern Pop'

        return companyName, ' ', colorName, ' ' , newItem.productStyle, ' ' ,productKeywords, ' ', genderDescription 

    def upchargeByPercentage(self, browser, ):
        # Must be in 'pricing' stage of create product
        dollarOrPercentageDropdown = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/table/thead/tr[2]/td[4]/span[2]/select/option[1]') 

        dollarOrPercentageDropdown.click()

        numberToIncreaseField = browser.find_element_by_class_name('profit-amount')

        numberToIncreaseField.clear()

        numberToIncreaseField.send_keys('15')

    def clickSubmit(self, browser, newItem):

        # navigationFunctionsObject.clickSubmitButton(browser)

        print('-----------')
        print('Created... \n', newItem.productStyle, newItem.productCategory, newItem.colorName, newItem.gender)
        print('-----------')
