from datetime import datetime

class Room:
    def __init__(self, number, room_type, price_per_night):
        self.number = number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.available = True

    def display(self):
        return (f"""
                Room NO:{self.number}
                Room Type:{self.room_type}
                Price={self.price_per_night}
                Available={self.available}
                """)


class Guest:
    def __init__(self, name, guest_id):
        self.name = name
        self.guest_id = guest_id
        self.booked_rooms = []

    def display(self):
        return f"Guest {self.name}, ID={self.guest_id}"

class Booking:
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def display(self):
        return (f"""
                Booking ID:{self.booking_id}
                Guest:{self.guest.name} 
                Room:{self.room.number}
                Check-in:{self.check_in_date}
                Check-out:{self.check_out_date}
""")

class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def register_guest(self, guest):
        self.guests.append(guest)

    def make_booking(self, guest_id, room_number, check_in_date, check_out_date):
        guest = None
        room = None
        
        for g in self.guests:
            if g.guest_id == guest_id:
                guest = g
                break

        for r in self.rooms:
            if r.number == room_number:
                room = r
                break

        if guest is None:
            print(f"Guest with ID  not found.")
            return
        if room is None:
            print(f"Room with number not found.")
            return
        if not room.available:
            print(f"Room  is not available.")
            return

        booking_id = len(self.bookings) + 1
        booking = Booking(booking_id, guest, room, check_in_date, check_out_date)
        self.bookings.append(booking)
        guest.booked_rooms.append(room)
        room.available = False
        print(f"Booking made: {booking}")

    def check_in(self, guest_id, room_number):
        found = False
        for b in self.bookings:
            if b.guest.guest_id == guest_id and b.room.number == room_number:
                print(f"Guest  checked into room {room_number}.")
                found = True
                break

        if not found:
            print(f"No booking found for Guest  and Room {room_number}.")

    def check_out(self, guest_id, room_number):
        found = False
        for b in self.bookings:
            if b.guest.guest_id == guest_id and b.room.number == room_number:
                b.room.available = True
                b.guest.booked_rooms.remove(b.room)
                self.bookings.remove(b)
                print(f"Guest checked out from room {room_number}.")
                found = True
                break

        if not found:
            print(f"No booking found for Guest  and Room {room_number}.")

hotel = Hotel()


hotel.add_room(Room(101, 'Single', 100))
hotel.add_room(Room(102, 'Double', 150))


hotel.register_guest(Guest('Ali', 1))
hotel.register_guest(Guest('Hamza', 2))

hotel.make_booking(1, 101, datetime(2024, 7, 25), datetime(2024, 7, 30))
hotel.make_booking(2, 102, datetime(2024, 7, 26), datetime(2024, 7, 28))


hotel.check_in(1, 101)
hotel.check_out(1, 101)
