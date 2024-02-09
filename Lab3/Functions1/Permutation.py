def get_permutation(input_string, index=0):

    if index == len(input_string):   	 
        print("".join(input_string))

    for swap_index in range(index, len(input_string)):

        char_list = [char for char in input_string]
   
        char_list[index], char_list[swap_index] = char_list[swap_index], char_list[index]
   	 
        get_permutation(char_list, index + 1)


user_input = str(input("Enter a string: "))
get_permutation(user_input)
