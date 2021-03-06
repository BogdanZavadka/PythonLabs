from models.digital_element import DigitalElement


class Multiplexer(DigitalElement):
    def __init__(self, device_type: str, device_name: str, price: float, number_of_inputs: int):
        super().__init__(device_type, device_name, price)
        self.number_of_inputs = number_of_inputs

    def __str__(self):
        return f'Device type: {self.device_type}, device name: {self.device_name}, device price: {self.price}, ' \
            f'number of inputs: {self.number_of_inputs}'