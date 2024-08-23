'''
Description:

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
'''


# My solution

def make_readable(seconds):
    
    minutes = int(seconds/60)
    
    seconds = seconds - minutes*60
    
    hours = int(minutes/60)
    
    minutes = minutes - hours*60
    
    time = [hours, minutes, seconds]
    
    for i in range(len(time)):
        if time[i] < 10:
            time[i] = '0' + str(time[i])


''' Good solution

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def make_readable(seconds):
    return f"{seconds // 3600:02}:{(seconds % 3600) // 60:02}:{seconds % 60:02}"
'''
