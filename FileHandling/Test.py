# import json
# from math import pi, sin, cos, sqrt, asin
#
#
# def find_dist(latlng_1, latlng_2):
#     """
#     This function calculate distanse in km between two point on Earth
#     whose coordinates are passed as two lists and returns rounded distanse
#     """
#     lat1, lon1 = latlng_1[0] * pi / 180, latlng_1[1] * pi / 180
#     lat2, lon2 = latlng_2[0] * pi / 180, latlng_2[1] * pi / 180
#     d = 2 * 6371 * asin(sqrt(sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2))
#     return round(d, 2)
#
#
# file = "new1.json"
#
# limit = 28875
#
# with open(file, 'rb') as f:
#     contries = json.load(f)
# first_20 = {}
# for contry in contries:
#     if contry['population'] >= limit:
#         first_20[contry['alpha3Code']] = contry['latlng']
#         if len(first_20) == 20:
#             break
#
# total_dist = 0
# keys = list(first_20.keys())
# for i in range(len(keys) - 1):
#     for j in range(len(keys[i + 1:])):
#         total_dist += find_dist(first_20[keys[i]], first_20[keys[j]])
# total_dist = round(total_dist, 2)
#
# print(total_dist)

import json
from math import radians, sin, cos, sqrt, asin


def find_dist(latlng_1, latlng_2):
    # print(latlng_1[0],latlng_1[1])
    lat1, lon1 = radians(latlng_1[0][0]), radians(latlng_1[0][1])
    lat2, lon2 = radians(latlng_2[0][0]), radians(latlng_2[0][1])
    d = 2 * 6371 * asin(sqrt(sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2))

    return round(d, 2)


file = "new1.json"

limit = 28875

with open(file, 'rb') as f:
    contries = json.load(f)
first_20 = {}
for contry in contries:
    if contry['population'] >= limit and len(contry['currencies']) > 1:
        first_20[contry['alpha3Code']] = []
        first_20[contry['alpha3Code']].append(contry['latlng'])
        first_20[contry['alpha3Code']].append(contry['population'])

first_20 = dict(sorted(first_20.items(), key=lambda x: x[1][1])[:20])

total_dist = 0
keys = list(first_20.keys())
# print(keys)
N = len(keys)
for i in range(N):
    for j in range(i + 1, N):
        total_dist += find_dist(first_20[keys[i]], first_20[keys[j]])
total_dist = round(total_dist, 2)

print(total_dist)
