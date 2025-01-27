# Assignment 4: Simulate managing reservations for a restaurant

# Main logic for the program:
# Calls get_seating_capacity() to obtain user-specified number of seats in the restaurant.
# Calls manage_reservations(number_of_seats) to read the file containing number of people in a reservation request.
# Calls display_results(accepted, not_accepted) to display the total number of people whose reservations were accepted or not.

def main():
    number_of_seats = get_seating_capacity()
    accepted, not_accepted = manage_reservations(number_of_seats)
    display_results(accepted, not_accepted)


# Prompts for the seating capacity of the restaurant.
# Valid values are integers >= 10.
# If an invalid value is entered, display a message, and continue to prompt until a valid value is provided.
def get_seating_capacity():
    number_of_seats = input('What is the seating capacity for this restaurant? ')
    while not number_of_seats.isnumeric() or int(number_of_seats) < 10:
        print('Error: Number of seats must be at least 10.')
        number_of_seats = input('What is the seating capacity for this restaurant? ')
    number_of_seats = int(number_of_seats)
    return number_of_seats


# Open the reservations.txt file, and read each line.
# Each line specifies an integer that represents the number of people for a reservation.
# Keep a count of the number of people whose reservation has been accepted.
# If the number of people requesting a reservation would exceed the seating capacity,
# then the reservation is not accepted.
# Keep a count of the number of people whose reservation has not been accepted.
# Reservation requests for more than 6 people are not accepted, regardless of the available seating.
def manage_reservations(number_of_seats):
    filename = 'reservations.txt'
    try:
        reservations_file = open(filename, 'r')

        accepted = 0
        not_accepted = 0

        for line in reservations_file:
            reservation_request = int(line)
            if reservation_request <= 6 and reservation_request <= number_of_seats:
                number_of_seats = number_of_seats - reservation_request
                accepted = accepted + reservation_request
            else:
                not_accepted = not_accepted + reservation_request
        reservations_file.close()
        return accepted, not_accepted
    except FileNotFoundError as err:
        print('Error: cannot find file,', filename)
        print('Error:', err)
    except OSError as err:
        print('Error: cannot access file,', filename)
        print('Error:', err)
    except ValueError as err:
        print('Error: invalid data found in file', filename)
        print('Error:', err)
    except Exception as err:
        print('An unknown error occurred')
        print('Error:', err)


# Display the number of people whose reservations were accepted, and not accepted
def display_results(accepted, not_accepted):
    print(accepted, 'people were accepted')
    print(not_accepted, 'people were not accepted')


main()
