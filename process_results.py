from datetime import datetime

with open('speedbot.txt', 'r') as f:
    data = f.readlines()

data_all = [['timestamp ', 'download speed [Mbit/sec] ', 'temperature [°C] ', 'humidity [%] ']]
data_basic = [['timestamp ', 'download speed [Mbit/sec] ']]

for line in data:
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

with open(f'speedbot_all_{datetime.now().strftime("%Y-%m-%d")}.csv', 'w', encoding='utf8') as f:
    for line in data_all:
        f.write(','.join(map(str, line)) + '\n')

with open(f'speedbot_basic_{datetime.now().strftime("%Y-%m-%d")}.csv', 'w', encoding='utf8') as f:
    for line in data_basic:
        f.write(','.join(map(str, line)) + '\n')
