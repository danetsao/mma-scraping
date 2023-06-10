from storage import *
from scrape import *


def main():

    """
    All in one function that takes user input and then configures from there
    For more info, see https://github.com/danetsao/mma-scraping
    """
    ERROR_MESSAGE = "Unexpected error. Please try again or contact the developer."
    print("Welcome to the MMA Scraper!")
    print("Please select from the following options:")
    print("1. Scrape data and print to console")
    print("2. Scrape data and save to json file")
    print("3. Scrape data and save to database")
    print("4. Scrape data and save to json file and database")

    user_input = input("Please enter a number: ")

    # PRINT CONSOLE
    if user_input == "1":
        show = input("Would you like to see the status of the scraping? (y/n): ")
        if show == "y":
            show_data = True
        else:
            show_data = False

        print("Scraping data and printing to console...")
        athlete_data = get_all_athletes(show_data)

        print(athlete_data)
    
    # SAVE TO JSON FILE
    elif user_input == "2":
        print("Scraping data and saving to json file...")
    
    # SAVE TO DATABASE
    elif user_input == "3":
        print("Scraping data and saving to database...")
    
    # SAVE TO JSON FILE AND DATABASE
    elif user_input == "4":
        print("Scraping data and saving to json file and database...")

    # INVALID INPUT
    else:
        print("Invalid input. Please try again.")
        main()


if __name__ == "__main__":
    main()