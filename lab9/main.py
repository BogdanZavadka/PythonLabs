from models.counters.binary_counter import BinaryCounter
from models.counters.binary_decimal_counter import BinaryDecimalCounter
from models.counters.reverse_counter import ReverseCounter
from models.triggers.d_trigger import DTrigger
from models.triggers.rs_trigger import RSTrigger
from models.other_elements.multiplexer import Multiplexer
from models.other_elements.shift_register import ShiftRegister


def main():
    binary_counter = BinaryCounter(10, 'counter', 'binary counter', 500)
    binary_decimal_counter = BinaryDecimalCounter(15, 'counter', 'binary-decimal counter', 700)
    reverse_counter = ReverseCounter(10, 'counter', 'reverse counter', 900)
    d_trigger = DTrigger('trigger', 'D-trigger', 1000, 2)
    rs_trigger = RSTrigger('trigger', 'RS-trigger', 1200, 3)
    multiplexer = Multiplexer('other devices', 'multiplexer', 650, 13)
    shift_register = ShiftRegister('other devices', 'shift register', 770, 4)
    print(binary_counter)
    print(binary_decimal_counter)
    print(reverse_counter)
    print(d_trigger)
    print(rs_trigger)
    print(multiplexer)
    print(shift_register)


if __name__ == '__main__':
    main()
