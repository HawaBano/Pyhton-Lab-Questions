# Create a hotel management system with the following classes and features:
# A Room class with attributes for room number, room type, price per night,
#  and availability status.
# A Guest class with attributes for name, guest ID, and a list of booked rooms.
# A Booking class with attributes for booking ID, guest, room, check-in date, and 
# check-out date.
# A Hotel class to manage rooms, guests, and bookings. Implement methods to add rooms, 
# register guests, make bookings, and handle check-ins/check-outs.


class Room:
    
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.available = True

class Guest:

    def __init__(self, name , guest_id):
        self.name = name
        self.guest_id = guest_id
        self.booked_rooms = []

class Booking:
    def __init__(self, booking_id, guest, room, check_in, check_out):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out


class Hotel:

    def __init__(self):
        self.rooms = []
        self.guests = []
        self.bookings = []

    
    def add_room(self,room):
        self.rooms.append(room)
        print("room booked successfully")
        

    def register_guest(self, guest):
       self.guests.append(guest)
       print("Guest regester successfully")


##A Hotel class to manage rooms, guests, and bookings. Implement methods to add rooms, 
# register guests, make bookings, and handle check-ins/check-outs.

    def make_booking(self,booking):
        self.bookings.append(booking)
        booking.room.available = False
        booking.guest.booked_rooms.append(booking.room)
        # self.bookings.guest.booked_rooms.append(booking.room)
        print("Room booked successfully")

    def check_in(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.room.available = False
                print("Checked in to Room  for Booking ")
                return
        print("Booking ID  not found")

    def check_out(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.room.available = True
                booking.guest.booked_rooms.remove(booking.room)
                self.bookings.remove(booking)
                print("Checked out of Room for Booking ")
        print("Booking ID  not found.")
      
       



hotel = Hotel()
room1 = Room(101, "Single", 100)
hotel.add_room(room1)

guest1 = Guest("Ali", 1)
hotel.register_guest(guest1)

booking1 = Booking(1, guest1, room1, "2024-08-01", "2024-08-05")
hotel.make_booking(booking1)


hotel.check_in(1)
hotel.check_out(1)
