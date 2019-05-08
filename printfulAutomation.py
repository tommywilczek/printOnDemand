from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import configparser
from pprint import pprint

import itemClasses
import itemTypeLists
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

    mensSleevedShirtTypeList = itemTypeLists.mensSleevedShirtTypeList
    mensSleevelessShirtTypeList = itemTypeLists.mensSleevelessShirtTypeList

    for color in trianglifyColorList:
        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllSleevedShirts(browser, mensSleevedShirtTypeList, color, 'Mens')

        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllSleevelessShirts(browser, mensSleevelessShirtTypeList, color, 'Mens')




def waitForPageLoad():
    time.sleep(1)

if __name__ == "__main__":
    main()
