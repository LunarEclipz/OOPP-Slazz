class Activity:

    def __init__(self):
        self.name = ''
        self.image = ''
        self.hours = ''
        self.pricing = ''
        
    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def get_hours(self):
        return self.hours

    def get_pricing(self):
        return self.pricing

    def set_name(self, name):
        self.name = name

    def set_image(self, image):
        self.image = image

    def set_hours(self, hours):
        self.hours = hours

    def set_pricing(self, pricing):
        self.pricing = pricing


