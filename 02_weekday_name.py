def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    DAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    #input is a day of the week between 1 and 7 but list is 0 - 6
    #subtract 1 from day of week then return list at that number
    #at the start filter for out of range numbers
    if day_of_week < 1 or day_of_week > 7:
        return None

    return DAYS[day_of_week - 1]