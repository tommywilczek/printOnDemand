import itemClasses
from pprint import pprint

newItem = itemClasses.shirt("prodStyle", "prodType", "color")

pprint(newItem.__dict__, indent=2)