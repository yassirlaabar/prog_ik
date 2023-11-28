def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    Geeft None terug als het geen tijd is voor een maaltijd.
    >>> meal("07:30")
    'ontbijt'
    >>> meal("18:45")
    'avondeten'
    >>> meal("12:01")
    'lunch'
    """
    
    try:
        hours = int(hours_str)
        minutes = int(minutes_str)
    except ValueError:
        return None
    hours, minutes = time.split(":")
    if 7 <= hours < 8 or (hours == 8 and minutes == 0):
        return "ontbijt"
    elif 12 <= hours < 13 or (hours == 13 and minutes == 0):
        return "lunch"
    elif 18 <= hours < 19 or (hours == 19 and minutes == 0):
        return "avondeten"
    else:
        return None

if __name__ == '__main__':
    user_input = input("Hoe laat is het? ")
    result = meal(user_input)

    if result is not None:
        print(f"Het is tijd voor {result}")
