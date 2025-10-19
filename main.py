import requests


def get_drivers() -> dict[str, list[str | list[int]]]:
    response: requests.Response = requests.get("https://f1api.dev/api/current/drivers")
    data = response.json()["drivers"]
    drivers: dict[str, list[str | list[int]]] = {}
    for driver in data:
        drivers[driver["driverId"]] = [driver["shortName"], []]
    return drivers


def get_last_race() -> list[str]:
    response: requests.Response = requests.get("https://f1api.dev/api/current/last")
    data = response.json()["race"][0]
    return [data["championshipId"], str(data["round"])]


def get_race_results(championship_id: str, round: str, driver_id: str) -> int:
    year: str = championship_id[-4:]
    response: requests.Response = requests.get(
        f"https://f1api.dev/api/{year}/{round}/race"
    )
    data = response.json()["races"]["results"]
    points: int = 0
    for result in data:
        if result["driver"]["driverId"] == driver_id:
            points += result["points"]

    response = requests.get(f"https://f1api.dev/api/{year}/{round}/sprint/race")
    data = response.json()["races"]["sprintRaceResults"]

    for result in data:
        if result["driver"]["driverId"] == driver_id:
            points += result["points"]

    return points


def main():
    print("Hello from formulagraph!")


if __name__ == "__main__":
    main()
