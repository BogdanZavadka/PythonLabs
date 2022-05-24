from PythonLabs.lab9.models.counters.counter import Counter


class BinaryDecimalCounter(Counter):
    def __init__(self, number_of_elements, device_type, device_name, price):
        super().__init__(number_of_elements, device_type, device_name, price)

    def __str__(self):
        return f'Device type: {self.device_type}, device name: {self.device_name}, device price: {self.price}, ' \
            f'number of elements: {self.number_of_elements}'
