
def add_time(input_time, duration, day=None):
    # Store the weekdays in a dict with corresponding numbers.
    weekdays_number = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
    weekdays_name = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    # splitting input to get hours, minutes and clock format
    input_time = input_time.split(" ")
    clock_format = input_time[1]
    start_time = input_time[0].split(":")
    duration = duration.split(":")

    input_h = int(start_time[0]) + int(duration[0])
    input_m = int(start_time[1]) + int(duration[1])

    if clock_format == "PM":
        input_h += 12

    # converts minutes in hours
    m_to_h = 0
    while input_m >= 60:
        input_m = input_m % 60
        m_to_h += 1
    input_h += m_to_h  # adding converted hours

    # converts hours in days
    day_count = 0
    while input_h >= 24:
        input_h -= 24
        day_count += 1

    if input_h in range(0, 11):
      if input_h == 0:
        input_h = 12
      clock_format = "AM"
    elif input_h in range(12, 24):
        if input_h != 12:
          input_h -= 12
        clock_format = "PM"


    input_m = format(input_m, "02d")  # formatting 1 to 01

    if day is None and day_count == 0:
        return f"{input_h}:{input_m} {clock_format}"
    elif day is not None and day_count == 0:
        current_day_number = weekdays_number[day.lower()]
        return f"{input_h}:{input_m} {clock_format}, {weekdays_name[current_day_number+ day_count]}"
    elif day is None and day_count == 1:
        return f"{input_h}:{input_m} {clock_format} (next day)"
    elif day is not None and day_count == 1:
        current_day_number = weekdays_number[day.lower()]
        return f"{input_h}:{input_m} {clock_format}, {weekdays_name[current_day_number+ day_count]} (next day)"
    elif day is not None and day_count >= 1:
        current_day_number = weekdays_number[day.lower()]
        return f"{input_h}:{input_m} {clock_format}, {weekdays_name[(current_day_number + day_count) % 7]} ({day_count} days later)"
    elif day is None and day_count >= 1:
        return f"{input_h}:{input_m} {clock_format} ({day_count} days later)"