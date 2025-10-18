import requests

def get_drivers() -> dict[str, list[str | list[int]]]:
    response = requests.get("https://f1api.dev/api/current/drivers")
    data = response.json()["drivers"]
    drivers = {}
    for driver in data:
        drivers[driver["driverId"]] = [driver["shortName"], []]
    return drivers

def get_last_race() -> list[str]:
    response = requests.get("https://f1api.dev/api/current/last")
    data = response.json()["race"][0]
    return [data["championshipId"], str(data["round"])]

def get_race_results(championship_id: str, round: str, driver_id: str) -> int:
    year = championship_id[-4:]
    response = requests.get(f"https://f1api.dev/api/{year}/{round}/race")
    data = response.json()["races"]["results"]
    for result in data:
        if result["driver"]["driverId"] == driver_id:
            return result["points"]
    return -1

def main():
    print("Hello from formulagraph!")
    lastRace: list[str] = get_last_race()
    print(get_race_results(lastRace[0], str(int(lastRace[1]) - 1), "sainz"))


if __name__ == "__main__":
    main()
