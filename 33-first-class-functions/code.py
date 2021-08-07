def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
        raise RuntimeError (f"Could not find a element with {expected}.")


friends = [
    {"name" : "Rolf Smith", "Age": 24},
    {"name" : "Adam Sandler", "Age": 30},
    {"name" : "Anne H", "Age": 28},
]

print(search(friends, "Rolf Smith", lambda friend: friend["name"]))