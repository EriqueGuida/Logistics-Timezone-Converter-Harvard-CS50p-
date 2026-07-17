CITIES = {
    "new york": -5,
    "los angeles": -8,
    "brasília": -3,
    "dubai": +4,
    "shanghai": +8,
    "singapore": +8,
    "tokyo": +9,
    "sydney": +10
}


def main():
    # Receive and Validate Time
    while True:
        time = input("What time is it? ")
        result = validate_time(time)

        if result:
            hours, minutes = result
            break
        else:
            print("Invalid time format. Please use HH:MM.")

    # Receive and Validate Origin
    while True:
        origin = input("Origin City: ").lower()
        if origin in CITIES:
            break
        else:
            print("Invalid city, please try again.")

    # Receive and Validade Destination
    while True:
        destination = input("Destination City: ").lower()
        if destination in CITIES:
            break
        else:
            print("Invalid city, please try again.")

    # Convert TIme Zone
    if origin == destination:
        print ("Same time zone, no need to convert")
    else:
        hours_utc, minutes = convert_to_utc(hours, minutes, origin)
        new_hours, minutes = convert_from_utc(hours_utc, minutes, destination)

        # Print new time
        new_time = format_time(new_hours, minutes)
        print(new_time)


def validate_time(time):
    # Validates if the provided string is in HH:MM (24h) format.
    # Returns a tuple (hours, minutes) if valid, or None if invalid
    try:
        time = time.strip().split(":")

        if len(time) != 2:
            return None

        hours = int(time[0])
        minutes = int(time[1])
        if (0 <= hours <= 23) and (0 <= minutes <= 59):
            return hours, minutes
        return None
    except ValueError:
        return None


def convert_to_utc(hours, minutes, origin):
    # Converts local time to universal time (UTC)
    time_zone = CITIES[origin]
    hours_utc = (hours - time_zone) % 24
    return hours_utc, minutes


def convert_from_utc(hours_utc, minutes, destination):
    # Converts UTC time to the time of the destination city
    time_zone = CITIES[destination]
    new_hours = (hours_utc + time_zone) % 24
    return new_hours, minutes


def format_time(new_hours, minutes):
    # Returns the time formatted as a string HH:MM with zero padding
    new_time = f"{new_hours:02}:{minutes:02}"
    return new_time


if __name__ == "__main__":
    main()
