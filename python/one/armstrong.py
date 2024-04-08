def armstrong(num):
     oldnum=num
     sum=0
     while(num>0):
             sum=sum+(num%10)**3
             num=num//10
     if(sum==oldnum):
             return "armstrong",sum
     else:
             return "bandar",sum,num
print(armstrong(153))