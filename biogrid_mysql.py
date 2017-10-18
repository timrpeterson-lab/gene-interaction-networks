
import MySQLdb

from collections import Counter
#from collections import defaultdict


host     = '127.0.01' 
user     = 'root' 
password = '' 
database = 'bio-testing' 

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

cursor.close
db.close()


database = 'crispri' 

# Open database connection
db = MySQLdb.connect(host,user,password,database )

# prepare a cursor object using cursor() method
#cursor = db.cursor()
cursor = db.cursor(MySQLdb.cursors.DictCursor)

cursor.execute('SELECT gene, `t avg3 average phenotype of strongest 3` as tau from `crispri`.aln; ')

results_ALN = cursor.fetchall()

cursor.close
db.close()

#print len(results)
#print len(results_ALN)
print('done1')

output = [] #'gene_A', 'tau_A', 'gene_B', 'tau_B'

for row_ALN in results_ALN:

  gene = row_ALN['gene'].lower()

  tau = row_ALN['tau']

  for row in results:

  	gene_A = row['gene_A'].lower()

  	if gene_A == gene:

		gene_B = row['gene_B'].lower()	  	

		output.append([gene, tau, gene_B])

  	#break
print('done2')
#print(output)

output2 = []

for row_ALN in results_ALN:

	gene = row_ALN['gene'].lower()

	#print(gene)

	for out in output:

		#print(out[2])

		if out[2] == gene:

			#print(output2)
			out.append(row_ALN['tau'])

  			output2.append(out[:])

  			#print(out)
  			#print(output2)
  			#break
		#break
#gene tau gene_B tau_B
print('done3')
#print(output2)

with open('biogrid-tau-ppi.csv','wb') as file:
    for line in output2:
        file.write(str(line[0])+","+str(line[1])+str(line[2])+","+str(line[3]))
        file.write('\n')

