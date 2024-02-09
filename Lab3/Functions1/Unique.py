def unique(list):
    result=[]
    for element in list:
        if element not in result:
            result.append(element)
    print(result)

my_list=list(map(int, input(). split()))

unique(my_list)
        