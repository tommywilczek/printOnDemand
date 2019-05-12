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

    for color in trianglifyColorList:

        ### Men's shirts

        # # sleeved

        createItemsFromItemTypeList(browser, mensSleevedShirtTypeList, 'shirt', color, 'Mens all-over shirts', 'Mens')

        # # sleeveless

        createItemsFromItemTypeList(browser, mensSleevelessShirtTypeList, 'shirt', color, 'Mens all-over shirts', 'Mens')


        # for productType in mensSleevelessShirtTypeList:

        #         navigationFunctionsObject.navigateToMensAllOverShirts(browser)

        #         waitForPageLoad()

        #         newItem = itemClasses.item(productType, 'shirt', color, True, gender='Mens')

        #         productMethodsObject.createNewProduct(browser, newItem)

        # ### Women's shirts

        # # sleeved

        createItemsFromItemTypeList(browser, womensSleevedShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')


        # for productType in womensSleevedShirtTypeList:

        #         navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        #         waitForPageLoad()

        #         newItem = itemClasses.item(productType, 'shirt', color, True, gender='Womens')

        #         productMethodsObject.createNewProduct(browser, newItem)


        # # sleeveless

        createItemsFromItemTypeList(browser, womensSleevelessShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')


        # navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createNewProduct(browser, 'shirt', womensSleevelessShirtTypeList, color, 'Womens')

        # # just front womens shirts

        # navigationFunctionsObject.navigateToWomensAllOverShirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createNewProduct(browser, 'shirt', womensOneSidedShirtTypeList, color, 'Womens')

        # ### Unisex sweatshirts

        # navigationFunctionsObject.navigateToSweatshirts(browser)

        # waitForPageLoad()

        # productMethodsObject.createNewProduct(browser, 'sweatshirt', sweatshirtTypeList, color, 'Unisex')

        # ### Mens Shorts

        # navigationFunctionsObject.navigateToMensShorts(browser)

        # waitForPageLoad()

        # productMethodsObject.createNewProduct(browser, 'shorts', mensShortsTypeList, color, 'Mens')

        # ### Mens Leggings

        # navigationFunctionsObject.navigateToMensLeggings(browser)

        # waitForPageLoad()

        # productMethodsObject.createNewProduct(browser, 'leggings', mensLeggingsTypeList, color, 'Mens')

        # ### Womens Leggings

        # navigationFunctionsObject.navigateToWomensLeggings(browser)

        # waitForPageLoad()

        # productMethodsObject.createNewProduct(browser, 'leggings', womensLeggingsTypeList, color, 'Womens')

        # ### Womens Shorts

        # navigationFunctionsObject.navigateToWomensShorts(browser)

        # waitForPageLoad()

        # ######### ATTENTION: STILL NEED TO MAKE THE OTHER TYPES OF womens SHORTS

        # productMethodsObject.createFrontItem(browser, 'shorts', womensShortsTypeList, color, 'Womens')



def createItemsFromItemTypeList(browser, itemTypeList, productCategory, color, navigateBackTo, gender=None):

        navigationFunctionsObject = navigationFunctions.NavigationFunctions()

        productMethodsObject = generateProductMethods.generateProductMethods()

        for itemType in itemTypeList:

                if navigateBackTo == 'Mens all-over shirts':
                        navigationFunctionsObject.navigateToMensAllOverShirts(browser)
                elif navigateBackTo == 'Womens all-over shirts':
                        navigationFunctionsObject.navigateToWomensAllOverShirts(browser)
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

womensShortsTypeList = itemTypeLists.womensShortsTypeList


# womensSleevedShirtTypeList


if __name__ == "__main__":
    main()
