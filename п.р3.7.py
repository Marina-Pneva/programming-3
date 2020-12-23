string=input()
sum=0
for i in range(len(string)):
    if string[i]=='0'or string[i]=='1'or string[i]=='2' or string[i]=='3' or string[i]=='4' or string[i]=='5' or string[i]=='6' or string[i]=='7' or string[i]=='8' or string[i]=='9':
        sum+=int(string[i])
print(sum)
