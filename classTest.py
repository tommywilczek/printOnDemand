import itemClasses
from pprint import pprint

newItem = itemClasses.item("prodStyle", "prodType", "color", True, gender='Mens')

# newShirt = itemClasses.Shirt("prodStyle", "prodType", "color", True, gender='Mens')

pprint(newItem.__dict__, indent=2)