import json
# import pprint
filename = "contrast_data.json"
output = []
with open(filename, "r") as file:
    data = json.load(file)
    i = 0
    for val in data:
        newDict = val
        newDict["key"] = i
        output.append(newDict)
        i+=1
f = open(filename, "w")
# pretty_json_str = pprint.pformat(output, compact=True)
f.write(json.dumps(output))
f.close()
