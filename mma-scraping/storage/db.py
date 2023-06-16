import os, sys
from bs4 import BeautifulSoup
import psycopg2
import requests
import json
from dotenv import load_dotenv



from scrape import *


def save_to_db(athlete_data: any) -> None:

    load_dotenv()

    sys.path.append('../')

    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    USERNAME = os.getenv ('DB_USERNAME')
    PASSWORD = os.getenv('DB_PASSWORD')
    DATABASE = os.getenv('DB_DATABASE')  
        
    count, tot = 0, 0
    # First, strip the list of weight classes of the first element, which is the list the pound-for-pound rankings
    p4p_rankings = []
    # Turn this into a hashmap, where the key is the name of the athlete and the value is the rank
    p4p_rankings_map = {athlete['name']: athlete['rank'] for athlete in p4p_rankings}
    
    #insert data into table, from list of json objects in data.json
    for weight_class in athlete_data:
        for athlete in weight_class:
            athlete = validate(athlete)
            try:
                p4p_rank = athlete['p4p_rank']
                wc = athlete['weightclass'].strip().replace("'", '').lower()

                cur_athlete_sql = f"INSERT INTO top (name, name_postfix, weight_class, rank, first_round_finishes, sig_strikes_landed, sig_strikes_attempted, striking_accuracy, take_downs_landed, take_downs_attempted, take_down_accuracy, sig_strikes_landed_per_min, sig_strikes_absorbed_per_min, take_down_avg_per_15_min, submission_avg_per_15_min, sig_strikes_defense, take_down_defense, kockdown_avg, average_fight_time, sig_strikes_standing, sig_strikes_clinch, sig_strikes_ground, sig_strike_head, sig_strike_body, sig_strike_leg, wins_by_knockout, wins_by_submission, wins_by_decision, fights, p4p_rank) VALUES ('{str(athlete['name']).strip()}', '{str(athlete['name_postfix'])}', '{wc}', {int(athlete['rank'].strip())}, {int(athlete['data']['first_round_finishes'])}, {float(athlete['data']['sig_strikes_landed'])}, {float(athlete['data']['sig_strikes_attempted'])}, {float(athlete['data']['striking_accuracy'])}, {int(athlete['data']['take_downs_landed'])}, {int(athlete['data']['take_downs_attempted'])}, {float(athlete['data']['take_down_accuracy'])}, {float(athlete['data']['sig_strikes_landed_per_min'])}, {float(athlete['data']['sig_strikes_absorbed_per_min'])}, {float(athlete['data']['take_down_avg_per_15_min'])}, {float(athlete['data']['submission_avg_per_15_min'])}, {int(athlete['data']['sig_strikes_defense'])}, {int(athlete['data']['take_down_defense'])}, {float(athlete['data']['kockdown_avg'])}, '{str(athlete['data']['average_fight_time'])}', {int(athlete['data']['sig_strikes_standing'])}, {int(athlete['data']['sig_strikes_clinch'])}, {int(athlete['data']['sig_strikes_ground'])}, {int(athlete['data']['sig_strike_head'])}, {int(athlete['data']['sig_strike_body'])}, {int(athlete['data']['sig_strike_leg'])}, {int(athlete['data']['wins_by_knockout'])}, {int(athlete['data']['wins_by_submission'])}, {int(athlete['data']['wins_by_decision'])}, '{str(athlete['data']['fights'])}', {p4p_rank})"
                db.execute_query(cur_athlete_sql)

            except Exception as e:
                print(e)
                count += 1

            tot += 1

    print(f'Inserted {tot-count} of {tot} athletes into database')
    db.close()

    athlete['data']['fights'] = json.dumps(athlete['data']['fights'])

    return athlete


if __name__ == '__main__':
    save_to_db(get_athlete_data())