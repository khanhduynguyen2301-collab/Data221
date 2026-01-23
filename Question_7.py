def time_conversion(number_of_seconds):
    if not isinstance(number_of_seconds, int):
        return "Invalid input: seconds must be an integer."

    hours_in_24 = number_of_seconds // 3600
    minutes = (number_of_seconds % 3600) // 60
    seconds = number_of_seconds % 60

    am_pm = 'AM' if hours_in_24 < 12 else 'PM'

    hours_in_12 = number_of_seconds % 12
    if hours_in_12 == 0:
        hours_in_12 = 12
    return f'{hours_in_12} {minutes} {seconds} {am_pm}'

print(time_conversion(19067))
