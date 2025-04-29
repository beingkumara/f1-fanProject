import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from FakeData.telemetryData import FakeData
import KafkaProducerClient.KafkaProducerClient as KafkaProducerClient

def main():
    fakeData = FakeData()
    fakeTelemetryData = fakeData.generate_telemetry_data(10)  # Generate 10 rows of fake telemetry data
    producer = KafkaProducerClient(bootstrap_servers='localhost:9092')
                             
    print(fakeTelemetryData)
    for data in fakeTelemetryData:
        # Using the producer's send method directly since it's available through the KafkaProducer instance
        producer.producer.send('telemetry_topic', value=data)
        print(f"Sent data: {data}")
        producer.producer.flush()
    producer.close()
if __name__ == "__main__":  
    main()



