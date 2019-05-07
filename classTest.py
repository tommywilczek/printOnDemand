import itemClasses
from pprint import pprint

newItem = itemClasses.item("prodStyle", "prodType", "color")

pprint(newItem.__dict__, indent=2)