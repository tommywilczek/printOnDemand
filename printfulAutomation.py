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

    createAllOverPrintMensAthleticTShirt()

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

def createAllOverPrintMensAthleticTShirt():
    # Prerequisite: navigateToMensAllOverShirts
    allOverPrintMensAthleticTShirtButton = browser.find_element_by_xpath("//*[contains(text(), 'Athletic T-Shirt')]")

    allOverPrintMensAthleticTShirtButton.click()

    waitForPageLoad()

    modal = browser.find_element_by_xpath('//*[@class="modal-body"]')


    # modal.send_keys(Keys.END)

    # designTab = browser.find_element_by_xpath("//*[contains(text(), 'Upload file')]")

    # designTab.click()

    whiteRadioButton = browser.find_element_by_xpath(".//input[@type='radio' and @value='white']")

    whiteRadioButton.send_keys(Keys.SPACE) # click radio button

    uploadFileButton = browser.find_element_by_xpath("//*[contains(text(), 'Upload file')]")

    uploadFileButton.click()

def waitForPageLoad():
    time.sleep(1)

main()