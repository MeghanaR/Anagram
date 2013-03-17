import sys
import time
#start_time=time.time()


inp1=raw_input("Enter the Name.\n")
inp2=raw_input("Enter the name to be tested for an anagram.\n")

start_time=time.time()

inp1=inp1.lower()
inp2=inp2.lower()
li1=[]
li2=[]
for i in range(0,len(inp1)):
	li1.append(inp1[i])

for i in range(0,len(inp2)):
	li2.append(inp2[i])
flag=1
while flag==1 :
	Cnt=0
	if li1 == '' or li2 == '' : 
  		print 'Wrong Input. Strings cannot be empty!'
  		sys.exit(1)
	elif len(inp1)!=len(inp2):
		print 'not anagram'
		break
	else:
		for Char1 in li1 :
        		if Char1 in li2 :
      				Cnt+=1
  		if Cnt == len(li1): #and li1 not in li2 and li2 not in li1 :  
  			print 'These Strings are anagrams! :D '
  			break
  		else : 
 			print 'These Strings are not anagrams :( '
			flag=0
			break
  		print

	
		  

#end_time=time.time()
end_time=time.time()

time_taken=end_time-start_time
#time_taken=round(time_taken,3)

print 'Time taken to execute the program: %.8f'%(time_taken)
