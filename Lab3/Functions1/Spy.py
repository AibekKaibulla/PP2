def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i] ==0 and nums[i+1] == 0 and nums[i+2]==7:
            return True
    return False
    
    
    
my_list=list(map(int, input("Enter numbers:"). split()))
print(spy_game(my_list))