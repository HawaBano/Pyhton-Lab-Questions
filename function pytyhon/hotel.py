class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.available = True

    def display(self):
        return f"Room {self.room_number} ({self.room_type}) - {'Available' if self.available else 'Occupied'}"

class Guest:
    def __init__(self, name, guest_id):
        self.name = name
        self.guest_id = guest_id
        self.booked_rooms = []

    def book_room(self, room):
        self.booked_rooms.append(room)

    def display(self):
        return f"Guest {self.name} (ID: {self.guest_id})"

class Booking:
    def __init__(self, booking_id, guest, room):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room

    def display(self):
        return (f"Booking ID: {self.booking_id}\nGuest: {self.guest.name}\nRoom: {self.room.room_number}")

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.guests = {}
        self.bookings = {}

    def add_room(self, room_number, room_type, price_per_night):
        self.rooms[room_number] = Room(room_number, room_type, price_per_night)

    def register_guest(self, name, guest_id):
        self.guests[guest_id] = Guest(name, guest_id)

    def make_booking(self, booking_id, guest_id, room_number):
        guest = self.guests.get(guest_id)
        room = self.rooms.get(room_number)
        if not guest or not room or not room.available:
            return "Invalid booking."
        booking = Booking(booking_id, guest, room)
        self.bookings[booking_id] = booking
        guest.book_room(room)
        room.available = False
        return "Booking successful."

    def handle_check_in(self, booking_id):
        booking = self.bookings.get(booking_id)
        if not booking:
            return "Cannot check in."
        return f"Guest {booking.guest.name} checked in to room {booking.room.room_number}."

    def handle_check_out(self, booking_id):
        booking = self.bookings.pop(booking_id, None)
        if not booking:
            return "Cannot check out."
        booking.room.available = True
        booking.guest.booked_rooms.remove(booking.room)
        return f"Guest {booking.guest.name} checked out from room {booking.room.room_number}."

    def display(self):
        rooms_info = 'Rooms:\n' + '\n'.join(room.display() for room in self.rooms.values())
        guests_info = 'Guests:\n' + '\n'.join(guest.display() for guest in self.guests.values())
        bookings_info = 'Bookings:\n' + '\n'.join(booking.display() for booking in self.bookings.values())
        return f"Hotel Management System\n{rooms_info}\n{guests_info}\n{bookings_info}"

# Example Usage
hotel = Hotel()
hotel.add_room(101, 'Single', 100)
hotel.add_room(102, 'Double', 150)
hotel.register_guest('Alice Smith', 'G001')
hotel.register_guest('Bob Johnson', 'G002')

print(hotel.make_booking('B001', 'G001', 101))
print(hotel.make_booking('B002', 'G002', 102))
print(hotel.handle_check_in('B001'))
print(hotel.handle_check_out('B001'))
print(hotel.display())
