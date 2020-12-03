import random
import Node as nd
import time
from tqdm import tqdm

class Treap(object): 
	def insert(self, root, key):
		global level
		# Perform normal BST 
		if not root: 
			return key
		elif key.val < root.val: 
			level+=1
			root.left = self.insert(root.left, key) 
		else: 
			level+=1
			root.right = self.insert(root.right, key) 
  
		# Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
		if root.left:
			root.left.parent = root
		if root.right:
			root.right.parent = root;
  
		# Get the balance factor 
		balance = self.getBalance(root) 
		while(root.right and root.right.priority< root.priority):
			root = self.leftRotate(root)
		while(root.left and root.left.priority < root.priority):
			root = self.rightRotate(root)
		return root 

	def delete(self, root, key): 
		global level
		if not root: 
			return root 
		elif key < root.val: 
			level += 1
			root.left = self.delete(root.left, key) 
		elif key > root.val: 
			level += 1
			root.right = self.delete(root.right, key) 
		else: 
			if root.left is None: 
				temp = root.right 
				if temp:
					temp.parent = root.parent
				root = None
				return temp 
  
			elif root.right is None: 
				temp = root.left 
				if temp:
					temp.parent = root.parent
				root = None
				return temp 

			temp = root.right
			while(temp is not None and temp.left is not None):
				temp = temp.left

			root.val = temp.val
			root.priority = temp.priority
			root.right = self.delete(root.right, 
									  temp.val) 
  
		# If the tree has only one node,  return it 
		if root is None: 
			return root 
  
		# Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
  
		# Get the balance factor 
		balance = self.getBalance(root) 
  
		# Balance heap 
		while(root.right and root.right.priority< root.priority):
			root = self.leftRotate(root)
		while(root.left and root.left.priority < root.priority):
			root = self.rightRotate(root)
  
		return root 
			
	def leftRotate(self, z): 
		global level, rotations, levels
		level-=1
		rotations.append("LR")
		levels.append(level)
		y = z.right 
		T2 = y.left 
  
		# Perform rotation 
		temp = z.parent
		y.left = z 
		z.parent = y
		z.right = T2 
		if T2:
			T2.parent = z
		y.parent = temp
  
		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
		# Return the new root 
		return y 
  
	def rightRotate(self, z): 
		global level, rotations, levels
		level-=1
		rotations.append("RR")
		levels.append(level)
		y = z.left 
		T3 = y.right 
  
		# Perform rotation 
		temp = z.parent
		y.right = z
		z.parent = y
		z.left = T3 
		if T3:
			T3.parent = z
		y.parent = temp
  
		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
		# Return the new root 
		return y 
  
	def getHeight(self, root): 
		if not root: 
			return 0
		return root.height 
  
	def getBalance(self, root): 
		if not root: 
			return 0
		return self.getHeight(root.left) - self.getHeight(root.right) 
  
	def print(self, root): 
		if not root: 
			return
  
		print("{0} ".format(root.val), end="") 
		self.print(root.left) 
		self.print(root.right)

	def display(self, root):
		root.display() 
		print("Balance: " + str(self.getBalance(root)))

	def searchNormal(self, root, n, f):
		global level
		if n < root.val and root.left is not None:
			level+=1
			self.searchNormal(root.left, n,f)
		elif n > root.val and root.right is not None:
			level+=1
			self.searchNormal(root.right, n,f)
		elif n == root.val:
			f.write("," + str(level))
		return root
	def searchNewPriority(self, root, key):
		global level, newPriority,levels
		if not root: 
			return root
		elif key < root.val: 
			level+=1
			root.left = self.searchNewPriority(root.left, key) 
		elif key > root.val: 
			level+=1
			root.right = self.searchNewPriority(root.right, key) 
		elif key == root.val:
			levels.append(level)
			newPriority = random.randint(1, root.priority)
			root.priority = newPriority
		# Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						   self.getHeight(root.right)) 
		if root.left:
			root.left.parent = root
		if root.right:
			root.right.parent = root;
  
		while(root.right and root.right.priority< root.priority):
			root = self.leftRotate(root)
		while(root.left and root.left.priority < root.priority):
			root = self.rightRotate(root)
		return root
	def searchSwapParent(self, root, key):
		global level, levels
		if not root: 
			return root
		elif key < root.val: 
			level+=1
			root.left = self.searchSwapParent(root.left, key) 
		elif key > root.val: 
			level+=1
			root.right = self.searchSwapParent(root.right, key) 
		elif key == root.val:
			levels.append(level)
			if(root.parent):
				root.priority, root.parent.priority = root.parent.priority, root.priority
		# Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
		if root.left:
			root.left.parent = root
		if root.right:
			root.right.parent = root;
  
		while(root.right and root.right.priority< root.priority):
			root = self.leftRotate(root)
		while(root.left and root.left.priority < root.priority):
			root = self.rightRotate(root)
		return root

	def searchSwapParentWithProb(self, root, key):
		global level, swapped, prob
		if not root: 
			return root
		elif key < root.val: 
			level+=1
			root.left = self.searchSwapParentWithProb(root.left, key) 
		elif key > root.val: 
			level+=1
			root.right = self.searchSwapParentWithProb(root.right, key) 
		elif key == root.val:
			levels.append(level)
			prob = 1/self.getHeight(root)
			if random.random() < 1/self.getHeight(root) and root.parent:
				swapped = True
				root.priority, root.parent.priority = root.parent.priority, root.priority
			else:
				swapped = False
		# Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
		if root.left:
			root.left.parent = root
		if root.right:
			root.right.parent = root;
  
		while(root.right and root.right.priority< root.priority):
			root = self.leftRotate(root)
		while(root.left and root.left.priority < root.priority):
			root = self.rightRotate(root)
		return root

def calcRotations():
	global rotations
	leftRotations = 0
	rightRotations = 0
	for i in rotations:
		if i == "LR":
			leftRotations +=1
		elif i == "RR":
			rightRotations += 1
		else:
			print("Something went wrong!")
	return (leftRotations, rightRotations)
def saveTreap(root, prog, f):
	global level
	if root:
		level +=1
		saveTreap(root.left, prog,f)
		saveTreap(root.right, prog,f)
		level -=1 
		f.write(prog + "," + str(root.val) + "," + str(level) + "\n")
def file_len(file):
    for i, l in enumerate(file):
        pass
    return i + 1

def run(list,f,code,prog,t):
	global root, myTreap, level, levels, rotations, newPriority 
	for l in tqdm(list,total=t):
		l = l.strip()
		if(len(l.split()) == 2):
			x = int(l.split()[0])
			pri = int(l.split()[1])
		else:
			l = int(l)
		f.write(prog);
		start = time.perf_counter_ns()
		if (code == "I"):
			root = myTreap.insert(root,nd.Node(x,pri))
			lrRotations = calcRotations()
			f.write("," + str(lrRotations[0] + lrRotations[1]) + "," + str(lrRotations[0]) + "," + str(lrRotations[1]) + "," + " ".join(str(e) for e in levels))
		elif (code == "D"):
			root = myTreap.delete(root, l)
			lrRotations = calcRotations()
			f.write("," + str(lrRotations[0] + lrRotations[1]) + "," + str(lrRotations[0]) + "," + str(lrRotations[1]) + "," + " ".join(str(e) for e in levels))
		elif (code == "S"):
			if prog == "n":
				root = myTreap.searchNormal(root,l, f)
			elif prog == "np":
				root= myTreap.searchNewPriority(root,l)
				lrRotations = calcRotations()
				f.write("," + str(lrRotations[0] + lrRotations[1]) + "," + str(lrRotations[0]) + "," + str(lrRotations[1]) + "," + " ".join(str(e) for e in levels) +"," + str(newPriority) )
			elif prog == "ps":
				root = myTreap.searchSwapParent(root,l)
				lrRotations = calcRotations()
				f.write("," + str(lrRotations[0] + lrRotations[1]) + "," + str(lrRotations[0]) + "," + str(lrRotations[1]) + "," + " ".join(str(e) for e in levels) )
			elif prog == "psp":
				#FIX HERE!! IT ROTATES NOW
				root = myTreap.searchSwapParentWithProb(root,l)
				lrRotations = calcRotations()
				f.write("," + str(lrRotations[0] + lrRotations[1]) + "," + str(lrRotations[0]) + "," + str(lrRotations[1]) + "," + " ".join(str(e) for e in levels) +"," + str(prob) + "," + str(swapped))
			else:
				print("Something went wrong")
		f.write("," + str(myTreap.getHeight(root)) + 
		"," + str(myTreap.getBalance(root)) + 
		"," + str(time.perf_counter_ns()-start)+ "\n")
		level = 1
		rotations = []
		levels = []
		#myTreap.display(root)

inf = open('insertion_output.txt','w')
inf.write("treap_type,num_rotations,num_left_rotations,num_right_rotations,level(s),height,balance,time\n")
df = open('deletion_output.txt','w')
df.write("treap_type,num_rotations,num_left_rotations,num_right_rotations,level(s),height,balance,time\n")
nsf = open('n_search_output.txt','w')
nsf.write("treap_type,level(s),height,balance,time\n")
npsf = open('np_search_output.txt','w')
npsf.write("treap_type,num_rotations,num_left_rotations,num_right_rotations,level(s),new_priority,height,balance,time\n")
pssf = open('ps_search_output.txt','w')
pssf.write("treap_type,num_rotations,num_left_rotations,num_right_rotations,level(s),height,balance,time\n")
pspsf = open('psp_search_output.txt','w')
pspsf.write("treap_type,num_rotations,num_left_rotations,num_right_rotations,level(s),probability,swapped,height,balance,time\n")
ff = open('final_output.txt','w')
ff.write("treap_type,value,level(s)\n")
i = open('treap_insertion_file.txt', 'r+')
s = open('treap_search_file.txt', 'r+')
d = open('treap_delete_file.txt', 'r+')
insertionLength = file_len(i)
deletionLength = file_len(d)
searchLength = file_len(s)
levels = []
rotations = []
level = 1
myTreap = Treap() 
root = None
newPriority = 0
swapped = False
prob = 0

i.seek(0)
d.seek(0)
s.seek(0)
run(i,inf,"I", "n", insertionLength)
run(d,df,"D", "n", deletionLength)
run(s,nsf,"S", "n", searchLength)
#myTreap.display(root)
saveTreap(root, "n", ff)

myTreap = Treap() 
root = None
i.seek(0)
d.seek(0)
s.seek(0)
run(i,inf,"I", "np", insertionLength)
run(d,df,"D", "np", deletionLength)
run(s,npsf,"S", "np", searchLength)
#myTreap.display(root)
saveTreap(root, "np", ff)

myTreap = Treap() 
root = None
i.seek(0)
d.seek(0)
s.seek(0)
run(i,inf,"I", "ps", insertionLength)
run(d,df,"D", "ps", deletionLength)
run(s,pssf,"S", "ps", searchLength)
#myTreap.display(root)
saveTreap(root, "ps",ff)

myTreap = Treap() 
root = None
i.seek(0)
d.seek(0)
s.seek(0)
run(i,inf,"I", "psp", insertionLength)
run(d,df,"D", "psp", deletionLength)
run(s,pspsf,"S", "psp", searchLength)
#myTreap.display(root)
saveTreap(root, "psp",ff)
