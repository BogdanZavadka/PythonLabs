from abc import ABC


class DigitalElement(ABC):
    def __init__(self, device_type: str, device_name: str, price: float):
        self.device_type = device_type
        self.device_name = device_name
        self.price = price
