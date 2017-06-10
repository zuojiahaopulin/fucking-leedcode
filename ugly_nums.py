def get_ugly_nums(index):
    if index < 0:
        return 0
    ugly_nums = [1] * index
    next_ugly_num = 1
    ug_2 = 0
    ug_3 = 0
    ug_5 = 0
    while(next_ugly_num < index):
        min_num = min(ugly_nums[ug_2] * 2, ugly_nums[ug_3] * 3, ugly_nums[ug_5] * 5)
        ugly_nums[next_ugly_num] = min_num

        while ugly_nums[ug_2]*2 <= ugly_nums[next_ugly_num]:
            ug_2 += 1
        while ugly_nums[ug_3]*3 <= ugly_nums[next_ugly_num]:
            ug_3 += 1
        while ugly_nums[ug_5]*5 <= ugly_nums[next_ugly_num]:
            ug_5 += 1

        next_ugly_num += 1
    ugly = ugly_nums[next_ugly_num-1]
    return ugly
    
if __name__ == "__main__":
    print get_ugly_nums(100)
