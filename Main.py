class Star_Cinema:
    # to store hall objects.
    hall_list = []

    #updates hall information.
    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

#Hall Class
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.seats = {}
        self.show_list = []
        #Add this hall to star_cinema hall list.
        self.entry_hall(self)

    #mehtod-1
    def entry_show(self,show_id,movie_name,time):
        # Made a tuple with all information and appended it to the show_list.
        show_info = (show_id,movie_name,time)
        self.show_list.append(show_info) 

        #Create a 2D table to store seat information.
        seat_layout = [ ["Free  " for j in range(self.__cols) ] for i in range(self.__rows) ]

        #Assign the seat_layout to seats with show_id.
        self.seats[show_id] = seat_layout

    #method-2
    def book_seats(self, show_id, seat_positions):
        if show_id not in self.seats:
            print(f"{show_id} is an invalid show id.")
            return
        
        # Get the seat layout for the given show.
        seat_layout = self.seats[show_id]


        for row,col in seat_positions:
            #Check the row and column is within range.
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Seat at row {row+1}, column {col+1} is out of range.")
            elif seat_layout[row][col] == "Free  ":
                seat_layout[row][col] = "Booked"
                print(f"Seat at row {row+1}, column {col+1} booked successfully.")
            else:
                print(f"Sorry! Seat at row {row+1}, column {col+1} is already booked.")

    #mehtod-3
    def view_show_list(self):
        for show in self.show_list:
            show_id, movie_name, time = show
            print(f"Show ID: {show_id} ---- Movie: {movie_name} ---- Date: 9/11/2024 ---- Time: {time}")

    #method-4
    def view_available_seats(self,show_id):
        #Check the show id.
        if show_id not in self.seats:
            print(f"{show_id} is an invalid show id.")
            return
        seat_layout = self.seats[show_id]

        print(f"\nSeat configuration for show {show_id}:\n")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(seat_layout[i][j], end = " ")
            print()



#Option showing function
def optionShower():
    print("\n1.View all show today.")
    print("2.View available seats.")
    print("3.Book ticket.")
    print("4.Exit.")

#creating hall object.
hall1 = Hall(10,10,110)


#adding all deatails of hall1.
hall1.entry_show("113","Wall-E","6:00 PM")
hall1.entry_show("114","Zootopia","4:00 PM")
hall1.entry_show("115","Cars 4","8:00 PM")


#main function starts

while True:
    optionShower()
    choice = int(input("Enter option: "))

    if choice == 1:
        print("----------------------------------------------")
        hall1.view_show_list()
        print("----------------------------------------------")
    elif choice == 2:
        show_id = input("Enter show id: ")
        hall1.view_available_seats(show_id)
        print("----------------------------------------------")
    elif choice == 3:
        show_id = input("Enter show id: ")
        tickets = int(input("How many tickets do you want: "))

        #taking seat positions.
        seat_positions = []
        for i in range(tickets):
            row = int(input("Enter seat row [1,10]: "))
            col = int(input("Enter seat column [1,10]: "))
            seat_positions.append((row-1,col-1))

        print("\n----------------------------------------------")
        hall1.book_seats(show_id,seat_positions)
        print("----------------------------------------------")
    elif choice == 4:
        print("\nThanks for using the service. Have a good day!")
        break
    else:
        print("\nWrong option! Choose again")


