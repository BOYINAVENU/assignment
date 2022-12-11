import os
os.chdir("F:\\New folder")
print(os.getcwd())
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
if(n1>0 and n2>0 and n3>0 and n4>0 and n5>0):
    sum1=n1+n2+n3+n4+n5
    print("total sum is  " + str(sum1))
    sum1=str(sum1)
    file2=open('myfile1.txt','w')
    file2.write("total sum is "+sum1)
    file2.close()
else:
    print('please enter positive number')
    s='please enter positive number'
    file2=open('myfile1.txt','w')
    file2.write(s)
    file2.close()





