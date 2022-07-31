import csv
import pandas as pd
file1 = 'brightStars.csv'
file2 = 'unitConvertedStars.csv'
d1 = []
d2 = []
with open(file1, 'r', encoding = 'utf8') as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        d1.append(i)
with open(file2, 'r', encoding = 'utf8') as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        d2.append(i)
h1 = d1[0]
h2 = d2[0]
pD1 = d1[1:]
pD2 = d2[1:]
h = h1 + h2
pD = []
for i in pD1:
    pD.append(i)
for j in pD2:
    pD.append(j)
with open('totalStars.csv', 'w', encoding = 'utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(pD)
df = pd.read_csv('totalStars.csv')
df.tail(8)