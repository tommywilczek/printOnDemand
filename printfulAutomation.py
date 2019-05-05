from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import configparser

parser = configparser.ConfigParser()

parser.read('config.ini')

printfulPassword = parser.get('passwords', 'printfulPassword')

browser = webdriver.Chrome('/Users/tommywilczek/Documents/Projects/chromedriver')

def main():

    loginToPrintful(printfulPassword)

    waitForPageLoad()

    goToChooseProduct()

    waitForPageLoad()

    navigateToMensAllOverShirts()

    waitForPageLoad()

    colorName = 'Yellow-Orange-Red'

    createAllOverPrintMensAthleticTShirt(colorName)

def loginToPrintful(printfulPassword):
    browser.get("https://www.printful.com/auth/login")

    emailField = browser.find_element_by_id("customer-email")

    passwordField = browser.find_element_by_id("customer-password")

    emailField.send_keys("tommywilczek@gmail.com")

    passwordField.send_keys(printfulPassword, Keys.ENTER)

def goToChooseProduct():
    patternPopStoreId = '1354143'
    
    browser.get("https://www.printful.com/dashboard/sync?store=" + patternPopStoreId)
    
    waitForPageLoad()

    addProductButton = browser.find_element_by_xpath("//*[text()='Add product']")

    addProductButton.click()

def navigateToMensAllOverShirts():
    # Prerequisite: goToChooseProduct
    mensClothingButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[1]')

    mensClothingButton.click()

    allOverShirtsButton = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div/a[5]')

    allOverShirtsButton.click()

def createAllOverPrintMensAthleticTShirt(colorName):
    # Prerequisite: navigateToMensAllOverShirts
    allOverPrintMensAthleticTShirtButton = browser.find_element_by_xpath("//*[contains(text(), 'Athletic T-Shirt')]")

    allOverPrintMensAthleticTShirtButton.click()

    waitForPageLoad()

    whiteRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='white']")

    whiteRadioButton.send_keys(Keys.SPACE) # click radio button

    chooseColor(colorName)

    waitForPageLoad()

    chooseBackOfItemColor(colorName)

    waitForPageLoad()

    chooseRightSleeveColor(colorName)

    waitForPageLoad()

    chooseLeftSleeveColor(colorName)

    waitForPageLoad()

    makeProductDescription(colorName)



def chooseBackOfItemColor(colorName):
    backOfItemTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[2]/a/span')

    backOfItemTab.click()

    waitForPageLoad()

    chooseColor(colorName + '_mirror')

def chooseRightSleeveColor(colorName):
    rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[3]/a/span')

    rightSleeveTab.click()

    chooseColor(colorName + '_mirror')

def chooseLeftSleeveColor(colorName):
    rightSleeveTab = browser.find_element_by_xpath('//*[@id="modal-1"]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/ul/div/li[4]/a/span')

    rightSleeveTab.click()

    chooseColor(colorName + '_mirror')


def chooseColor(colorName):
    uploadFileButton = browser.find_element_by_xpath("//*[contains(text(), 'Upload file')]")

    uploadFileButton.click()

    waitForPageLoad()

    colorSearch = browser.find_element_by_xpath("//*[//*[contains(@id, 'search')]]")

    colorSearch.send_keys(colorName)

    colorSearch.send_keys(Keys.ENTER)

    waitForPageLoad()

    frontColorChooserButton = browser.find_element_by_xpath('//*[@title="%s.png"]' % colorName)

    frontColorChooserButton.click()

def makeProductDescription(colorName):
    proceedToMockupsButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to mockups')]")

    proceedToMockupsButton.click()

    proceedToDescriptionButton = browser.find_element_by_xpath("//*[contains(text(), 'Proceed to description')]")

    proceedToDescriptionButton.click()

    lookupProductKeywords('tshirt')

    productNameField = browser.find_element_by_class_name('form-control')

    productNameField.send_keys('HELLO')

def lookupProductKeywords(productType):
    #todo: mens/womens/unisex? perhaps pass in a value with default type of none

def waitForPageLoad():
    time.sleep(1)

main()