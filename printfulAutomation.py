from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import configparser

import itemClasses
import navigationFunctions
import generateProductMethods



def main():

    browser = webdriver.Chrome('/Users/tommywilczek/Documents/Projects/chromedriver')

    navigationFunctionsObject = navigationFunctions.NavigationFunctions()

    productMethodsObject = generateProductMethods.generateProductMethods()

    navigationFunctionsObject.loginToPrintful(browser)

    waitForPageLoad()

    navigationFunctionsObject.goToChooseProduct(browser)

    waitForPageLoad()

    navigationFunctionsObject.navigateToMensAllOverShirts(browser)

    waitForPageLoad()

    colorName = 'Yellow-Orange-Red'

    productMethodsObject.createAllOverPrintMensAthleticTShirt(browser, colorName)



def waitForPageLoad():
    time.sleep(1)

if __name__ == "__main__":
    main()
