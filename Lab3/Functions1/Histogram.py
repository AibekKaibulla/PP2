def histogram(list):
    for i in list:
        for j in range(i):
            print("*", end="")
        print()

my_list = list(map(int, input().split()))
histogram(my_list)