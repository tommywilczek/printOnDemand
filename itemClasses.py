class item():
    def __init__(self, productStyle, productCategory, colorName, gender=None):
        self.productStyle = productStyle

        self.productType = productCategory

        self.colorName = colorName

        self.gender = gender

class Shirt(item):
    def __init__(self, productStyle, productCategory, colorName, hasSleeves, gender=None):
        item.__init__(self, productStyle, productCategory, colorName, gender)
        self.hasSleeves = hasSleeves
