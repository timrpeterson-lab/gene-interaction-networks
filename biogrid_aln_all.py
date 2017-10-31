
import MySQLdb
import time
import csv
import numpy as np
from timeit import default_timer as timer

from collections import Counter
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list


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
cursor.execute('SELECT `Official Symbol Interactor A` as gene_A, `Official Symbol Interactor B` as gene_B, Score from `bio-testing`.Biogrid where `Pubmed ID` = "28514442" ; ') #and `Score` > 0.98


results = cursor.fetchall()
results_biogrid = results

cursor.close
db.close()


database = 'crispri' 

# Open database connection
db = MySQLdb.connect(host,user,password,database )

# prepare a cursor object using cursor() method
#cursor = db.cursor()
cursor = db.cursor(MySQLdb.cursors.DictCursor)

#cursor.execute('SELECT gene, `t avg3 average phenotype of strongest 3` as tau from `crispri`.aln where gene not like "%pseudo_%"; ')
cursor.execute('SELECT gene, `r avg3 average phenotype of strongest 3` as tau from `crispri`.aln where gene not like "%pseudo_%"; ')


results_ALN = cursor.fetchall()

cursor.close
db.close()



#start = time.time()
print("hello")

#start = timer()
# ...

#print(end - start) 


tau_A = []

for row_ALN in results_ALN:
	try:
	    t = float(row_ALN['tau'])
	    tau_A.append(t)
	except ValueError:
	    pass	
	
l = tau_A

len_l1 = len(l) - 1

tau_A_diff = [sum(abs(abs(i)-abs(j)) for j in l if j!=i)/len_l1 for i in l]

tau_A_avg = np.average(tau_A_diff)

#print("len diff: " + str(len(tau_A_diff)))
#print("diff: " + str(tau_A_diff))
print("avg: " + str(tau_A_avg))

#tau
#avg: 0.0775684772843
# abs avg: avg: 0.0510719601067
# abs - 1 avg: 0.051074405145
#end = timer()

#rho
# abs - 1 avg: 0.0580234619271

quit()

tau_A_diff = []

csv_file = '/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/interaction_networks/bio-testing-10-30-17-Biogrid-scores-ALN-crispri-rho-tau.csv'


with open(csv_file) as f:
	reader = csv.DictReader(f)
	for row in reader:

		#if float(row['Score']) < 0.98:
			#continue

		try:
			#tau_A_diff.append(abs(abs(float(row['a_tau_pheno'])) - abs(float(row['b_tau_pheno']))))
			tau_A_diff.append(abs(abs(float(row['a_rho_pheno'])) - abs(float(row['b_rho_pheno']))))
		except ValueError:
			pass


tau_A_avg = np.average(tau_A_diff)

print(tau_A_diff)
#print("len diff: " + str(len(tau_A_diff)))
#print("diff: " + str(tau_A_diff))
print("avg ppi: " + str(tau_A_avg))

#tau
# avg ppi: 0.0868121328243
# avg abs ppi: 0.0587519493237
# avg abs, Score > 0.95 ppi: 0.05807410137
# avg abs, Score > 0.98 ppi: 0.0573491512837

#rho
#avg abs ppi: 0.0671395057277

'''len diff: 1034
avg: 2.58123791103'''


'''avg: 1620.32792199
29357.5124741

avg: 1620.32792199
30135.3608131'''


'''list_a = [1,2,3,4]

el1 = 1+2+3 = 6
el2 = 1+1+2 = 4
el3 = 2+1+1 = 4
el4 = 3+2+1 = 6
avg = 5

list_b = [1,2,3,6]

el1 = 5+4+3 = 12
el2 = 1+1+4 = 6
el3 = 2+1+3 = 6
el4 = 5+4+3 = 12
avg = 9'''


#print(numpy.diff(tau_A))
'''print(len(tau_A))
quit()

for row_ALN in results_ALN:
	tau_A = row_ALN['tau']


	for row_ALN2 in results_ALN:
		tau_B = row_ALN['tau']

		tau_diff = float(tau_A) - float(tau_B)

		output.append(tau_diff)

		end = time.time()
		end = timer()'''
		#print( (end - start)  )
		
		#quit()
'''	if gene == gene_A:
		tau_A = row_ALN['tau']
	elif gene == gene_B:
		tau_B = row_ALN['tau']

for row in results:
	gene_A = row['gene_A'].lower()
	gene_B = row['gene_B'].lower()	



	output2.append([gene_A, tau_A, gene_B, tau_B])

print(output2)'''
#quit()


'''
print ("mean is: ")
print(output)
print(numpy.mean(output))

quit()

print('done3')'''
#print(output2)

'''with open('biogrid-tau-ppi2.csv','wb') as file:
    for line in output2:
        file.write(str(line[0])+","+str(line[1])+","+str(line[2])+","+str(line[3]))
        file.write('\n')'''

