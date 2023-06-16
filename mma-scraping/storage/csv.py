import os, sys
from bs4 import BeautifulSoup
import json

sys.path.append('../')

from scrape import *

def save_to_csv(athelte_data: any) -> None:
    pass


if __name__ == '__main__':
    athlete_data = get_all_athletes()
    save_to_csv(athlete_data)