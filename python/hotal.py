class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def display(self):
        return f"Room {self.room_number} ({self.room_type}) - ${self.price_per_night}/night - {'Available' if self.is_available else 'Booked'}"


class Guest:
    def __init__(self, name, guest_id):
        self.name = name
        self.guest_id = guest_id
        self.booked_rooms = []

    def display(self):
        return f"Guest {self.guest_id}: {self.name}, Booked Rooms: {', '.join(str(room.room_number) for room in self.booked_rooms)}"


class Booking:
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def display(self):
        return (f"Booking {self.booking_id}: Guest {self.guest.name} (ID: {self.guest.guest_id}), "
                f"Room {self.room.room_number}, Check-in: {self.check_in_date}, Check-out: {self.check_out_date}")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = []
        self.bookings = []

    def add_room(self, room_number, room_type, price_per_night):
        room = Room(room_number, room_type, price_per_night)
        self.rooms.append(room)
        print(f"Added {room}")

    def register_guest(self, name, guest_id):
        guest = Guest(name, guest_id)
        self.guests.append(guest)
        print(f"Registered {guest}")

    def make_booking(self, booking_id, guest_id, room_number, check_in_date, check_out_date):
        guest = next((g for g in self.guests if g.guest_id == guest_id), None)
        room = next((r for r in self.rooms if r.room_number == room_number), None)

        if guest and room and room.is_available:
            booking = Booking(booking_id, guest, room, check_in_date, check_out_date)
            guest.booked_rooms.append(room)
            room.is_available = False
            self.bookings.append(booking)
            print(f"Made {booking}")
        else:
            print("Cannot make booking: invalid guest ID, room number, or room not available.")

    def handle_check_in(self, booking_id):
        booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
        if booking:
            print(f"Check-in successful for {booking}")
        else:
            print("Booking ID not found for check-in.")

    def handle_check_out(self, booking_id):
        booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
        if booking:
            booking.room.is_available = True
            booking.guest.booked_rooms.remove(booking.room)
            self.bookings.remove(booking)
            print(f"Check-out successful for {booking}")
        else:
            print("Booking ID not found for check-out.")



hotel = Hotel("Grand Plaza")

hotel.add_room(101, "Single", 100)
hotel.add_room(102, "Double", 150)


hotel.register_guest("Ali", "G001")
hotel.register_guest("Hamza", "G002")

hotel.make_booking("B001", "G001", 101, "2024-08-01", "2024-08-05")
hotel.make_booking("B002", "G002", 102, "2024-08-02", "2024-08-06")


hotel.handle_check_in("B001")


hotel.handle_check_out("B001")
