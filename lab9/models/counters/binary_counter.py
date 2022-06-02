from models.counters.counter import Counter


class BinaryCounter(Counter):
    def __init__(self, number_of_elements: int, device_type: str, device_name: str, price: float):
        super().__init__(number_of_elements, device_type, device_name, price)

    def __str__(self):
        return f'Device type: {self.device_type}, device name: {self.device_name}, device price: {self.price}, ' \
            f'number of elements: {self.number_of_elements}'
