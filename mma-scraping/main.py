from storage.json import save_to_json
from storage.db import save_to_db
from storage.csv import save_to_csv
from storage import *
from scrape import *
import sys
import os
import json
import psycopg2 as pg2
from dotenv import load_dotenv
from storage.Database import db
import os, sys
from bs4 import BeautifulSoup
import psycopg2
import requests
from storage.validate import validate



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
    print("4. Scrape data and save to CSV file")

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
        show = input("Would you like to see the status of the scraping? (y/n): ")
        if show == "y":
            show_data = True
        else:
            show_data = False

        print("Scraping data and saving to json file...")

        athlete_data = get_all_athletes(show_data)

        save_to_json(athlete_data)
        
    
    # SAVE TO DATABASE
    elif user_input == "3":
        show = input("Would you like to see the status of the scraping? (y/n): ")
        if show == "y":
            show_data = True
        else:
            show_data = False
        print("Scraping data and saving to database...")

        athlete_data = get_all_athletes(show_data)

        save_to_db(athlete_data)

    
    # SAVE TO CSV FILE
    elif user_input == "4":

        show = input("Would you like to see the status of the scraping? (y/n): ")
        if show == "y":
            show_data = True
        else:
            show_data = False

        print("Scraping data and saving to CSV file...")

        athlete_data = get_all_athletes(show_data)

        save_to_csv(athlete_data)

    # INVALID INPUT
    else:
        print("Invalid input. Please try again.")
        main()


if __name__ == "__main__":
    main()