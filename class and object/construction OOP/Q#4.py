# Design a Clock class with attributes for hours and minutes. Create a constructor to initialize the time and a method to add minutes to the clock.
class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_minutes(self, additional_minutes):
        total_minutes = self.hours * 60 + self.minutes + additional_minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"


my_clock = Clock(9, 30)
print("Current time:", my_clock)
my_clock.add_minutes(75)
print("Time after adding 75 minutes:", my_clock)
