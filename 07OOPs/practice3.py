

class Booking:
    movie_name = "Avengers"
    theater = "PVR"
    capacity = 400
    def __init__(self, cx_name, cx_num, no_of_tickets):
        self.cx_name = cx_name
        self.cx_num = cx_num
        self.no_of_tickets = no_of_tickets

    def display(self):
        print(f"{self.cx_name} has booked {self.no_of_tickets} tickets for the movie {self.movie_name} at {self.theater}")

    def book(self):
        if self.no_of_tickets <= Booking.capacity:
            Booking.capacity -= self.no_of_tickets
            print(f"Tickets booked successfully for {self.no_of_tickets} tickets, now the available tickets are {Booking.capacity}")
        else:
            print(f"Sorry, the tickets are not available for {self.no_of_tickets} tickets, available tickets are {Booking.capacity}")


booking1 = Booking("Chenchu", 1234567890, 50)
booking2 = Booking("Manohar", 9876543210, 100)
booking3 = Booking("Krishna", 1234509876, 105) 
booking4 = Booking("Ram", 1234567890, 200)

booking1.display()
booking2.display()
booking3.display()

booking1.book()
booking2.book()
booking3.book()
booking4.book()




