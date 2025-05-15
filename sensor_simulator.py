import random
import time
import json
from datetime import datetime
import os

class IoTSimulator:
    def __init__(self, config_file="iot_simulator/config.json"):
        with open(config_file) as f:
            self.config = json.load(f)
        
        self.devices = [f"sensor_{i}" for i in range(1, self.config["num_devices"]+1)]
        
    def generate_data(self):
        try:
            while True:
                for device in self.devices:
                    data = {
                        "device_id": device,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "temperature": round(random.uniform(
                            self.config["normal_ranges"]["temperature"]["min"],
                            self.config["normal_ranges"]["temperature"]["max"]
                        ), 1),
                        "humidity": round(random.uniform(
                            self.config["normal_ranges"]["humidity"]["min"],
                            self.config["normal_ranges"]["humidity"]["max"]
                        ), 1),
                        "status": "normal"
                    }
                    
                    if random.random() < self.config["anomaly_settings"]["probability"]:
                        data["temperature"] = round(random.uniform(
                            self.config["anomaly_settings"]["temperature_range"]["min"],
                            self.config["anomaly_settings"]["temperature_range"]["max"]
                        ), 1)
                        data["status"] = "ANOMALY"
                        
                    print(json.dumps(data))
                    time.sleep(self.config["update_interval_sec"])
                    
        except KeyboardInterrupt:
            print("\nSimulator stopped by user")

if __name__ == "__main__":
    print("Starting configurable IoT Simulator...")
    simulator = IoTSimulator()
    simulator.generate_data()