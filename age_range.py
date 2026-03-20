import json

with open("clienti.json","r") as f:
    dict = json.load(f)

def age_range(cust_list:List[Dict])->Dict:
    dict = {}

"60-":list(),
"40-59":list(),
"30-39":list(),
"20-29":list(),
"18-":list()

for elem in cust_list:

    if elem["eta"] >= 60:
        dict["60-"].append(elem)
    elif elem["eta"] >= 40 and elem["eta"] < 60:
        dict["40-59"].append(elem)
    elif elem["eta"] >= 30 and elem["eta"] < 40:
        dict["30-39"].append(elem)
    elif elem["eta"] >= 20 and elem["eta"] < 30:
        dict["20-29"].append(elem)
age_range(f)
print(age_range)