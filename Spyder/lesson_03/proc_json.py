import json

obj = {'one': '一', 'two': '二'}
encoded = json.dumps(obj)
print(type(encoded))
print(encoded)
decoded = json.loads(encoded)
print(type(decoded))
print(decoded)
