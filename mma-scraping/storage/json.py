import os, sys
from bs4 import BeautifulSoup
import json

sys.path.append('../')

from scrape import *


# Main function
def save_to_json(athlete_data: any) -> None:

    # Save output to json file
    print('Saving output to json file...')

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(athlete_data, f, ensure_ascii=False)


if __name__ == '__main__':
    athlete_data = get_all_athletes()
    save_to_json(athlete_data)
    