class Node:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x

def Inorder(root):

	if root:

		
		Inorder(root.left)

		
		print(root.val),

		
		Inorder(root.right)



def Postorder(root):

	if root:

		
		Postorder(root.left)

		
		Postorder(root.right)

		
		print(root.val),



def Preorder(root):

	if root:

		print(root.val),

		
		Preorder(root.left)

		
		Preorder(root.right)



root = Node(12)
root.left = Node(13)
root.right = Node(14)
root.left.left = Node(15)
root.left.right = Node(16)
print ("\nPreorder traversal")
Preorder(root)
print ("\nInorder traversal")
Inorder(root)
print ("\nPostorder traversal")
Postorder(root)
