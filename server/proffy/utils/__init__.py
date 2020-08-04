def convert_to_minutes(hour_minute_str):
    hours, minutes = hour_minute_str.split(":")
    total_minutes = 60*int(hours) + int(minutes)
    return total_minutes