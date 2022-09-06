import csv
import pandas as pd

rows = []
with open('Stars.csv', 'r') as f:
    csv_r = csv.reader(f)
    for i in csv_r:
        rows.append(i)

headers = rows[0]
stars_data = rows[1:]
headers[0] = 'Index'

star_data = []
for star in stars_data:
    if star[3] != '?': 
        star[3] = float(star[3].strip("\'"))*1.989e+30
    
    if star[4] != '?':
        star[4] = float(star[4].strip("\'"))*6.957e+8
    star_data.append(star)

star_data_gravity = []

for star in star_data:
    if star[3] != '?' and star[4] != '?':
        gravity = (6.674e-11 * float(star[3]))/(float(star[4])*float(star[4]))
    star.append(gravity)
    star_data_gravity.append(star)

name = []
distance = []
mass = []
radius = []
gravity = []

for i in star_data_gravity:
    name.append(i[1])
    distance.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)

df.to_csv('final.csv')