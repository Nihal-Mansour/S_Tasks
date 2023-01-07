"""
Method1:
The approach is to slice the string , take all characters before that position then concatenate the new
one then continue concatenating the rest of the string. 
"""
def mutate_string1 (string, position , character):
    return string[:position] + character + string[position+1:]


"""
Method2:
The approach is to convert the string into a list of characters and then we can simply change the character 
in the given position with the new one and after that we will join back this list of characters so that 
it becomes one string again.
"""
def mutate_string2 (string, position , character):
    new_string = list(string)
    new_string[position] = character
    return "".join(new_string)

def main ():
    input_string = input("Enter the String: ")
    pos_char = input("Enter the position then the character: ").split()
    print("The Result of First Method: ",mutate_string1(input_string,int(pos_char[0]),pos_char[1]))
    print("The Result of Second Method:",mutate_string2(input_string,int(pos_char[0]),pos_char[1]))


main()


"""
These functions are tested on the following examples:
1- Nehal  1 i  ==> Nihal
2- abracadabra  5 k ==> abrackdabra
3- movie  0 M ==> Movie
4- String  3 o ==> Strong
"""