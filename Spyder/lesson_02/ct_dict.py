# key<->value对应的hash表
di = {'k1': 'v1', 'k2': 'v2'}
di['k3'] = 'v3'
di['k4'] = 'v4'

for k in di:
    print(di[k])

for k, v in di.items():
    print(k, v)
