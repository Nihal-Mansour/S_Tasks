def isBalanced(input):
    # this condition to check whether the length of the string is even or not as if it is not even then 
    # there is a missing number of brackets and this will return NO from the begining.
    if (len(input) % 2 != 0):
        return "NO"
    '''
    The Approach taken is the stack as we will push every open bracket to the stack and when we meet 
    a close bracket we will have to pop from the stack which will actually bring the last entered element
    and then we have to check whether the current character is the close bracket of the poped one from the stack or not
    if it is the closed one then continue the checks till finishing the string, but if it is not the closed bracket then
    it is not balanced and return NO. finally if it comes to the end of the for loop without returning with NO, then the string
    is balanced and return YES.
    '''
    stack = []
    for char in input:
        if char in ['(','{','[']:
            stack.append(char)
        else:
            # this condition to check if the string starts with close bracket then it is not balanced
            if len(stack) == 0 and char in ['}',']',')']:
                return "NO"
            open = stack.pop()
            if (open == '(' and char != ')') or (open == '[' and char != ']') or (open == '{' and char != '}'):
                return "NO"
    # if the stack is empty then we have matched all open brackets with closed ones then return YES otherwise return NO
    if len(stack) == 0:
        return "YES"
    else: return "NO"

def main():
    num = input("Enter number of Strings: ")
    outputs = []
    for i in range(int(num)):
        string = input("Enter string " + str(i+1) + " : ")
        output = isBalanced(string)
        outputs.append(output)
    for output in outputs:
        print(output)

main()

'''
Tests:
//////////////first test//////////////
input:
3
{[()]}
{[(])}
{{[[(())]]}}
output:
YES
NO
YES
/////////////////////////////////////
//////////////second test//////////////
input:
2
{{((()))}}
{()
output:
YES
NO
/////////////////////////////////////
/////////////third test//////////////
input:
6
}][}}(}][))]
[](){()}
()
({}([][]))[]()
{)[](}]}]}))}(())(
([[)
output:
NO
YES
YES
YES
NO
NO
'''
