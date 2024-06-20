class Automobile():
    def _init_(self, make, model, vin, engine_size, owner, year):
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year



automobile_generator.py
import automobile

def main():
    #create automobile objects
    auto1 = automobile.Automobile("Ford", "Focus", "1234", 2.2, "Alice", 2013)
    auto2 = automobile.Automobile("Honda", "Accord", "23456", 3.0, "Bob", 2017)

    print(f"{auto1.make} {auto1.model}: {auto1.year} ")

main()
