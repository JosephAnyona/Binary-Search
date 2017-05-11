
class BinarySearch(list):
	
	def __init__(self, a, b):
		self.a = a
		self.b = b    
		for i in range(1,a+1):
			# print("i: %s and b: %s" %(i,b))
			self.append(i*b)

		self.length = len(self)

		
	def search(self, target):
		self.sort() # sort the list first
		
		first = 0
		last = self.length - 1
		
		count = 0
		while 1:
			# print("count ",count)

			middle = ((first + last) // 2) 

			if first > last or middle > last:
				return {'count':count, 'index':-1}
			
			if self[middle] == target:
				return {'count':count, 'index':middle}

			elif self[last] == target:
				return {'count':count, 'index':last}

			elif self[first] == target:
				return {'count':count, 'index':first}

			elif middle==first or middle==last:
				return {'count':count, 'index':-1}			

			elif self[middle] < target:
				# middle = ((first + last) // 2) + 1
				first = middle + 1

			elif self[middle] > target:
				# middle = ((first + last) // 2)
				last = middle - 1

			count+=1
	