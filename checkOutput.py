import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def count(c):
	if c.size < 2:
		return 0
	else:
		return c[True]*100
def addBalanced(c):
	c['balanced'] = [True if x >= -1 and x <= 1 else False for x in c['balance']]

searchdf = pd.read_csv('treap_search_file.txt')
insertionData = pd.read_csv('insertion_output.txt')
deletionData = pd.read_csv('deletion_output.txt')
finalData = pd.read_csv('final_output.txt')
nSearchData = pd.read_csv('n_search_output.txt')
npSearchData = pd.read_csv('np_search_output.txt')
psSearchData = pd.read_csv('ps_search_output.txt')
pspSearchData = pd.read_csv('psp_search_output.txt')
addBalanced(insertionData)
addBalanced(deletionData)
addBalanced(nSearchData)
addBalanced(npSearchData)
addBalanced(psSearchData)
addBalanced(pspSearchData)

#number of rotations
print("Number of Rotations:")
print("        Insertion Total: " + str(insertionData['num_rotations'].sum()))
print("        Insertion Average: " + str(insertionData['num_rotations'].mean()))
print("        Deletion Total: " + str(deletionData['num_rotations'].sum()))
print("        Deletion Average: " + str(deletionData['num_rotations'].mean()))
print("        New Priority Search Total: " + str(npSearchData['num_rotations'].sum()))
print("        New Priority Search Average: " + str(npSearchData['num_rotations'].mean()))
print("        Swap Parent Search Total: " + str(psSearchData['num_rotations'].sum()))
print("        Swap Parent Search Average: " + str(psSearchData['num_rotations'].mean()))
print("        Swap Parent with Probability Search Total: " + str(pspSearchData['num_rotations'].sum()))
print("        Swap Parent with Probability Search Average: " + str(pspSearchData['num_rotations'].mean()))

#operation times
print("Operation Times:")
print("        Insertion Total: " + str(insertionData['time'].sum()))
print("        Insertion Average: " + str(insertionData['time'].mean()))
print("        Deletion Total: " + str(deletionData['time'].sum()))
print("        Deletion Average: " + str(deletionData['time'].mean()))
print("        Normal Search Total: " + str(nSearchData['time'].sum()))
print("        Normal Search Average: " + str(nSearchData['time'].mean()))
print("        New Priority Search Total: " + str(npSearchData['time'].sum()))
print("        New Priority Search Average: " + str(npSearchData['time'].mean()))
print("        Swap Parent Search Total: " + str(psSearchData['time'].sum()))
print("        Swap Parent Search Average: " + str(psSearchData['time'].mean()))
print("        Swap Parent with Probability Search Total: " + str(pspSearchData['time'].sum()))
print("        Swap Parent with Probability Search Average: " + str(pspSearchData['time'].mean()))

#Balance Factors
print("Balance Factors:")
print("        Insertion Average: " + str(insertionData['balance'].mean()))
print("        Insertion Balance %: " + str(count(insertionData['balanced'].value_counts(normalize = True))))
print("        Deletion Average: " + str(deletionData['balance'].mean()))
print("        Deletion Balance %: " + str(count(deletionData['balanced'].value_counts(normalize = True))))
print("        Normal Search Average: " + str(nSearchData['balance'].mean()))
print("        Normal Search Balance %: " + str(count(nSearchData['balanced'].value_counts(normalize = True))))
print("        New Priority Search Average: " + str(npSearchData['balance'].mean()))
print("        New Priority Search Balance %: " + str(count(npSearchData['balanced'].value_counts(normalize = True))))
print("        Swap Parent Search Average: " + str(psSearchData['balance'].mean()))
print("        Swap Parent Search Balance %: " + str(count(psSearchData['balanced'].value_counts(normalize = True))))
print("        Swap Parent with Probability Search Average: " + str(pspSearchData['balance'].mean()))
print("        Swap Parent with Probability Search Balance %: " + str(count(pspSearchData['balanced'].value_counts(normalize = True))))

#Treap Heights
print("Treap Heights:")
print("        Insertion Average: " + str(insertionData['height'].mean()))
print("        Deletion Average: " + str(deletionData['height'].mean()))
print("        Normal Search Average: " + str(nSearchData['height'].mean()))
print("        New Priority Search Average: " + str(npSearchData['height'].mean()))
print("        Swap Parent Search Average: " + str(psSearchData['height'].mean()))
print("        Swap Parent with Probability Search Average: " + str(pspSearchData['height'].mean()))

#Seach Value Frequencies
s = searchdf.value_counts()

print("Ending level for most common item " + str(s.idxmax()))
print(finalData.loc[finalData['value'] == s.idxmax(), ["treap_type", "level(s)"]])

n = 0
np = 0
ps = 0
psp = 0
index = 1
for items in s.iteritems():
	val = items[0]
	data = finalData.loc[finalData['value'] == val, ["treap_type", "level(s)"]]
	nData = int((data.loc[data['treap_type'] == "n"]).iloc[0][1])
	npData = int((data.loc[data['treap_type'] == "np"]).iloc[0][1])
	psData = int((data.loc[data['treap_type'] == "ps"]).iloc[0][1])
	pspData = int((data.loc[data['treap_type'] == "psp"]).iloc[0][1])
	if nData == index:
		n+=1
	if npData == index:
		np+=1
	if psData == index:
		ps+=1
	if pspData == index:
		psp+=1
	index += 1
	
print("Normal Search Common Accuracy: " + str(float(n/s.size)))
print("New Priority Search Common Accuracy: " + str(float(np/s.size)))
print("Parent Swap Search Common Accuracy: " + str(float(ps/s.size)))
print("Parent Swap with Probability Search Common Accuracy: " + str(float(psp/s.size)))

# f = open('output.txt', 'r')
# for l in f:
# 	if len(l.split(',')) != 14:
# 		print("Uh-oh " + l)

fig, ax = plt.subplots()
labels = ["D","I", "NP","PS","PSP"]
left = [deletionData['num_left_rotations'].sum(), insertionData['num_left_rotations'].sum(),  npSearchData['num_left_rotations'].sum(), psSearchData['num_left_rotations'].sum(), pspSearchData['num_left_rotations'].sum()]
right = [deletionData['num_right_rotations'].sum(), insertionData['num_right_rotations'].sum(),  npSearchData['num_right_rotations'].sum(), psSearchData['num_right_rotations'].sum(), pspSearchData['num_right_rotations'].sum()]
ax.bar(labels, left, 0.35, label = "Left")
ax.bar(labels, right, 0.35, bottom = left, label = "Right")
ax.set_ylabel("Number of Rotations")
ax.set_title("Left vs Right Rotations")
ax.legend()
plt.show()


fig, ax = plt.subplots()
labels = ["D","I", "N", "NP","PS","PSP"]
left = [deletionData['time'].mean(), insertionData['time'].mean(), nSearchData['time'].mean(), npSearchData['time'].mean(), psSearchData['time'].mean(), pspSearchData['time'].mean()]
ax.bar(labels, left, 0.35, label = "Left")
ax.set_ylabel("Time")
ax.set_title("Operation Time")
plt.show()