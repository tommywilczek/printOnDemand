class item():
    def __init__(self, productStyle, productCategory, colorName, hasBack, gender=None):
        self.productStyle = productStyle

        self.productType = productCategory

        self.colorName = colorName

        self.hasBack = hasBack

        self.gender = gender

class Shirt(item):
    def __init__(self, productStyle, productCategory, colorName, hasBack, hasSleeves, gender=None):
        item.__init__(self, productStyle, productCategory, colorName, hasBack, gender)
        self.hasSleeves = hasSleeves
