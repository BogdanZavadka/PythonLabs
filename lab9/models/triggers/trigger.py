from models.digital_element import DigitalElement


class Trigger(DigitalElement):
    def __init__(self, device_type: str, device_name: str, price: float, number_of_states: int):
        super().__init__(device_type, device_name, price)
        self.number_of_states = number_of_states
