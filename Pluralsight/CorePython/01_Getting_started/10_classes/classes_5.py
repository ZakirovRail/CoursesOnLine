from pprint import pprint as pp

class Flight:
    """
    A flight with a particular passenger aircraft.
    """

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')

        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')

        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError(f'Invalid route number "{number}"')

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name.
        Raises:
            ValueError: If the seat is unavailable
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row  ][letter] = passenger


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


f = Flight("BA758", Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# f.allocate_seat("12A", "Guido van Rossum")
f.allocate_seat("12A", "Rasmus Leodorf")
f.allocate_seat("15F", "Bjarne Stroustrup")
f.allocate_seat("15E", "Anders Hejlsberg")
f.allocate_seat("1C", "John McCarthy")
f.allocate_seat("1D", "Richard Hickey")
pp(f._seating)
"""
[None,
 {'A': None,
  'B': None,
  'C': 'John McCarthy',
  'D': 'Richard Hickey',
  'E': None,
  'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': 'Rasmus Leodorf', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None,
  'B': None,
  'C': None,
  'D': None,
  'E': 'Anders Hejlsberg',
  'F': 'Bjarne Stroustrup'},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}]
"""
