def palindrome_chain_length(n):
    
    number = n
    steps = 0
    while(True):
        if(check_for_palindrome(number) is True):
            break                
        else:
            number = number + reverse_number(number)
            steps+=1
    return steps
    
def check_for_palindrome(input):
    numberStr = str(input)
    numberLen = len(numberStr)
    if(numberLen % 2 == 0):
        max=int(numberLen / 2)
    else:
        max=int((numberLen-1) / 2)
        
    for i in range(0, int(max)):
        if(numberStr[i] == numberStr[numberLen-i-1]):
            continue
        else:
            return False
    return True
    
def reverse_number(number):
    number = str(number)
    newNumber = ''
    numberLen = len(number)

    for i in range(numberLen-1, -1, -1):
        newNumber+=number[i]

    return int(newNumber)

print(palindrome_chain_length(87))
