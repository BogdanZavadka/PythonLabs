from PythonLabs.lab9.models.digital_element import DigitalElement


class Trigger(DigitalElement):
    def __init__(self, device_type, device_name, price, number_of_states):
        super().__init__(device_type, device_name, price)
        self.number_of_states = number_of_states
