import re
from prettytable import PrettyTable
with open('wearher_json.json', 'r') as f:
    data = f.read()
temp =re.search(r'"temp":\s*(\d+\.\d+)', data).group(1)
feels_like =re.search(r'"feels_like":\s*(\d+\.\d+)', data).group(1)
pressure =re.search(r'"pressure":\s*(\d+\.*\d+)', data).group(1)
hum =re.search(r'"humidity":\s*(\d+\.*\d+)', data).group(1)
t = PrettyTable(['City', 'Alexandria'])
t.add_row(['temprature', temp])
t.add_row(['feels_like', feels_like])
t.add_row(['pressure', pressure])
t.add_row(['humidity', hum])
with open('wearher_data.txt', 'w') as f:
    f.write(t.get_string())


