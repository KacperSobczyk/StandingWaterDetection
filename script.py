import pandas as pd
import numpy as np
import datetime
import random



def set_season(image_date):
    if (image_date.month in [4, 5] or
        (image_date.month == 6 and image_date.day < 22) or
        (image_date.month == 3 and image_date.day >= 21)) :
        return 1
    if (image_date.month in [7, 8] or
        (image_date.month == 9 and image_date.day < 23) or
        (image_date.month == 6 and image_date.day >= 22)) :
        return 2
    if (image_date.month in [10, 11] or
        (image_date.month == 12 and image_date.day < 22) or
        (image_date.month == 9 and image_date.day >= 23)) :
        return 3
    if (image_date.month in [1, 2] or
        (image_date.month == 3 and image_date.day < 21) or
        (image_date.month == 12 and image_date.day >= 22)) :
        return 4

start_time = datetime.date(2021, 1, 1)
end_time = datetime.date(2021, 12, 31)
min_temperature = 18.0
max_temperature = 30.0
min_humidity = 95.0
max_humidity = 100.0
min_rainfall = 25.0
max_rainfall = 40.0

datasets = []
dates = []
for i in range(20):
    while True:
        date_range = pd.date_range(start=start_time, end=end_time)
        random_date = np.random.choice(date_range)
        random_date = datetime.datetime.utcfromtimestamp(random_date.astype(int) * 1e-9).date()
        season = set_season(random_date)
        if season != 2:
            continue
        template_dict = {
            'area_id': None,
            'month': None,
            'season': None,
            'day_id': None,
            'temperature': None,
            'humidity': None,
            'rainfall': None,
        }
        template_dict['month'] = random_date.month
        template_dict['season'] = season
        template_dict['day_id'] = (random_date - datetime.date(2021,1,1)).days + 1
        template_dict['temperature'] = round(random.uniform(min_temperature, max_temperature),3)
        template_dict['humidity'] = round(random.uniform(min_humidity, max_humidity),3)
        template_dict['rainfall'] = round(random.uniform(min_rainfall, max_rainfall),3)
        if template_dict['day_id'] in dates:
            continue
        dates.append(template_dict['day_id'])
        for j in range(1,20):
            template_dict['area_id'] = j
            datasets.append(template_dict.copy())
            print(template_dict)
        break
df = pd.DataFrame(datasets)
df.to_csv('data_summer_high.csv', index=False)