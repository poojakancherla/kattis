import json
import datetime
import csv
import unicodedata


filename = "yelp_academic_dataset_user.json"

with open('users.csv', 'w') as file:
    w = csv.writer(file)
    w.writerow(["user_id", "year", "num_friends", "votes", "num_reviews", "avg rating"])
    with open(filename, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            votes = data['useful'] + data['funny'] + data['cool']
            print(len(data['friends']))
            if data['review_count'] >= 30:
                w.writerow([data['user_id'], data['yelping_since'], len(data['friends']), votes, data['review_count'], data['average_stars']])
