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

    def createNewProduct(self, browser, newItem):
        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        navigationFunctionsObject.navigateToCreateProductStyle(browser, newItem.productStyle)

        self.clickColorRadioButtonIfAvailable(browser, 'white')

        self.clickPocketRadioButtonIfAvailable(browser)

        self.chooseColor(browser, newItem.colorName)

        self.chooseBackOfItemColorIfAvailable(browser, newItem)

        self.chooseRightSleeveColorIfAvailable(browser, newItem)

        self.chooseLeftSleeveColorIfAvailable(browser, newItem)

        self.chooseLeftLegColorIfAvailable(browser, newItem)

        self.chooseFrontWaistColorIfAvailable(browser, newItem)

        self.chooseBackWaistColorsIfAvailable(browser, newItem)

        navigationFunctionsObject.proceedToProductDescription(browser)
        
        self.createProductDescription(browser, newItem)

        navigationFunctionsObject.proceedToPricing(browser)

        self.upchargeByPercentage(browser)

        self.submitProduct(browser, newItem)

    def clickColorRadioButtonIfAvailable(self, browser, color):

        try:
            browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % color)
        except NoSuchElementException:
            return 

        whiteRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % color)

        whiteRadioButton.send_keys(Keys.SPACE) # click radio button

    def clickPocketRadioButtonIfAvailable(self, browser):

        radioButtonValue = '0'

        try:
            browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % radioButtonValue)
        except NoSuchElementException:
            return 

        hasPocketRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='%s']" % radioButtonValue)

        hasPocketRadioButton.send_keys(Keys.SPACE) # click radio button


    def chooseBackOfItemColorIfAvailable(self, browser, newShirt):
        
        backOfItemTab = self.findElement(browser, 'back')

        if backOfItemTab == False:
            return

        backOfItemTab.click()

        printfulAutomation.waitForPageLoad()

        self.chooseColor(browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

    def chooseRightSleeveColorIfAvailable(self, browser, newShirt):

        rightSleeveTab = self.findElement(browser, 'right sleeve')

        if rightSleeveTab == False:
            return

        rightSleeveTab.click()

        self.chooseColor(browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()


    def chooseLeftSleeveColorIfAvailable(self, browser, newShirt):

        leftSleeveTab = self.findElement(browser, 'left sleeve')

        if leftSleeveTab == False:
            return

        leftSleeveTab.click()

        self.chooseColor(browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

    def chooseLeftLegColorIfAvailable(self, browser, newShirt):

        leftLegTab = self.findElement(browser, 'left leg')

        if leftLegTab == False:
            return

        leftLegTab.click()

        self.chooseColor(browser, newShirt.colorName + '_mirror')

        printfulAutomation.waitForPageLoad()

    def chooseFrontWaistColorIfAvailable(self, browser, newShirt):

        frontWaistTab = self.findElement(browser, 'front waist')

        if frontWaistTab == False:
            return

        frontWaistTab.click()

        self.chooseColor(browser, newShirt.colorName)

        printfulAutomation.waitForPageLoad()

    def chooseBackWaistColorsIfAvailable(self, browser, newShirt):

        backWaistTab = self.findElement(browser, 'back waist')

        if backWaistTab == False:
            return

        backWaistTab.click()

        self.chooseColor(browser, newShirt.colorName + '_mirror')

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

    def createProductDescription(self, browser, newShirt):
        productDescription = self.generateProductDescription(browser, newShirt)

        productNameField = browser.find_element_by_class_name('form-control')

        productNameField.clear()

        productNameField.send_keys(productDescription)

        productNameField.send_keys(Keys.ENTER)

    def generateProductDescription(self, browser, newItem):
        if newItem.gender == 'Unisex':
            genderDescription = 'Mens Womens' # Usually says unisex in product style
        if newItem.gender == 'Youth':
            genderDescription = 'Teen'
        elif newItem.gender == None:
            genderDescription = ''
        else:
            genderDescription = newItem.gender

        colorName = newItem.colorName.replace('-', ' ')

        if keywordLookup.keywordDict.get(newItem.productCategory) is not None:
            productKeywords = keywordLookup.keywordDict[newItem.productCategory]
        else:
            productKeywords = ''

        companyName = 'Güd Vibes'

        return companyName, ' ', colorName, ' ' , newItem.productStyle, ' ' ,productKeywords, ' ', genderDescription 

    def upchargeByPercentage(self, browser, ):
        # Must be in 'pricing' stage of create product
        dollarOrPercentageDropdown = browser.find_element_by_xpath('.//option[ @value=\"%\"]') 

        dollarOrPercentageDropdown.click()

        numberToIncreaseField = browser.find_element_by_class_name('profit-amount')

        numberToIncreaseField.clear()

        upchargePercentage = '15'

        numberToIncreaseField.send_keys(upchargePercentage)

    def submitProduct(self, browser, newItem):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        # navigationFunctionsObject.clickSubmitButton(browser)

        print('-----------')
        print('Created... \n', newItem.productStyle, newItem.productCategory, newItem.colorName, newItem.gender)
        print('-----------')

    def findElement(self, browser, name):

        name = name.lower()

        try:
            browser.find_element_by_xpath("//*[translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = \"%s\"]" % name)
        except NoSuchElementException:
            return False

        return browser.find_element_by_xpath("//*[translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = \"%s\"]" % name)
