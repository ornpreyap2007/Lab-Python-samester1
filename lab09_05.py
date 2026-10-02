def SeatType() :
    while True :
        seat = input('Select the seat type (P or D or H) : ')
        if seat == "P" or seat == "D" or seat == "H" :
            break
        else :
            print('Wrong seat type! Please select again.')
    return seat
def MovieType() :
    while True :
        movie = input('Select the movie type (1 or 2) : ')
        if movie == "1" or movie == "2" :
            break
        else :
            print('Wrong movie type! Please select again.')
    return movie 
def TicketPrice(s,m) :
    if m == "1" :
        if s == "P" :
            price = 100
        elif s == "D" :
            price = 140
        else :
            price = 400
    if m == "2" :
        if s == "P" :
            price = 120
        elif s == "D" :
            price = 200
        else :
            price = 500
    print('\nThe ticket price is',price)
s = SeatType()
m = MovieType()
TicketPrice(s,m)
    