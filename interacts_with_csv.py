import csv

abstracts=[]
pmids=[]

names = []
with open('/Users/timrpeterson/Desktop/morpheome-10-16-17-aliases.csv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f)
    for name in reader:
    	names.append(name)

pairs = []
with open('/Users/timrpeterson/Desktop/morpheome-10-16-17-interacts_with.csv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f)
    for pmid,abstract in reader:
    	words = abstract.partition("interacts with")
    	before = words[0].split()[-1]
    	#print("before" + before)

    	after = words[2].split()
    	if test_list.__contains('is') == 1:
    		after = words[2].split()[0]
    	if before in names:
    		if after in names:
    			pairs.append = [before,after]



print(pairs)

