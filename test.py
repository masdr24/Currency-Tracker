import datetime

x = datetime.datetime.now()
c = float(f"{x.year}{x.month}{x.day}.{x.hour}{x.minute}{x.second}")
print(c)
