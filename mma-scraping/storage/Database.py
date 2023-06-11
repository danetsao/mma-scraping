# Module exquizdb.py
import psycopg2 as pg2
from dotenv import load_dotenv
import os

load_dotenv()
# Database connection constants
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
USERNAME = os.getenv ('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_DATABASE')  

PRESQL = '''DROP TABLE IF EXISTS top'''

SQL = '''CREATE TABLE IF NOT EXISTS top (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
name_postfix VARCHAR(100),
weight_class VARCHAR(100),
rank INTEGER,
first_round_finishes INTEGER,
sig_strikes_landed FLOAT,
sig_strikes_attempted FLOAT,
striking_accuracy FLOAT,
take_downs_landed INTEGER,
take_downs_attempted INTEGER,
take_down_accuracy FLOAT,
sig_strikes_landed_per_min FLOAT,
sig_strikes_absorbed_per_min FLOAT,
take_down_avg_per_15_min FLOAT,
submission_avg_per_15_min FLOAT,
sig_strikes_defense INTEGER,
take_down_defense INTEGER,
kockdown_avg FLOAT,
average_fight_time VARCHAR(10),
sig_strikes_standing INTEGER,
sig_strikes_clinch INTEGER,
sig_strikes_ground INTEGER,
sig_strike_head INTEGER,
sig_strike_body INTEGER,
sig_strike_leg INTEGER,
wins_by_knockout INTEGER,
wins_by_submission INTEGER,
wins_by_decision INTEGER,
fights JSONB,
p4p_rank INTEGER
)
'''
# Fights is a list of json

class Database:
  def __init__(self, db, username, password, port):
    self.db = db
    self.user = username
    self.password = password
    self.port = port
    self.cur = None
    self.conn = None

  def connect(self):
    self.conn = pg2.connect(database=self.db, user=self.user, password=self.password, port=self.port)
    self.cur = self.conn.cursor()
    self.cur.execute(PRESQL)
    self.cur.execute(SQL)
    self.conn.commit()


  def execute_query(self, query):
    try:
        self.cur.execute(query)
        self.conn.commit()
    except Exception as e:
        print(e)
        self.conn.rollback()

  def close(self):
    self.conn.commit()
    self.cur.close()
    self.conn.close()

db = Database(DATABASE, USERNAME, PASSWORD, PORT)

db.connect()
