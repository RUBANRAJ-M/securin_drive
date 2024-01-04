die_A=[1,2,3,4,5,6]
die_B=[1,2,3,4,5,6]
sum_of_comb=[]
for i in die_A:
    for j in die_B:
        sum_of_comb.append(i+j)
sums=list(set(sum_of_comb))
count_of_sums=[]
for k in sums:
    count_of_sums.append(sum_of_comb.count(k))
def undoom_dice(die_1,die_2):
    sum_of_comb_undoom=[]
    for i in die_1:
        for j in die_2:
            sum_of_comb_undoom.append(i+j)
    sums_of_undoom=list(set(sum_of_comb_undoom))
    count_of_undoom=[]
    for k in sums_of_undoom:
        count_of_undoom.append(sum_of_comb_undoom.count(k))
    if(sums==sums_of_undoom and count_of_sums==count_of_undoom):
        return True
    else:
        return False
New_die_A=[1,4]
New_die_B=[1,8]
Rem_faces_A=[[2,3,3,3],[2,3,2,3],[2,2,2,3],[2,2,2,2],[3,3,3,3]]
Rem_faces_B=[]
p=list(range(min(New_die_B)+1,max(New_die_B)))
for i in p:
    for j in p:
        if i!=j:
            r=p.copy()
            r.remove(i)
            r.remove(j)
            if r not in Rem_faces_B:
                Rem_faces_B.append(r)
for spots_A in Rem_faces_A:
    for spots_B in Rem_faces_B:
        New_die_A=[1,4]
        New_die_A += spots_A
        New_die_B=[1,8]
        New_die_B += spots_B
        if(undoom_dice(New_die_A,New_die_B)):
            New_die_A=sorted(New_die_A)
            New_die_B=sorted(New_die_B)
            print("New Die A = ",New_die_A)
            print("New Die B = ",New_die_B)

        
        
