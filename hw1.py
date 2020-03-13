# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061229.csv'
data = []
data_id = []
data_pre = []
header = []
target_data = []
index = []

with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
       # data.append(row)
        data_id.append(row['station_id'])
        data_pre.append(float(row['PRES']))
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

for i in range(len(data_pre)):
    if(data_pre[i] == -99.000 or data_pre[i] == -999.000):
        index.append(i)

index.reverse()
for i in index:
    del data_id[i]
    del data_pre[i]

while(len(data_id)):
    a = []
    item = data_id[0]
    index = [i for i, j in enumerate(data_id) if j == item]
    j = 0
    pre = 0
    for i in index:
        pre = pre + data_pre[i]
        j = j + 1
    avg = pre / j
    a.append(item)
    a.append(avg)
    data.append(a)
    index.reverse()
    for i in index:
        del data_pre[i]
        del data_id[i]

id = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']

for i in range(5):
    find = False
    for j in range(len(data)):
        if (id[i] == data[j][0]):
            target_data.append(data[j])
            find = True  
    if (find == False):
        target_data.append([id[i], 'None'])
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================