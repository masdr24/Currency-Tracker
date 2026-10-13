import datetime

x = datetime.datetime.now()
print(x.minute)
c = float(f"{x.year}{x.month:02d}{x.day:02d}.{x.hour:02d}{x.minute:02d}{x.second:02d}")
print(c)
