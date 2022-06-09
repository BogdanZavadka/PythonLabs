from models.digital_element import DigitalElement


class Counter(DigitalElement):
    def __init__(self, number_of_elements: int, device_type: str, device_name: str, price: float):
        super().__init__(device_type, device_name, price)
        self.number_of_elements = number_of_elements
