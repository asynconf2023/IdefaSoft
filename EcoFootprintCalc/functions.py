def get_tuple_score(value, data):
    for start, end, score in data:
        if start <= value < end:
            return score


def calculate_interest_rate(vehicle_type: str, energy: str, kilometer: int, year: int, passager_number: int):
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