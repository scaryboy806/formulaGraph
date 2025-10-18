import requests

def get_drivers() -> dict[str, list[str | list[int]]]:
    response = requests.get("https://f1api.dev/api/current/drivers")
    data = response.json()["drivers"]
    drivers = {}
    for driver in data:
        drivers[driver["driverId"]] = [driver["shortName"], []]
    return drivers

def main():
    print("Hello from formulagraph!")


if __name__ == "__main__":
    main()
