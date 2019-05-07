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

    sleevedShirtTypeList = [
        'Athletic T-Shirt',
        'Crew Neck T-Shirt',
        'Rash Guard',
        'V-Neck T-Shirt'
    ]

    sleevelessShirtTypeList = [
        'Tank Top',
        'Sublimation T-Shirt',
        'Sublimation Tank'
    ]

    for shirtType in sleevedShirtTypeList:
        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        color = 'Yellow-Orange-Red'

        newShirt = itemClasses.item(shirtType, 'shirt', color, 'Mens')

        productMethodsObject.createSleevedShirt(browser, newShirt)

    # for color in trianglifyColorList:
    #     navigationFunctionsObject.navigateToMensAllOverShirts(browser)

    #     waitForPageLoad()

    #     shirtType = 'Athletic T-Shirt'

    #     productMethodsObject.createSleevedShirt(browser, shirtType, color)



def waitForPageLoad():
    time.sleep(1)

if __name__ == "__main__":
    main()
