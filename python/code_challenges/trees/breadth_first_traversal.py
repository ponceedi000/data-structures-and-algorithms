from trees.queue import Queue

class Breadth_First_Traversal:

	def breadth_first(tree):
		list = [ ]
		breadth = Queue()

		if tree.root is None:
			return list

		breadth.enqueue(tree.root)

		while not breadth.is_empty():
			front = breadth.dequeue()
			list.append(front.value)

			if front.left:
				breadth.enqueue(front.left)

			if front.right:
				breadth.enqueue(front.right)

		return list
