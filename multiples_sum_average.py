#multiples

#part 1
#print all odd numbers from 1 to 1000
for i in range(1, 1000):
	if i % 2 != 0:
		print i

#part 2
#print all multiples of 5 from 5 to 1,000,000
for i in range(5, 1000000):
	if i % 5 == 0:
		print i


#sum list
#print the sumer of all the values in the given list
a = [1,2,5,10,255,3]

for i in a:
	print i

#average
#print the average of the values in the given list
a = [1,2,5,10,255,3]

s = 0

for x in a:
	s += x

print s / len(a)