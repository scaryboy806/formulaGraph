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

def main():
    print("Hello from formulagraph!")


if __name__ == "__main__":
    main()
