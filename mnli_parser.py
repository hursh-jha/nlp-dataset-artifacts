import json
filename = "Stress_Tests/Numerical_Reasoning/multinli_0.9_quant_hard.jsonl"
f = open("newfile.json", "w") 
output = []
with open(filename, "r") as file:
    for line in file:
        json_line = json.loads(line)
        correct_json_object = {}
        correct_json_object["premise"] = json_line["sentence1"]
        correct_json_object["hypothesis"] = json_line["sentence2"]
        string_val = json_line["gold_label"]
        if string_val == "entailment":
            correct_json_object["label"] = 0
        elif string_val == "neutral":
            correct_json_object["label"] = 1
        elif string_val == "contradiction":
            correct_json_object["label"] = 2
        output.append((correct_json_object))
f.write(json.dumps(output))
f.close()