
userInput   = int(input("Enter a number: "))
numList     = range(2,userInput)
divisorList = []

for item in numList:
    if(userInput%item == 0):
        divisorList.append(item)
        
print(divisorList)    
