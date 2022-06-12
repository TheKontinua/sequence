import random
import datetime
import numpy as np
import sys
import math
import sqlite3 as db

def should_generate_error():
    return random.random() < 0.008

if len(sys.argv) < 2:
    print(f"Usage: python {argv[0]} <output_file>")
    exit(1)

output_filename = sys.argv[1]

row_count = 1000
max_id = 9999999
incorrect_statuses = {'available': ['Available', 'good'], 'rented': ['out', 'Rented'], 'broken':['Busted', 'Flat tire']}
correct_statuses = list(incorrect_statuses.keys())
correct_brands = ['Trek', 'BMC', 'Cannondale', 'Giant', 'Canyon', 'GT']
now = datetime.datetime.now(datetime.timezone.utc)
print(f"{now}: writing {row_count} rows to {output_filename}")
first_purchase = datetime.date.fromisoformat("1970-01-01")
max_days_after_first = 40 * 365

bike_ids = []
used_ids = set()
sizes = []
brands = []
# last_rented_dates = []
prices = []
purchase_dates = []
statuses = []


for i in range(row_count):
    new_id = random.randint(1, max_id)
    while new_id in used_ids:
        new_id = random.randint(1, max_id)
    used_ids.add(new_id)
    id_str = f"{new_id:07d}"
    bike_ids.append(id_str)

    # Status
    p = random.random()
    if p < 0.1:
        original_status = correct_statuses[2]
    elif p < 0.4:
        original_status = correct_statuses[1]
    else:
        original_status = correct_statuses[0]

    original_status = random.choice(correct_statuses)
    
    # Incorrect entry?
    if should_generate_error():
        status = random.choice(incorrect_statuses[original_status])
    else:
        status = original_status

    # Missing entry?
    if should_generate_error():
        statuses.append(None)
    else:
        statuses.append(status)

    # Size
    size = random.randint(50,59)
    sizes.append(size)

    # Brand
    brand = random.choice(correct_brands)
    brands.append(brand)

    # Price
    price = np.random.normal(loc=250, scale=45)
    price_str = f"{price:.2f}"
    prices.append(price_str)


    # DOB
    days_after = random.randint(0, max_days_after_first)
    purchase_date = first_purchase + datetime.timedelta(days=days_after)
    purchase_dates.append(purchase_date)

con = db.connect(output_filename)
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS bike")
cur.execute("CREATE TABLE bike (bike_id int PRIMARY KEY, brand text, size int, purchase_price real, purchase_date date, status text) ");
for i in range(len(bike_ids)):
    cur.execute("INSERT INTO bike VALUES (?, ?, ?, ?, ?, ?)", (bike_ids[i], brands[i], sizes[i], prices[i], purchase_dates[i], statuses[i]));
con.commit()
con.close()