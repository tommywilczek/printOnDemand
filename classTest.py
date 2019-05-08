import itemClasses
from pprint import pprint

newItem = itemClasses.item("prodStyle", "prodType", "color", gender='Mens')

newShirt = itemClasses.Shirt("prodStyle", "prodType", "color", True, gender='Mens')

pprint(newShirt.__dict__, indent=2)