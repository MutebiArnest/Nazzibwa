class Vehicle:
    def __init__(self, registration_number, price_per_day):
        self.registration_number = registration_number
        self.price_per_day = price_per_day

    def calculate_rental_cost(self, days):
        return self.price_per_day * days
    
class Car(Vehicle):
    def __init__(self, registration_number, price_per_day, num_seats):
        super().__init__(registration_number, price_per_day)
        self.num_seats = num_seats

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        if days > 7:
            return base_cost * 0.9
        return base_cost

class Motorcycle(Vehicle):
    def __init__(self, registration_number, price_per_day, engine_capacity):
        super().__init__(registration_number, price_per_day)
        self.engine_capacity = engine_capacity

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        if days > 5:
            return base_cost * 0.95
        return base_cost
    
subaru = Car("SUB123", 50, 5)
honda = Motorcycle("HON456", 30, 600)   

subaru_rental_cost = subaru.calculate_rental_cost(10) 
honda_rental_cost = honda.calculate_rental_cost(6) 