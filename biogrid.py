import csv

names=[]
ages=[]
with open('/Users/timrpeterson/Downloads/BIOGRID-ALL-3.4.153.tab2.csv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')
    for name,age in reader:
        names.append(name)
        ages.append(age) 

print(names)
# ('Mark', 'Matt', 'John', 'Jason', 'Matt', 'Frank', 'Frank', 'Frank', 'Frank')
print(ages)
# ('32', '29', '67', '45', '12', '11', '34', '65', '78')


#/Users/timrpeterson/OneDrive\ -\ Washington\ University\ in\ St.\ Louis/Data/MORPHEOME/interaction_networks/morpheome-10-16-17-interacts_with.csv