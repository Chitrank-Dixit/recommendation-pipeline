__author__ = 'py'

import json
import csv
# import pandas as pd

json_data = open("mpd_1.json")
jdata = json.load(json_data)
final_list = []
user_dict = {}

#creating list of look_up sheet
with open('/Users/py/Downloads/look_up - Sheet1.csv', 'r') as f:
    reader = csv.reader(f)
    look_up = list(reader)


# print(jdata["hits"]["hits"])
for each in jdata["hits"]["hits"]:
    final_list.append(each["_source"])

# Creating user-event timeseries

list1 = list()
for each in final_list:
    if each["event"] == "Details Web" or each["event"] == "Add To Cart Web":
        if each["distinct_id"] not in user_dict:
            user_dict[each["distinct_id"]] = list1
        user_dict[each["distinct_id"]] = user_dict[each["distinct_id"]] + [{each["event"]: [each["time"], each["parent_id"]]}]

user_detail_corr = {}
for user in user_dict:
    user_detail_corr[user] = []
    for each in user_dict[user]:
        for key, value in each.items():
            if key == "Details Web":
                user_detail_corr[user].append(value[1])

user_atc_corr = {}
for user in user_dict:
    user_atc_corr[user] = []
    for each in user_dict[user]:
        for key, value in each.items():
            if key == "Add To Cart Web":
                user_atc_corr[user].append(value[1])

user_detail_inv_corr = {}
for user in user_detail_corr:
    user_detail_inv_corr[user] = []
    for parent in user_detail_corr[user]:
        #get inv_cat for the item : inv_cat_item
        for item in look_up:
            if item[1] == parent:
                inv_cat_item = item[6]
                user_detail_inv_corr[user].append(inv_cat)


