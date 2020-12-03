import numpy as np
import random
import matplotlib.pyplot as plt

#variables

numNodes = int(input("Please enter the number of nodes you'd like in the treap:"))
maxNodeValue = int(input("Please enter the maximum value of the nodes:"))
maxPriorityValue = int(input("Please enter the maximum priority you'd like the nodes to have:"))
numNodesDelete = int(input("Please enter the number of nodes to delete:"))
numNodesSearch = int(input("Please enter the number of searches to perform:"))

#generate random insertion points
f = open('treap_insertion_file.txt', 'w')

nodeList = list(range(1,maxNodeValue + 1))
priorityList = list(range(1,maxPriorityValue + 1))
random.shuffle(nodeList)
random.shuffle(priorityList)

for i in range(numNodes):
	f.write(str(nodeList[i]) + " " + str(priorityList[i]) + "\n")

#################################################################

#delete points
f = open('treap_delete_file.txt','w')

nodeList = nodeList[:numNodes]
random.shuffle(nodeList)

for i in range(numNodesDelete):
	f.write(str(nodeList[i]) + "\n")

#################################################################

#search for points
f = open('treap_search_file.txt','w')

nodeList = nodeList[numNodesDelete:]
center = len(nodeList)/2
sigma = center/3 #because extreme values are 3 SD away from mean
s = np.random.normal(center, sigma, numNodesSearch)


for i in s:
	if(i < 0):
		i = 0
	if(i >= len(nodeList)):
		i = len(nodeList) -1
	f.write(str(nodeList[int(i)]) + "\n")

# count, bins, ignored = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - center)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')
# plt.xlabel('Index')
# plt.ylabel('Frequency')
# plt.show()

