import re
from prettytable import PrettyTable
with open('wearher_json.json', 'r') as f:
    data = f.read()
temp =re.search(r'"temp":\s*(\d+\.\d+)', data).group(1)
feels_like =re.search(r'"feels_like":\s*(\d+\.*\d+)', data).group(1)
pressure =re.search(r'"pressure":\s*(\d+\.*\d+)', data).group(1)
hum =re.search(r'"humidity":\s*(\d+\.*\d+)', data).group(1)
t = PrettyTable(['City', 'Alexandria'])
t.add_row(['Temperature K', temp])
t.add_row(['Feels like C', (float(feels_like) - 273)])
t.add_row(['Pressure', pressure])
t.add_row(['Humidity', hum])
with open('weather_data.txt', 'w') as f:
    f.write(t.get_string())


