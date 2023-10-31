import datetime

VEHICLE_TYPES = {
    "citadine": 8,
    "cabriolet": 6,
    "berline": 6.5,
    "suv": 4,
    "4x4": 4
}
ENERGIES = {
    "essence": 5,
    "electrique": 9,
    "gaz": 6,
    "diesel": 4,
    "hybride": 7
}
KILOMETERS = [
    (5, 10, 9),
    (10, 15, 7),
    (15, 20, 5),
    (20, 25, 3),
    (25, 30, 1)
]
YEARS = [
    (1960, 1970, 1),
    (1970, 1980, 2),
    (1980, 1990, 3),
    (1990, 2000, 4),
    (2000, 2010, 5),
    (2010, datetime.datetime.now().year, 7)
]
INTEREST_RATE = [
    (0, 10, 3),
    (11, 15, 2.74),
    (16, 25, 2.52),
    (26, 33, 2.10),
    (33, 40, 1.85)
]
PASSAGERS = {
    1: 0.11,
    2: -0.17,
    3: -0.29,
    4: -0.53
}


def get_tuple_score(value, data):
    for start, end, score in data:
        if start <= value < end:
            return score


def get_interest_rate(vehicle_type: str, energy: str, kilometer: int, year: int, passager_number: int):
    vehicle_type = vehicle_type.lower()
    energy = energy.lower()
    if vehicle_type not in VEHICLE_TYPES:
        raise ValueError(f"{vehicle_type} is not in the list of possible values ({', '.join(VEHICLE_TYPES.keys())})")
    if energy not in ENERGIES:
        raise ValueError(f"{energy} is not in the list of possible values ({', '.join(ENERGIES.keys())})")
    if not KILOMETERS[0][0] <= kilometer <= KILOMETERS[-1][1]:
        raise ValueError(f"The kilometer arg must be between {KILOMETERS[0][0]} and {KILOMETERS[-1][1]}.")
    if not YEARS[0][0] <= year <= YEARS[-1][1]:
        raise ValueError(f"The year arg must be between {YEARS[0][0]} and {YEARS[-1][1]}.")
    if passager_number not in PASSAGERS:
        raise ValueError(f"{passager_number} is not in the list of possible values ({', '.join(map(str, PASSAGERS.keys()))})")
    vehicle_score = VEHICLE_TYPES[vehicle_type] + ENERGIES[energy] + get_tuple_score(kilometer, KILOMETERS) + get_tuple_score(year, YEARS)
    return get_tuple_score(vehicle_score, INTEREST_RATE) + PASSAGERS[passager_number]


print(get_interest_rate("Citadine", "electrique", 25, 2009, 1))
