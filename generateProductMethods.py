from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import keywordLookup
import printfulAutomation
import navigationFunctions
import itemClasses

class generateProductMethods():

    def createSleevedShirt(self, browser, shirtType, colorName):
        # Prerequisite: navigateToMensAllOverShirts

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        newShirt = itemClasses.shirt(shirtType, 'shirt', colorName, 'Mens')

        allOverPrintMensAthleticTShirtButton = browser.find_elements_by_xpath("//*[contains(text(), '%s')]" % shirtType)[-1] #last one in the ist AKA theone in the modal

        allOverPrintMensAthleticTShirtButton.click()

        printfulAutomation.waitForPageLoad()

        whiteRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='white']")

        whiteRadioButton.send_keys(Keys.SPACE) # click radio button

        generateProductMethods.chooseColor(self, browser, newShirt.colorName)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseBackOfItemColor(self, browser, newShirt)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseRightSleeveColor(self, browser, newShirt)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseLeftSleeveColor(self, browser, newShirt)

        printfulAutomation.waitForPageLoad()

        navigationFunctionsObject.proceedToProductDescription(browser)

        printfulAutomation.waitForPageLoad()
        
        generateProductMethods.createProductDescription(self, browser, newShirt)

        navigationFunctionsObject.proceedToPricing(browser)

        printfulAutomation.waitForPageLoad()

        generateProductMethods.upchargeByPercentage(self, browser)

        submitItemButton = browser.find_element_by_xpath("//*[contains(text(), 'Submit to store')]")

        ########## For Testing
        print('Creating product of color:', colorName)
        navigationFunctionsObject.goToChooseProduct(browser)

        #########################
        # submitItemButton.click()
        printfulAutomation.waitForPageLoad()


    def chooseBackOfItemColor(self, browser, newShirt):
        backOfItemTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[2]/a/span')

        backOfItemTab.click()

        printfulAutomation.waitForPageLoad()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

    def chooseRightSleeveColor(self, browser, newShirt):
        rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[3]/a/span')

        rightSleeveTab.click()

        generateProductMethods.chooseColor(self, browser, newShirt.colorName + '_mirror')

    def chooseLeftSleeveColor(self, browser, newShirt):
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

    def generateProductDescription(self, browser, newShirt):
        if newShirt.gender == 'unisex':
            genderDescription = 'Mens Womens Unisex'
        elif newShirt.gender == None:
            genderDescription = ''
        else:
            genderDescription = newShirt.gender

        colorName = newShirt.colorName.replace('-', ' ')

        productKeywords = keywordLookup.keywordDict[newShirt.productType]

        return newShirt.colorName, ' ' , newShirt.productStyle, ' ' ,productKeywords, ' ', genderDescription 

    def upchargeByPercentage(self, browser, ):
        # Must be in 'pricing' stage of create product
        dollarOrPercentageDropdown = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/table/thead/tr[2]/td[4]/span[2]/select/option[1]') 

        dollarOrPercentageDropdown.click()

        numberToIncreaseField = browser.find_element_by_class_name('profit-amount')

        numberToIncreaseField.clear()

        numberToIncreaseField.send_keys('15')
