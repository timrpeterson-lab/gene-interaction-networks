


import MySQLdb


from collections import Counter
#from collections import defaultdict


host     = '127.0.01' 
user     = 'root' 
password = '' 
database = 'morpheome' 

# Open database connection
db = MySQLdb.connect(host,user,password,database )

# prepare a cursor object using cursor() method
#cursor = db.cursor()
cursor = db.cursor(MySQLdb.cursors.DictCursor)
# execute SQL query using execute() method.
cursor.execute("SELECT pmid,abstract FROM publications WHERE match(abstract) against('"physically interacts"' IN BOOLEAN MODE)` ")

# Fetch a single row using fetchone() method.
results = cursor.fetchall()

print len(results)

genes = {}

for row in results:

  name = row['gene']

  status = row['Status']
  #list_of_genes.append(name)
  #urls = defaultdict(int)

  #genes = [{"": key, "nbr": value} for key, value in Counter(list_of_genes).items()]
  
  '''  for gene in genes:
    urls[gene] += 1'''

  #genes[name][status] = 1

  if name in genes:

    gene = genes[name]

    if status in genes[name]:
        genes[name][status]+= 1
    else:
        genes[name][status] = 1

  else:

    genes[name] = {}
    genes[name][status] = 1


print len(genes)

for g in genes.keys():
  
  #print (g)


  for y in genes[g]:
    if y == 'Control' and genes[g][y] > 0:
      del genes[g]


print len(genes)

counter = 0
for g in genes:
  for y, value in genes[g].iteritems():
    counter += value

num_human_genes = 20000
c = float(counter)/float(num_human_genes)
print "% of random gene variants scoring as Cases with atypical fractures: ", c

threshold_num = 10
cursor.execute("SELECT * from `alendronate_crispri_tau_ranked` where name not like '''%pseudo_%''' and id < " + str(threshold_num + 1))

# Fetch a single row using fetchone() method.
results2 = cursor.fetchall()

genes2 = {}

counter2 = 0
for row2 in results2:

  name2 = row2['name']
  if name2 in genes:
    for y, value in genes[name2].iteritems():
      counter2 += value    
    
c2 = float(counter2)/float(threshold_num)
print "% of CRISPRI-Alendronate gene hit variants scoring as Cases with atypical fractures:: ", c2

cursor.close
db.close()


