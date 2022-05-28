from collections import deque

pumps = int(input())
gas_infos = deque()

for x in range(pumps):
    station = [int(x) for x in input().split()]
    gas_infos.append(station)

for gas_station in range(len(gas_infos)):
    failed = False
    gas = 0
    for petrol, distance in gas_infos:
        gas = gas + petrol - distance
        if gas < 0:
            failed = True
            break
    if not failed:
        print(gas_station)
        break
    gas_infos.rotate(-1)

