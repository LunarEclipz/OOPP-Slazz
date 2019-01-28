class Budget:

    def __init__(self, food_b, leisure_b, essen_b, others_b, food_e, leisure_e, essen_e, others_e):
        self.food_b = food_b
        self.leisure_b = leisure_b
        self.essen_b = essen_b
        self.others_b = others_b
        self.food_e = food_e
        self.leisure_e = leisure_e
        self.essen_e = essen_e
        self.others_e = others_e

    def get_foodb(self):
        return self.food_b
    
    def get_foode(self):
        return self.food_e
    
    def get_leisureb(self):
        return self.leisure_b
    
    def get_leisuree(self):
        return self.leisure_e

    def get_othersb(self):
        return self.food_b

    def get_otherse(self):
        return self.others_e

    def get_essenb(self):
        return self.essen_b

    def get_essene(self):
        return self.essen_e


class Default(Budget):

    def __init__(self, food_b=0.2, leisure_b=0.4, essen_b=0.3, others_b=0.1, food_e='', leisure_e='', essen_e='', others_e='', type='Default'):
        super().__init__(food_b, leisure_b, essen_b, others_b, food_e, leisure_e, essen_e, others_e)
        self.type = type

    def get_type(self):
        return self.type


class self_Settings(Budget):

    def __init__(self, food_b='', leisure_b='', essen_b='', others_b='', food_e='', leisure_e='', essen_e='', others_e='', type='Self Settings'):
        super().__init__(food_b, leisure_b, essen_b, others_b, food_e, leisure_e, essen_e, others_e)
        self.type = type

    def get_type(self):
        return self.type


