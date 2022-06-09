from models.triggers.trigger import Trigger


class DTrigger(Trigger):
    def __init__(self, device_type: str, device_name: str, price: float, number_of_states: int):
        super().__init__(device_type, device_name, price, number_of_states)

    def __str__(self):
        return f'Device type: {self.device_type}, device name: {self.device_name}, device price: {self.price}, ' \
            f'number of states: {self.number_of_states}'
