class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def create_citizen_from_human(self):
        return Citizen(self.name, self.age)


class Citizen(Human):
    country_name = 'Belarus'

    def __init__(self, name, age, country_name='Belarus'):
        super().__init__(name, age)

    @classmethod
    def change_country_name(cls, country_name):
        cls.country_name = country_name

    @staticmethod
    def cell_average_age_of_given_citizens(list_of_citizens: list) -> int:
        average = 0
        for item in list_of_citizens:
            average += item.age
        return average / len(list_of_citizens)