from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import configparser

import itemClasses
import navigationFunctions
import generateProductMethods
import trianglifyColors

def main():

    browser = webdriver.Chrome('/Users/tommywilczek/Documents/Projects/chromedriver')

    navigationFunctionsObject = navigationFunctions.NavigationFunctions()

    productMethodsObject = generateProductMethods.generateProductMethods()

    navigationFunctionsObject.loginToPrintful(browser)

    waitForPageLoad()

    navigationFunctionsObject.goToChooseProduct(browser)

    waitForPageLoad()

    trianglifyColorList = trianglifyColors.trianglifyColorDict

    for color in trianglifyColorList:
        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllOverPrintMensAthleticTShirt(browser, color)



def waitForPageLoad():
    time.sleep(1)

if __name__ == "__main__":
    main()
