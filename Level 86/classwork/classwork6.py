# Codewars 7 kyu: Simple Fun #74: Growing Plant

def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = upSpeed
    while (height < desiredHeight):
        height += upSpeed - downSpeed
        days += 1
    return days;