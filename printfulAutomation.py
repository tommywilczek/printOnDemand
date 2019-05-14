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

        createItemsFromItemTypeList(browser, mensSleevedShirtTypeList, 'shirt', color, 'Mens all-over shirts', 'Mens')

        # # sleeveless

        createItemsFromItemTypeList(browser, mensSleevelessShirtTypeList, 'shirt', color, 'Mens all-over shirts', 'Mens')

        ### Women's shirts

        # sleeved

        createItemsFromItemTypeList(browser, womensSleevedShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')

        # sleeveless

        createItemsFromItemTypeList(browser, womensSleevelessShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')

        # just front womens shirts

        createItemsFromItemTypeList(browser, womensOneSidedShirtTypeList, 'shirt', color, 'Womens all-over shirts', 'Womens')

        ### Unisex sweatshirts

        createItemsFromItemTypeList(browser, sweatshirtTypeList, 'sweatshirt', color, 'Sweatshirts', 'Unisex')

        ### Mens Shorts

        createItemsFromItemTypeList(browser, mensShortsTypeList, 'shorts', color, 'Mens shorts', 'Mens')

        ### Mens Leggings

        createItemsFromItemTypeList(browser, mensLeggingsTypeList, 'leggings', color, 'Mens leggings', 'Mens')

        ### Womens Leggings

        createItemsFromItemTypeList(browser, womensLeggingsTypeList, 'leggings', color, 'Womens leggings', 'Womens')

        # Womens Swimwear

        createItemsFromItemTypeList(browser, womensSwimwearTypeList, 'swimwear', color, 'Womens swimwear', 'Womens')

        # Kids Shirts

        createItemsFromItemTypeList(browser, kidsShirtsTypeList, 'shirt', color, 'Kids all-over shirts', 'Kids')

        # Kids Leggings

        createItemsFromItemTypeList(browser, kidsLeggingsTypeList, 'leggings', color, 'Kids leggings', 'Kids')

        # Kids swimwear

        createItemsFromItemTypeList(browser, kidsSwimwearTypeList, 'swimwear', color, 'Kids swimwear', 'Kids')

        # Bags

        createItemsFromItemTypeList(browser, bagsTypeList, 'bag', color, 'Bags')

        # Flip Flops

        # createItemsFromItemTypeList(browser, bagsTypeList, 'Flip-Flops', color, 'Flip-Flops', 'Unisex')

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
                elif navigateBackTo == 'Womens swimwear':
                        navigationFunctionsObject.navigateToWomensSwimwear(browser)
                elif navigateBackTo == 'Kids all-over shirts':
                        navigationFunctionsObject.navigateToKidsAllOverShirts(browser)
                elif navigateBackTo == 'Kids leggings':
                        navigationFunctionsObject.navigateToKidsLeggings(browser)
                elif navigateBackTo == 'Kids swimwear':
                        navigationFunctionsObject.navigateToKidsSwimwear(browser)
                elif navigateBackTo == 'Bags':
                        navigationFunctionsObject.navigateToBags(browser)
                elif navigateBackTo == 'Flip-Flops':
                        navigationFunctionsObject.navigateToFlipFlops(browser)

                waitForPageLoad()

                newItem = itemClasses.item(itemType, productCategory, color, gender)

                productMethodsObject.createNewProduct(browser, newItem)



def waitForPageLoad():
    time.sleep(2)


mensSleevedShirtTypeList = itemTypeLists.mensSleevedShirtTypeList
mensSleevelessShirtTypeList = itemTypeLists.mensSleevelessShirtTypeList

womensSleevedShirtTypeList = itemTypeLists.womensSleevedShirtTypeList
womensSleevelessShirtTypeList = itemTypeLists.womensSleevelessShirtTypeList
womensOneSidedShirtTypeList = itemTypeLists.womensOneSidedShirtTypeList

sweatshirtTypeList = itemTypeLists.sweatshirtTypeList

mensShortsTypeList = itemTypeLists.mensShortsTypeList

mensLeggingsTypeList = itemTypeLists.mensLeggingsTypeList

womensLeggingsTypeList = itemTypeLists.womensLeggingsTypeList

womensSwimwearTypeList = itemTypeLists.womensSwimwearTypeList

kidsShirtsTypeList = itemTypeLists.kidsShirtsTypeList

kidsLeggingsTypeList = itemTypeLists.kidsLeggingsTypeList

kidsSwimwearTypeList = itemTypeLists.kidsSwimwearTypeList

bagsTypeList = itemTypeLists.bagsTypeList

flipFlopsTypeList = itemTypeLists.flipFlopsTypeList

if __name__ == "__main__":
    beginningTime = time.time()
    main()
    endTime = time.time()

    total = endTime - beginningTime

    print(total)
