# A python program to add time
def add_time(current_time, time_amount, day="Day"):
    # Getting all useful part of the time and timme to be added
    day_number = 0
    current_time_split = current_time.split(" ")
    meridian = current_time_split[1].upper()
    current_time_now = current_time_split[0].split(":")
    current_hour = int(current_time_now[0])
    current_minutes = int(current_time_now[1])
    time_amount_split = time_amount.split(":")
    time_amount_hour = int(time_amount_split[0])
    time_amount_minute = int(time_amount_split[1])
    # Checking which meridian is given
    if meridian == "AM":
        current_hour = current_hour
    elif meridian == "PM":
        current_hour = current_hour + 12
    else:
        print("Error: Check invalid type of meridian")
        exit()
    # Turning the 12 hours format to 24 hours format
    if current_minutes + time_amount_minute >= 60:
        current_hour += 1
        current_minutes = current_minutes + time_amount_minute - 60
        if current_minutes < 10:
            current_minutes = "0" + str(current_minutes)
    else:
        current_minutes = current_minutes + time_amount_minute
    # Calculating the time.
    current_hour = current_hour + time_amount_hour
    day_number = current_hour//24
    remaining_hour = current_hour%24
    # Converting the time back to 12 hours format.
    if remaining_hour == 12:
        meridian = "PM"
        current_hour = remaining_hour
    elif remaining_hour == 0:
        meridian = "AM"
        current_hour = "00"
    elif  remaining_hour >= 12:
        meridian = "PM"
        current_hour = remaining_hour - 12
    else:
        meridian = "AM"
        current_hour = remaining_hour
    hour = current_hour
    if day_number == 1:
        next_day = "(next day)"
    elif day_number > 1:
        next_day = "(next {} days)".format(day_number)
    else: 
        next_day = ""
    minutes = current_minutes
    # Selection of day from days of the week.
    days = [ "Sunday", "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday"]
    if day != "Day":
        day = day.capitalize()
        try:
            index = days.index(day)
        except ValueError:
            print("Error: Day inputed not part of days in the week")
            exit()
        else:
            new_day = days[index + day_number]
    else:
        new_day = ""
    if new_day != "":
        display_time= str(hour) + ":" + str(minutes) + " " + meridian + " " + new_day + next_day
    else:
        display_time= str(hour) + ":" + str(minutes) + " " + meridian + next_day
    print(display_time)

add_time("11:30 AM", "2:32", "MondAY")