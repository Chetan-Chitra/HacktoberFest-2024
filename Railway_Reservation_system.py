class Train:
    def __init__(self, train_number, name, source, destination, total_seats):
        self.train_number = train_number
        self.name = name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats

class ReservationSystem:
    def __init__(self):
        self.trains = {}
        self.bookings = {}

    def add_train(self, train):
        self.trains[train.train_number] = train

    def display_trains(self):
        print("\nAvailable Trains:")
        for train in self.trains.values():
            print(f"Train {train.train_number}: {train.name} - From {train.source} to {train.destination}, Available Seats: {train.available_seats}")

    def book_ticket(self, train_number, passenger_name):
        if train_number not in self.trains:
            return "Train not found."
        
        train = self.trains[train_number]
        if train.available_seats > 0:
            train.available_seats -= 1
            booking_id = f"{train_number}-{len(self.bookings) + 1}"
            self.bookings[booking_id] = {"train": train, "passenger": passenger_name}
            return f"Booking confirmed. Booking ID: {booking_id}"
        else:
            return "Sorry, no seats available."

    def cancel_booking(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings.pop(booking_id)
            booking['train'].available_seats += 1
            return f"Booking {booking_id} cancelled successfully."
        else:
            return "Booking not found."

def main():
    reservation_system = ReservationSystem()

    # Adding sample trains
    reservation_system.add_train(Train("123", "Express", "New York", "Washington", 50))
    reservation_system.add_train(Train("456", "Superfast", "Los Angeles", "San Francisco", 40))

    while True:
        print("\n1. Display available trains")
        print("2. Book a ticket")
        print("3. Cancel a booking")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            reservation_system.display_trains()
        elif choice == '2':
            train_number = input("Enter train number: ")
            passenger_name = input("Enter passenger name: ")
            print(reservation_system.book_ticket(train_number, passenger_name))
        elif choice == '3':
            booking_id = input("Enter booking ID: ")
            print(reservation_system.cancel_booking(booking_id))
        elif choice == '4':
            print("Thank you for using the Railway Reservation System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
