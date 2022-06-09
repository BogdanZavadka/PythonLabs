from models.digital_element import DigitalElement


class ShiftRegister(DigitalElement):
    def __init__(self, device_type: str, device_name: str, price: float, bit_rate: int):
        super().__init__(device_type, device_name, price)
        self.bit_rate = bit_rate

    def __str__(self):
        return f'Device type: {self.device_type}, device name: {self.device_name}, device price: {self.price}, ' \
               f'bit rate: {self.bit_rate}'
