import csv 

cat = {}
with open("products.csv", encoding="utf8") as fp:
    lines = csv.DictReader(fp)
    for i in lines:
        if i['category'] not in cat:
            cat[i["category"]] = []
        cat[i["category"]].append({"name":i['name'], "price":i["price"], "available":i["available"]})

print(cat["deli"])