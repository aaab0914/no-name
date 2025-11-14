class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):  # 修正：incrment → increment
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery:  # 修正：battery → Battery (类名应该大写)
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")  # 修正：batery → battery

    def get_range(self):
        """Print a statement about the range this battery provides."""  # 修正：battert → battery
        if self.battery_size == 40:  # 修正：==40 → == 40
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 200

        print(f"This car can go about {range} miles on a full charge.")
        return range
    
    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it's not already."""  # 修正：the 65 → 65
        if self.battery_size < 65:
            old_size = self.battery_size
            self.battery_size = 65
            print(f"Battery upgraded from {old_size}-kWh to {self.battery_size}-kWh.")  # 修正：upgradeed → upgraded, form → from
        else:
            print(f"Battery is already {self.battery_size}-kWh, no upgrade needed.")  # 修正：alredy → already

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""  # 修正：Repeesent → Represent

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # Create a Battery instance


# Test the battery upgrade feature
print("Electric Car Battery Upgrade Demonstration")
print("=" * 40)

# Create an electric car with default battery size
my_tesla = ElectricCar('tesla', 'model s', 2024)

print(f"Vehicle: {my_tesla.get_descriptive_name()}")
my_tesla.battery.describe_battery()

print("\nRange before upgrade:")
range_before = my_tesla.battery.get_range()

print("\nPerforming battery upgrade...")
my_tesla.battery.upgrade_battery()

print("\nBattery status after upgrade:")
my_tesla.battery.describe_battery()

print("\nRange after upgrade:")
range_after = my_tesla.battery.get_range()

print(f"\nRange increased by: {range_after - range_before} miles")
