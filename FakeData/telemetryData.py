import pandas as pd  # type: ignore
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# List of F1 drivers
drivers = [
    "Lewis Hamilton", "Max Verstappen", "Charles Leclerc", 
    "Sebastian Vettel", "Fernando Alonso", "Lando Norris", 
    "Daniel Ricciardo", "George Russell", "Carlos Sainz", 
    "Sergio Perez"
]

class FakeData:
    def __init__(self):
        pass
    
    # Generate fake telemetry data
    def generate_telemetry_data(self, num_rows):
        data = []
        for _ in range(num_rows):
            data.append({
                "timestamp": fake.date_time_this_year().isoformat(),
                "driver": random.choice(drivers),
                "car_number": random.randint(1, 20),
                "speed_kph": round(random.uniform(100, 350), 2),
                "engine_rpm": random.randint(8000, 15000),
                "gear": random.randint(1, 8),
                "throttle": round(random.uniform(0, 100), 2),
                "brake": round(random.uniform(0, 100), 2),
                "steering_angle": round(random.uniform(-90, 90), 2),
                "lap_distance": round(random.uniform(0, 5000), 2),
            })
        return data
