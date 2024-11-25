import json
with open("output.txt", "a") as g:
    with open("eval_predictions.jsonl") as f:
        eval_output =  f.readlines()
        for val in eval_output:
            temp_val = json.loads(val)
            if temp_val["label"] != temp_val["predicted_label"]:
                g.write(str(temp_val))
                g.write("\n")