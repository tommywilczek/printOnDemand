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

    navigationFunctionsObject.loginToPrintful(browser)

    waitForPageLoad()

    trianglifyColorList = trianglifyColors.trianglifyColorDict

    for color in trianglifyColorList:

        ### Men's shirts

        # # sleeved

        # createItemsFromItemTypeList(browser, mensSleevedShirtTypeList, 'shirt', color, 'Mens all-over shirts', 'Mens')

        # # sleeveless

        # createItemsFromItemTypeList(browser, mensSleevelessShirtTypeList, 'shirt', color, 'Mens all-over shirts', 'Mens')

        # ### Women's shirts

        # # sleeved

        # createItemsFromItemTypeList(browser, womensSleevedShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')

        # # sleeveless

        # createItemsFromItemTypeList(browser, womensSleevelessShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')

        # # just front womens shirts

        # createItemsFromItemTypeList(browser, womensOneSidedShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')

        # # ### Unisex sweatshirts

        # createItemsFromItemTypeList(browser, sweatshirtTypeList, 'sweatshirt', color, 'Sweatshirts', 'Unisex')

        # ### Mens Shorts

        # createItemsFromItemTypeList(browser, mensShortsTypeList, 'shorts', color, 'Mens shorts', 'Mens')

        # ### Mens Leggings

        # createItemsFromItemTypeList(browser, mensLeggingsTypeList, 'leggings', color, 'Mens leggings', 'Mens')

        # ### Womens Leggings

        createItemsFromItemTypeList(browser, womensLeggingsTypeList, 'leggings', color, 'Womens leggings', 'Womens')

def createItemsFromItemTypeList(browser, itemTypeList, productCategory, color, navigateBackTo, gender=None):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        productMethodsObject = generateProductMethods.generateProductMethods()

        for itemType in itemTypeList:

                navigationFunctionsObject.goToChooseProduct(browser)
        
                waitForPageLoad()

                if navigateBackTo == 'Mens all-over shirts':
                        navigationFunctionsObject.navigateToMensAllOverShirts(browser)
                elif navigateBackTo == 'Womens all-over shirts':
                        navigationFunctionsObject.navigateToWomensAllOverShirts(browser) 
                elif navigateBackTo == 'Sweatshirts':
                        navigationFunctionsObject.navigateToSweatshirts(browser)
                elif navigateBackTo == 'Mens shorts':
                        navigationFunctionsObject.navigateToMensShorts(browser)
                elif navigateBackTo == 'Mens leggings':
                        navigationFunctionsObject.navigateToMensLeggings(browser)
                elif navigateBackTo == 'Womens leggings':
                        navigationFunctionsObject.navigateToWomensLeggings(browser)
                # Accessories, Home, etc.

                waitForPageLoad()

                newItem = itemClasses.item(itemType, productCategory, color, gender)

                productMethodsObject.createNewProduct(browser, newItem)



def waitForPageLoad():
    time.sleep(1)


mensSleevedShirtTypeList = itemTypeLists.mensSleevedShirtTypeList
mensSleevelessShirtTypeList = itemTypeLists.mensSleevelessShirtTypeList

womensSleevedShirtTypeList = itemTypeLists.womensSleevedShirtTypeList
womensSleevelessShirtTypeList = itemTypeLists.womensSleevelessShirtTypeList
womensOneSidedShirtTypeList = itemTypeLists.womensOneSidedShirtTypeList

sweatshirtTypeList = itemTypeLists.sweatshirtTypeList

mensShortsTypeList = itemTypeLists.mensShortsTypeList

mensLeggingsTypeList = itemTypeLists.mensLeggingsTypeList

womensLeggingsTypeList = itemTypeLists.womensLeggingsTypeList


if __name__ == "__main__":
    main()
