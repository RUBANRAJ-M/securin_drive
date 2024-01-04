die_A=[1,2,3,4,5,6]
die_B=[1,2,3,4,5,6]
tot_comb=0
for i in die_A:
    for j in die_B:
        tot_comb+=1
print("1. The Total number of combinations are : ",tot_comb)
print()
print("2. The Distribution of all possible combinations are :")
for i in die_A:
    for j in die_B:
        print('({},{})'.format(i,j),end=" ")
    print()
print()
print("The sum of distribution of all possible combinations are :")
sum_of_comb=[]
for i in die_A:
    for j in die_B:
        print(i+j,end=" ")
        sum_of_comb.append(i+j)
    print()
sums=set(sum_of_comb)
print()
print("3. The Probability of All Possible Sums Occuring among the number of Combinations are :")
for k in sums:
    print("P(Sum={}) = {}/36 = {}".format(k,sum_of_comb.count(k),sum_of_comb.count(k)/36))
        
