import json
details = {"totalCrowd": 5, "totalCount" : 10}
details = json.dumps(details)
x = json.loads(details)

print(type(x))
