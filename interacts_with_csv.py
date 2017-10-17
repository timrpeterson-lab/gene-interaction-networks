import csv

abstracts=[]
pmids=[]

names = []
ids = []
with open('/Users/timrpeterson/Desktop/morpheome-10-16-17-aliases.csv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f)
    for name in reader:
    	names.append(name[1].lower())
    	ids.append(name[3].lower())

#print(names)
pairs = []
with open('/Users/timrpeterson/Desktop/morpheome-10-16-17-interacts_with.csv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f)
    for abstract in reader:
    	words = abstract[1].partition("physically interacts with")
    	before = words[0].split()
    	after = words[2].split()

    	if len(before) >= 1:
    		before = words[0].split()[-1].lower()
    		#print("before" + before)

	    	if len(after) >= 1:
	    		after = words[2].split()[0].lower()
	    		#print("after" + after)

	    		#before = "ALIEN"
		    	if before in names:
		    		#after = "cbp"
		    		before_i = names.index(before)
		    		if after in names:
		    			after_i = names.index(after)
		    			pairs.append([before_i,after_i])

		#break

with open('pubmed-interactions-ids.csv','wb') as file:
    for line in pairs:
        file.write(str(line[0])+","+str(line[1]))
        file.write('\n')


#print(pairs)

