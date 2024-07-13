ops = ['+','-','','/','*','%']

def getLeftDigit(str):
        str = str.strip()
        y = len(str)-1
        
        if str.isdigit():
            return str
        
        if  len(str) < 1:
            return 0
        
        for x in range(len(str)-1):
            if str[y] in ops:
                if x == 0:
                    print("Wrong expression!!, Enter the right arithmetic expression: "+str)
                else:
                    return str[y+1:]  
            else:
                y = y -1            
def getRightDigit(str):
        y = 0
        str = str.strip()
        if str.isdigit():
            return str
        
        if  len(str) < 1:
            return 0
            
        for x in range(len(str)-1):
            if str[y] in ops:
                if x == 0:
                    print("Wrong expression!!, Enter the right arithmetic expression: "+str)
                else:
                    return str[0:y]  
            else:
                y = y +1           


def operate(str1,str2,op):
    leftNum = getLeftDigit(str1)
    rightNum = getRightDigit(str2)
    ans = 0
    if op == "*":
        ans = int(leftNum) * int(rightNum)
        str1 = str1 + '*' + str2
        return str1.replace(str(leftNum) + op + str(rightNum), str(ans))
    
    if op == "+":
        ans = int(leftNum) + int(rightNum)
        str1 = str1 + '+' + str2
        return str1.replace(str(leftNum) + op + str(rightNum), str(ans))
    
    if op == "-":
        ans = int(leftNum) - int(rightNum)
        str1 = str1 + '-' + str2
        return str1.replace(str(leftNum) + op + str(rightNum), str(ans))

express_input = input(f"Enter an arithmetic expression:")

while express_input.find('*')>=0:
    left_right = express_input.split('*',1)
    express_input = operate(left_right[0],left_right[1],'*')
    

while express_input.find('+')>=0:
    left_right = express_input.split('+',1)
    express_input = operate(left_right[0],left_right[1],'+')
    if express_input.startswith("+"):
        break

while express_input.find('-')>=0:
    left_right = express_input.split('-',1)
    
    express_input = operate(left_right[0],left_right[1],'-')
    if express_input.startswith("-"):
        break


print(express_input)