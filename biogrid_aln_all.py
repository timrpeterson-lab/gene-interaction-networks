
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


'''tau_A = []

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
print("avg: " + str(tau_A_avg))'''

#tau
#avg: 0.0775684772843
# abs avg: avg: 0.0510719601067
# abs - 1 avg: 0.051074405145
#end = timer()

#rho
# abs - 1 avg: 0.0580234619271

#quit()

tau_A_diff_high = []
tau_A_diff_low = []

csv_file = '/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/interaction_networks/bio-testing-10-30-17-Biogrid-scores-ALN-crispri-rho-tau.csv'


with open(csv_file) as f:
	reader = csv.DictReader(f)
	for row in reader:

		score = float(row['Score'])

		if score > 0.834:
			try:
				#tau_A_diff.append(abs(abs(float(row['a_tau_pheno'])) - abs(float(row['b_tau_pheno']))))
				tau_A_diff_high.append(abs(abs(float(row['a_rho_pheno'])) - abs(float(row['b_rho_pheno']))))
			except ValueError:
				pass
		else:

			try:
				#tau_A_diff.append(abs(abs(float(row['a_tau_pheno'])) - abs(float(row['b_tau_pheno']))))
				tau_A_diff_low.append(abs(abs(float(row['a_rho_pheno'])) - abs(float(row['b_rho_pheno']))))
			except ValueError:
				pass


tau_high_avg = np.average(tau_A_diff_high)
tau_low_avg = np.average(tau_A_diff_low)

a = tau_A_diff_high
b = tau_A_diff_low

import scipy.stats as stats

#print(tau_A_diff_high)
#print("len diff: " + str(len(tau_A_diff)))
#print("diff: " + str(tau_A_diff))
print("avg high ppi: " + str(tau_high_avg))
print("avg low ppi: " + str(tau_low_avg))

# Use scipy.stats.ttest_ind.
t, p = stats.ttest_ind(a, b, equal_var=False)
print("ttest_ind:")

print(t)
print(p)

'''
ComPASS > 0.99
avg high ppi: 0.064667924834
avg low ppi: 0.069506651597
ttest_ind:
-5.20977856712
1.90193907819e-07

ComPASS > 0.98
avg high ppi: 0.0649722791229
avg low ppi: 0.0698375674262
ttest_ind:
-5.10100869539
3.39944652212e-07

ComPASS > 0.95
avg high ppi: 0.0660323313883
avg low ppi: 0.0693437990434
ttest_ind:
-3.20898080351
0.00133415973008

ComPASS > 0.9
avg high ppi: 0.0664396160918
avg low ppi: 0.0695763729642
ttest_ind:
-2.5833909478
0.00979634427532

ComPASS > 0.85
avg high ppi: 0.0666754155538
avg low ppi: 0.0700621748481
ttest_ind:
-2.24109810315
0.0250578407052

ComPASS > 0.84
avg high ppi: 0.0666443363012
avg low ppi: 0.0707401836801
ttest_ind:
-2.5198383291
0.0117724931014

ComPASS > 0.835
avg high ppi: 0.0666569686126
avg low ppi: 0.0708979168681
ttest_ind:
-2.50947723384
0.0121256491217

ComPASS > 0.834
avg high ppi: 0.0667068894413
avg low ppi: 0.0705574495042
ttest_ind:
-2.27205814165
0.023130354542

ComPASS > 0.8325
avg high ppi: 0.0668370345227
avg low ppi: 0.0695845494627
ttest_ind:
-1.62286636049
0.104689960905

ComPASS > 0.83
avg high ppi: 0.0668334486953
avg low ppi: 0.0696908032746
ttest_ind:
-1.67114342226
0.094767060441

ComPASS > 0.825
avg high ppi: 0.0668948207033
avg low ppi: 0.0693402877233
ttest_ind:
-1.38650713091
0.165670912624

ComPASS > 0.8
avg high ppi: 0.0670781499172
avg low ppi: 0.068030554275
ttest_ind:
-0.47151525332
0.637315189016

'''

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

