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
    womensOneSidedShirtTypeList = itemTypeLists.womensOneSidedShirtTypeList

    sweatshirtTypeList = itemTypeLists.sweatshirtTypeList

    mensShortsTypeList = itemTypeLists.mensShortsTypeList

    mensLeggingsTypeList = itemTypeLists.mensLeggingsTypeList

    womensLeggingsTypeList = itemTypeLists.womensLeggingsTypeList

    womensShortsTypeList = itemTypeLists.womensShortsTypeList


    # womensSleevedShirtTypeList

    for color in trianglifyColorList:

        ### Men's shirts

        # sleeved

        navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        waitForPageLoad()

        productMethodsObject.createNewProduct(browser, 'shirt', mensSleevedShirtTypeList, color, 'Mens')

        # # sleeveless

        # navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createFrontBackItem(browser, 'shirt',mensSleevelessShirtTypeList, color, 'Mens')

        # #### Women's shirts

        # # sleeved

        # navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createAllSleevedShirts(browser, womensSleevedShirtTypeList, color, 'Womens')

        # # sleeveless

        # navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createFrontBackItem(browser, 'shirt', womensSleevelessShirtTypeList, color, 'Womens')

        # # just front womens shirts

        # navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createFrontItem(browser, 'shirt', womensOneSidedShirtTypeList, color, 'Womens')

        # ### Unisex Sweaters

        # navigationFunctionsObject.navigateToSweaters(browser)

        # waitForPageLoad()

        # productMethodsObject.createAllSleevedShirts(browser, sweatshirtTypeList, color, 'Unisex')

        # ### Mens Shorts

        # navigationFunctionsObject.navigateToMensShorts(browser)

        # waitForPageLoad()

        # productMethodsObject.createFrontBackItem(browser, 'shorts', mensShortsTypeList, color, 'Mens')

        # ### Mens Leggings

        # navigationFunctionsObject.navigateToMensLeggings(browser)

        # waitForPageLoad()

        # productMethodsObject.createFrontItem(browser, 'leggings', mensLeggingsTypeList, color, 'Mens')


        ### Womens Leggings

        # ### Womens Shorts

        # navigationFunctionsObject.navigateToWomensShorts(browser)

        # waitForPageLoad()

        # ######### ATTENTION: STILL NEED TO MAKE THE OTHER TYPES OF womens SHORTS

        # productMethodsObject.createFrontItem(browser, 'shorts', womensShortsTypeList, color, 'Womens')






def waitForPageLoad():
    time.sleep(1)

if __name__ == "__main__":
    main()
