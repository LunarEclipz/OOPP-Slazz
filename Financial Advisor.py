class Finance:
    __department = ''
    __expenditure = ''
    __savings = ''

    def __init__(self, department, expenditure, savings):
        self.__department = department
        self.__expenditure = expenditure
        self.__savings = savings

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_expenditure(self):
        return self.__expenditure

    def set_expenditure(self, expenditure):
        self.__expenditure = expenditure

    def get_savings(self):
        return self.__savings

    def set_savings(self, savings):
        self.__savings = savings
