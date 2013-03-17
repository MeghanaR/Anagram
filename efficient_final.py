import sys
import os
import time
ip1=raw_input("Enter name\n")
ip2=raw_input("Enter second input to be tested\n")
start_time=time.time()
l1=len(ip1)
l2=len(ip2)
s1=s2=0
if(l1!=l2):
	print 'not anagram'

else:
	for i in range(0,l1):
		s1=s1+ord(ip1[i])
		s2=s2+ord(ip2[i])
	if s1==s2:
		print 'Anagram'
	else:
		print 'not anagram'
end_time=time.time()
time_taken=end_time-start_time
print 'Time taken to execute the program: %.8f'%(time_taken)
