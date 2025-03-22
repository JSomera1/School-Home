import csv
with open('products.csv') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        print(row['name'])