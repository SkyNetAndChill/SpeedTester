from datetime import datetime

with open('speedbot.txt', 'r') as f:
    data = f.readlines()

today = datetime.now().strftime("%Y-%m-%d")

# if 'processed' folder not exists, create it
import os
if not os.path.exists('processed'):
    os.makedirs('processed')

folder_today = os.path.join('processed', today)

# if today folder not exists, create it
if not os.path.exists(folder_today):
    os.makedirs(folder_today)

data_all = [['timestamp ', 'download speed [Mbit/sec] ', 'temperature [°C] ', 'humidity [%] ']]
data_basic = [['timestamp ', 'download speed [Mbit/sec] ']]
data_basic_1 = [['timestamp ', 'download speed [Mbit/sec] ']]

for l, line in enumerate(data):
    line = line.strip().replace('*', '')
    if line:
        try:
            dt, dl, temp, hum = line.split(',')
        except:
            dt, dl = line.split(',')
            temp = ''
            hum = ''
        # dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f%z')
        # dl = float(dl)
        # temp = float(temp)
        # hum = float(hum)
        data_all.append([dt, dl, temp, hum])
        data_basic.append([dt, dl])
        if l < 10000:
            data_basic_1.append([dt, dl])


with open(os.path.join(folder_today, f'speedbot_all_{today}.csv'), 'w', encoding='utf8') as f:
    for line in data_all:
        f.write(','.join(map(str, line)) + '\n')

with open(os.path.join(folder_today, f'speedbot_basic_{today}.csv'), 'w', encoding='utf8') as f:
    for line in data_basic:
        f.write(','.join(map(str, line)) + '\n')

with open(os.path.join(folder_today, f'speedbot_basic_1_{today}.csv'), 'w', encoding='utf8') as f:
    for line in data_basic_1:
        f.write(','.join(map(str, line)) + '\n')
