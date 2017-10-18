


import MySQLdb


from collections import Counter
#from collections import defaultdict


host     = '127.0.01' 
user     = 'root' 
password = '' 
#database = 'bio-testing' 

# Open database connection
db = MySQLdb.connect(host,user,password,database )

# prepare a cursor object using cursor() method
#cursor = db.cursor()
cursor = db.cursor(MySQLdb.cursors.DictCursor)
# execute SQL query using execute() method.
cursor.execute('SELECT `Official Symbol Interactor A` as gene_A, `Official Symbol Interactor B` as gene_B from `bio-testing`.Biogrid where `Pubmed ID` = "28514442" and `Score` > 0.98; ')

'''select `bio-testing`.Official Symbol Interactor A`, `Official Symbol Interactor B`, p.`t avg3 average phenotype of strongest 3`  from biogrid b
join `crispri`.aln  p
on b.`Official Symbol Interactor A` = p.`gene`
or b.`Official Symbol Interactor B` = p.`gene`

where (b.`Pubmed ID` = "28514442" and b.`Score` > 0.98)'''

results = cursor.fetchall()

cursor.execute('SELECT gene, `t avg3 average phenotype of strongest 3` as tau from `crispri`.aln; ')

results_ALN = cursor.fetchall()

#print len(results)

output = []

for row in results:

  gene_A = row['gene_A']

  gene_B = row['gene_B']

	for row_ALN in results_ALN:

	  gene = row_ALN['gene']

	  tau = row_ALN['tau']

	  if gene_A = gene:
	  	tau_A = tau 

	  if gene_B = gene:
	  	tau_B = tau 	  	

	output.append[gene_A, gene_B, tau_A, tau_B]

  print(gene_A)
  break

cursor.close
db.close()


with open('biogrid-tau-ppi.csv','wb') as file:
    for line in pairs:
        file.write(str(line[0])+","+str(line[1]))
        file.write('\n')
