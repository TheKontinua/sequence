import pandas as pd
import random
import datetime
import numpy as np
import sys
import math

def should_generate_error():
    return random.random() < 0.008

if len(sys.argv) < 2:
    print("Usage: python main.py <output_file>")
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

    # incident
    # age = now.date() - purchase_date
    # days_old = age.days
    # age_in_days_at_last_rental = int(np.random.normal(days_old/1.5, 1000))
    #
    #while age_in_days_at_last_rental > days_old:
    #    age_in_days_at_last_rental -= int(np.random.normal(100, 10))
    #birth_timestamp = datetime.datetime.combine(purchase_date, now.time())
    #hours = random.randrange(0,24)
    # minutes = random.randrange(0,60)
    #last_rental = birth_timestamp + datetime.timedelta(days=age_in_days_at_last_rental, hours=hours, minutes=minutes)
    #last_rented_dates.append(last_rental)

df = pd.DataFrame({'brand':brands, 'size':sizes,  'purchase_price':prices, 'purchase_date':purchase_dates, 'status': statuses}, 
index=bike_ids)

df.to_csv(output_filename, index_label = 'bike_id', line_terminator='\n', float_format='%.02f', date_format='%Y-%m-%dT%H:%MZ')








