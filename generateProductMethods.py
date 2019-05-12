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

    def createNewProduct(self, browser, itemCategory, itemTypeList, color, genderParameter):
        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        for index in range(len(itemTypeList)):

            newItem = itemClasses.item(itemTypeList[index], itemCategory, color, True, gender=genderParameter)

            navigationFunctionsObject = navigationFunctions.NavigationFunctions()

            navigationFunctionsObject.navigateToCreateProductStyle(browser, newItem.productStyle)

            generateProductMethods.clickColorRadioButtonIfAvailable(self, browser, 'white')

            generateProductMethods.chooseColor(self, browser, newItem.colorName)

            generateProductMethods.chooseBackOfItemColorIfAvailable(self, browser, newItem)

            generateProductMethods.chooseRightSleeveColorsIfAvailable(self, browser, newItem)

            generateProductMethods.chooseLeftSleeveColorsIfAvailable(self, browser, newItem)

            generateProductMethods.chooseLeftLegColorIfAvailable(self, browser, newItem)

            navigationFunctionsObject.proceedToProductDescription(browser)
            
            generateProductMethods.createProductDescription(self, browser, newItem)

            navigationFunctionsObject.proceedToPricing(browser)

            generateProductMethods.upchargeByPercentage(self, browser)

            generateProductMethods.submitProduct(self, browser, newItem)

            navigationFunctionsObject.goToChooseProduct(browser)

            lastIndex = len(itemTypeList) - 1

            if index is not lastIndex: # How to return to accessories, etc?

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


    def chooseBackOfItemColorIfAvailable(self, browser, newShirt):
        
        backOfItemTab = generateProductMethods.findElement(self, browser, 'back')

        if backOfItemTab == False:
            return

        backOfItemTab.click()

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

    def chooseRightSleeveColorsIfAvailable(self, browser, newShirt):

        rightSleeveTab = generateProductMethods.findElement(self, browser, 'right sleeve')

        if rightSleeveTab == False:
            return

        rightSleeveTab.click()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()


    def chooseLeftSleeveColorsIfAvailable(self, browser, newShirt):

        leftSleeveTab = generateProductMethods.findElement(self, browser, 'left sleeve')

        if leftSleeveTab == False:
            return

        leftSleeveTab.click()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

    def chooseColor(self, browser, colorName):
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

        printfulAutomation.waitForPageLoad()

    def chooseLeftLegColorIfAvailable(self, browser, newItem):

        leftLegTab = generateProductMethods.findElement(self, browser, 'left leg')

        if leftLegTab == False:
            return

        leftLegTab.click()

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseColor(self, browser, newItem.colorName + '_mirror')


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

    def submitProduct(self, browser, newItem):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        # navigationFunctionsObject.clickSubmitButton(browser)

        print('-----------')
        print('Created... \n', newItem.productStyle, newItem.productCategory, newItem.colorName, newItem.gender)
        print('-----------')

    def findElement(self, browser, name):
# Implement with javascript instead of xpath
        name = name.lower()

        try:
            browser.find_element_by_xpath("//*[translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = \"%s\"]" % name)
        except NoSuchElementException:
            return False

        return browser.find_element_by_xpath("//*[translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = \"%s\"]" % name)
