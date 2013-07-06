#!/usr/bin/env python


from array import *
from tree_lcrs import *
from tree_loc import *
from list_pointer import *

def heightOfTreeLCRS(x, z): #x - tree , #z node
	#print "height called:", x, z.element
	
	if x.leftmost_child(z)==None and x.right_sibling(z)==None:
		return 0
	elif x.leftmost_child(z)!= None and x.right_sibling(z)!=None:
		if heightOfTreeLCRS(x, x.leftmost_child(z))+1>heightOfTreeLCRS(x,
x.right_sibling(z)):
			return heightOfTreeLCRS(x,x.leftmost_child(z))+1
		else:
			return heightOfTreeLCRS(x,x.right_sibling(z))
	elif x.leftmost_child(z)!= None and x.right_sibling(z)== None:
		return heightOfTreeLCRS(x,x.leftmost_child(z))+1
	else:
	  #Doesnt have child, has sibing
		return heightOfTreeLCRS(x,x.right_sibling(z))
	  


#def heightOfTreeLCRS(x):


A= TreeLCRS() 
B=TreeLCRS()
C=TreeLCRS()
D=TreeLCRS()
E = TreeLCRS()
F=TreeLCRS()
G=TreeLCRS()
H=TreeLCRS()
I=TreeLCRS()
J=TreeLCRS()
K=TreeLCRS()
L=TreeLCRS()
M=TreeLCRS()
N=TreeLCRS()


A = A.create(0,"A")
B = B.create(0,"B")
C = C.create(0,"C")
D=D.create(0,"D")
E = E.create(0,"E")
F=F.create(0,"F")
G = G.create(0,"G")
H = H.create(0,"H")
I = I.create(0,"I")
J = J.create(0,"J")
K = K.create(0,"K")
L=L.create(0,"L")
M=M.create(0,"M")
N=N.create(0,"N")



I=I.create(2,"I",[M,N])
G=G.create(2,"G",[J,K])
H=H.create(1,"H",[L])
C=C.create(3,"C",[F,G,H])
E = E.create(1,"E",[I])
B =B.create(2,"B",[D,E])
A=A.create(2,"A",[B,C])

#For each created tree include adjustment
C.relativeIndex = A.locate("C")


print A.locate("C")

#A.printtree()
#C.printtree()

print heightOfTreeLCRS(A,A.root_node())
print heightOfTreeLCRS(C,C.root_node())


y= TreeLCRS()



#concatenateLists(L)


