def Concatenation(n,number, ans):
    i=1
    for i in range(n*2):
        if(i<=n):
            ans[i] = number[i]
        elif(i>n):
            ans[i+n] = number[i]
    print(ans)

n = int(input("\nEnter length of first array: "))
length=n
nums = []
ans = []
i=0

while (length!=0):
    
    number = int(input(f"Enter element {i+1} : "))
    nums.append(number)
    i+=1
    length-=1
    
answerList = Concatenation(n,number, ans)
print(f"The final list after concatenate with number: {answerList}")