#sum of Squres of numbers in simple method than usual
def sumofsquares(nums):
	return sum(x * x for x in nums)

lis=[]
n=int(input('please specify the how many numbers you need to have sum of Squares'))
print('Enter The Numbers')
for i in range(1,n):
	lis.append(int(input())	

j=sumofsquares(lis)
print(j)