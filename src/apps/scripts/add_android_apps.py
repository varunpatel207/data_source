import csv
import os

from apps.models.android_app_model import AndroidApp
from twitch.settings import BASE_DIR

file_path = os.path.join(BASE_DIR, '../', 'data', 'android-games.csv')

convert_key = {
    "rank": 'rank',
    "title": 'title',
    "total_ratings": 'total ratings',
    "installs": 'installs',
    "avg_rating": 'average rating',
    "growth_30day": 'growth (30 days)',
    "growth_60day": 'growth (60 days)',
    "price": 'price',
    "category": 'category',
    "rating_5": '5 star ratings',
    "rating_4": '4 star ratings',
    "rating_3": '3 star ratings',
    "rating_2": '2 star ratings',
    "rating_1": '1 star ratings',
    "paid": 'paid'
}

def add_android_app():
    with open(file_path) as file:
        csv_reader = csv.DictReader(file)

        android_app_object_list = []
        for row in csv_reader:
            row['paid'] = True if row['paid'] == "True" else False
            row['installs'] = row['installs'].replace("M", "").replace("k", "").strip()
            row['installs'] = float(row['installs'])
            for db_key, csv_key in convert_key.items():
                row[db_key] = row.pop(csv_key)

            android_app_object = AndroidApp(**row)
            android_app_object_list.append(android_app_object)

        AndroidApp.bulk_add(android_app_object_list)

        print(row['rank'], row['title'])

add_android_app()

print(AndroidApp.all())