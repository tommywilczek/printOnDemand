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

    womensSleevedShirtTypeList = itemTypeLists.womensSleevedShirtTypeList
    womensSleevelessShirtTypeList = itemTypeLists.womensSleevelessShirtTypeList
    wpmensOneSidedShirtTypeList = itemTypeLists.womensOneSidedShirtTypeList


    # womensSleevedShirtTypeList

    for color in trianglifyColorList:

        # Men's shirts

        ######################
        # Todo: generalize create sleeve and sleeveless shirts into 
        #       sleeve shirts and front/back items
        #       then create a createFrontItem for rest of women's shirts and to be used for more

        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllSleevedShirts(browser, mensSleevedShirtTypeList, color, True, 'Mens')

        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllSleevelessShirts(browser, mensSleevelessShirtTypeList, color, True, 'Mens')

        # Women's shirts

        navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllSleevedShirts(browser, womensSleevedShirtTypeList, color, True, 'Womens')

        navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createAllSleevelessShirts(browser, womensSleevelessShirtTypeList, color, True, 'Womens')





def waitForPageLoad():
    time.sleep(1)

if __name__ == "__main__":
    main()
