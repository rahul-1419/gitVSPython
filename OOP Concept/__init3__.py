class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.started = False

    def start_engine(self):
        if not self.started:
            self.started = True
            print(f'{self.brand} {self.model} engine started.')
        else:
            print("Engine is already running.")

    def info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")

    def stop_engine(self):
        if self.started:
            self.started = False
            print(f'{self.brand} {self.model} engine stopped.')
        else:
            print('Engine is already stopped.')

car1 = car("Toyota", "Corolla", 2020)

car1.start_engine()
car1.stop_engine()