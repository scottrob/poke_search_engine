import psycopg2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series


df = pd.read_csv('poke.csv','\t')


conn = psycopg2.connect("dbname=poke user=thescottrob host=/tmp/")
cur = conn.cursor()
cur.execute("CREATE TABLE poke (id serial PRIMARY KEY, df varchar);")
for row in df.itertuples():
    cur.execute("""INSERT INTO poke VALUES (DEFAULT, {}, {}, {}, {}, {}, {}, {}, {}, {});""".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
cur.execute("SELECT * FROM poke;")
conn.commit()
cur.close()
conn.close()
