class Country:

    avg_populatn = 210000

    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code

    def abv(self, country_name):
        return country_name[:2]

    @classmethod
    def is_densly_populated(cls, population):
        if population > cls.avg_populatn:
            return True
        return False

    @staticmethod
    def world_avg_population(*args):
        return sum(args) / len(args)

    @staticmethod
    def validate_country_name(country_name):
        if type(country_name) != str:
            raise ValueError("Country name should be type string")
        return True

    @staticmethod
    def validate_country_code(country_code):
        if type(country_code) != str:
            raise ValueError("Country code should be type string")
        if len(country_code) != 3:
            raise ValueError("Country code should be exactly 3 characters")
        return True

    @property
    def country(self):
        return f'{self._country_name} ({self._country_code})'

    @property
    def country_name(self):
        print('Getting country name..')
        return self._country_name

    @country_name.setter
    def country_name(self, value):
        if Country.validate_country_name(value):
            print(f'Country name set to - [{value}]')
            self._country_name = value

    @country_name.deleter
    def country_name(self):
        print(f'Country name [{self._country_name}] is deleted')
        self._country_name = None

    @property
    def country_code(self):
        print('Getting country code..')
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        if Country.validate_country_code(value):
            print(f'Country code set to - [{value}]')
            self._country_code = value

    @country_code.deleter
    def country_code(self):
        print(f'Country code [{self._country_code}] is deleted')
        self._country_code = None


country = Country("India", "IND")

print()
print(country.country_code)
print(country.country_name)
print(country.country)


print()
del country.country_name
del country.country_code


print()
country.country_name = "Russia"
country.country_code = "RSA"

print()
print(Country.is_densly_populated(3700))
print(Country.is_densly_populated(70000))


print()
print(Country.world_avg_population(1651, 765, 3770, 11500, 9876))