class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    

    def read_odometer(self): 
        """Exibe uma frase que mostra a milhagem do carro.""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    

    def update_odometer(self, mileage): 
        #"""Define o valor de leitura do hodômetro com o valor especificado.""" 
        """Define o valor de leitura do hodômetro com o valor especificado Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles): 
        """Soma a quantidade especificada ao valor de leitura do hodômetro.""" 
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
    
    def fill_gas_tank():
        """Exibe uma mensagem informando que o tanque foi cheio de gasolina.""" 
        print("Full gas tank!")
            


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(7)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year): 
        """Inicializa os atributos da classe-pai. Em seguida, inicializa
        os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year)
        #self.battery_size = 70 :: esse atributo foi remodelado
        # e foi criada uma class Battery()
        self.battery = Battery()

    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    #SOBRESCRITA DE MÉTODOS
    def fill_gas_tank(): 
        """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't need a gas tank!")


class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    
    def get_range(self): 
        """Exibe uma frase sobre a distância que o carro é capaz de 
        percorrer com essa bateria."""
        if self.battery_size == 70: 
            range = 240 
        elif self.battery_size == 85: 
            range = 270 
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge." 
        print(message)


print("\n-.-.-.-.-.-.-.-.-.-.-.-.-")
my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()