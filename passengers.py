class Flight:

    counter = 1

    def __init__(self, duration, destination, origin):

        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight dureation: {self.duration}")

        print()
        print("passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name

def main():
    f1 = Flight(origin="London", destination="New York", duration=185)

    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()

if __name__ == "__main__":
    main()
