from datetime import timedelta


def get_color_of_score(waiting_time):
    green_color_max_time = 7
    red_color_max_time = 30
    green_color = "#01DF01"
    yellow_color = "#FFFF00"
    red_color = "#FF0000"
    if waiting_time <= timedelta(minutes=green_color_max_time):
        return green_color
    elif waiting_time > timedelta(minutes=red_color_max_time):
        return red_color
    else:
        return yellow_color
