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

        self.clickAllColorsCheckboxIfAvailable(browser)

        self.chooseColor(browser, newItem.colorName) # first color

        self.chooseItemColorIfAvailable(browser, 'back', newItem.colorName, True)

        self.chooseItemColorIfAvailable(browser, 'right sleeve', newItem.colorName, True)

        self.chooseItemColorIfAvailable(browser, 'left sleeve', newItem.colorName, True)

        self.chooseItemColorIfAvailable(browser, 'left leg', newItem.colorName, True)

        self.chooseItemColorIfAvailable(browser, 'front waist', newItem.colorName)

        self.chooseItemColorIfAvailable(browser, 'back waist', newItem.colorName, True)

        self.chooseItemColorIfAvailable(browser, 'top', newItem.colorName)

        if newItem.productCategory == 'bag': # don't get confused with inside pocket radio btn
            self.chooseItemColorIfAvailable(browser, 'inside pocket', newItem.colorName)

        self.chooseItemColorIfAvailable(browser, 'top panel', newItem.colorName)

        self.chooseItemColorIfAvailable(browser, 'bottom panel', newItem.colorName)

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

    def clickAllColorsCheckboxIfAvailable(self, browser):

        checkboxValue = 'Select all colors'

        try:
            browser.find_element_by_xpath(".//span[text()='%s']" % checkboxValue)
        except NoSuchElementException:
            return 
        

        allColorsCheckbox = browser.find_element_by_xpath(".//span[text()='%s']" % checkboxValue)

        browser.execute_script("arguments[0].scrollIntoView();", allColorsCheckbox)

        allColorsCheckbox.click()

        printfulAutomation.waitForPageLoad()

    def chooseItemColorIfAvailable(self, browser, itemPiece, color, mirror=False):

        itemPieceTab = self.findElement(browser, itemPiece)

        if itemPieceTab == False:
            return

        browser.execute_script("arguments[0].scrollIntoView();", itemPieceTab)

        itemPieceTab.click()

        if mirror:
            color += '_mirror'

        self.chooseColor(browser, color)

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

    def createProductDescription(self, browser, newItem):
        productDescription = self.generateProductDescription(browser, newItem)

        productNameField = browser.find_element_by_class_name('form-control')

        productNameField.clear()

        productNameField.send_keys(productDescription)

        time.sleep(2)

        productNameField.send_keys(Keys.ENTER)

    def generateProductDescription(self, browser, newItem):
        if newItem.gender == 'Unisex':
            genderDescription = 'Mens Womens' # Usually says unisex in product style
        elif newItem.gender == None:
            genderDescription = ''
        else:
            genderDescription = newItem.gender

        colorName = newItem.colorName.replace('-', ' ')

        if newItem.productCategory == 'bag':
            keywordKey = newItem.productStyle
        else:
            keywordKey = newItem.productCategory

        if keywordLookup.keywordDict.get(keywordKey) is not None:
            productKeywords = keywordLookup.keywordDict[keywordKey]
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

        navigationFunctionsObject.clickSubmitButton(browser)

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
