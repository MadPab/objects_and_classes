class Passport:
    pages = 20 # атрибут класса, принадлежит всем объектам класса

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        print('Added new passport') 

    def add_visa(self, visa_name):
        # hasattr - проверяет наличие атрибута у объекта
        if not hasattr(self, 'visas'):
            self.visas = [visa_name] # Атрибут экземплятра (объекта) класса для хранения списка названий виз
        else:
            self.visas.append(visa_name) # Добавление нового названия визы к существующему списку виз

    def print_all_visas(self):
        if not hasattr(self, 'visas'):
            print('No visas')
        else:
            print(f'List all visas: {", ".join(self.visas)}')

    def show_info(self):
        print(f'Name: {self.first_name}, Surname: {self.last_name}, Date od Birth: {self.date_of_birth}')

passport_1 = Passport('Oleg', 'Bulygin', '30.08.1991')
passport_1.show_info()

# passport_1.name = 'Oleg'
# passport_1.visas = ['visa_1', 'visa_2']
# passport_1.print_all_visas()
# passport_1.add_visa('visa_3')
# passport_1.print_all_visas()


# Как выглядит self изнутри. passport_1 передается в self
# Passport.print_all_visas(passport_1)

# peter = Passport()
# peter.name = 'Peter' # атрибут экземпляра (объекта) класса
# peter.last_name = 'Parker' # атрибут экземпляра (объекта) класса

