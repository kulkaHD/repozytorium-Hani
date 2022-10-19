from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column
import csv

engine = create_engine('sqlite:///czyste_stacje.db')
meta = MetaData()

clean_stations = Table(
    'clean_stations', meta,
    Column('station', String, primary_key = True),
    Column('latitude', Integer),
    Column('longitude', Integer),
    Column('elevation', Integer),
    Column('name', String),
    Column('country', String),
    Column('state', String),
    )

clean_measure = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('date', String),
    Column('precip', Integer),
    Column('tobs', String)
    )

stations = Table(
    "stations",
     meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('latitude', Integer),
    Column('longitude', Integer),
    Column('elevation', Integer),
    Column('name', String),
    Column('country', String),
    Column('state', String),
    Column('station', String),
    Column('date', String),
    Column('precip', Integer),
    Column('tobs', String)
    )

insCS = clean_stations.insert()
insCM = clean_measure.insert()
insSTATIONS = stations.insert()

dict_clean_stations = {}
data_clean_measure = []
data_clean_stations = []
all_data = []

with open('clean_stations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for rowCS in reader:
        data_clean_stations.append(rowCS)
        dict_clean_stations[rowCS["station"]] = rowCS

with open('clean_measure.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for rowCM in reader:
        row_data = rowCM
        row_data.update(dict_clean_stations[rowCM["station"]])
        data_clean_measure.append(rowCM)
        all_data.append(row_data)

meta.create_all(engine)

conn = engine.connect()
# conn.execute(insCS,data_clean_stations)
# conn.execute(insCM,data_clean_measure)
# conn.execute(insSTATIONS,all_data)

# print (f'''

# Odwołanie się do tabeli poprzez wywyołanie

# conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()

# Daje następujące wyniki:
# ''')

# for i in conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall():
#     print (i)

from sqlalchemy.sql import select
s = select(clean_stations)
result = conn.execute(s)
for i in result:
    print(i)

conn.close()