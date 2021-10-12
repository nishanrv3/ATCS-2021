mountains = {"Everest": 2566, "Yosemite": 1021, "Grand Canyon": 586}
for key_mountain in mountains.keys():
    print(key_mountain)
for value_mountain in mountains.values():
    print(value_mountain)

for key_mountain, value_mountain in mountains.items():
    print(key_mountain + " is " + str(value_mountain))
