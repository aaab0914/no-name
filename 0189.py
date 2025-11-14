class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"{self.brand} {self.model} engine started")
        
    def accelerate(self, increment):
        if self.is_running:
            self.speed += increment
            print(f"Speed increased to {self.speed} km/h")
        else:
            print("Start the engine first!")
            
    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model},"
f"Speed: {self.speed} km/h")

car1 = Car("Toyota", "Camry", 2023)
car1.display_info()
car1.start_engine()
car1.accelerate(30)
    
        