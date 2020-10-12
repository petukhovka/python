import re

with open("in_file_task6.txt") as f_obj:
    list = []
    vcbl = {}
    for line in f_obj:
        nums = re.findall(r'\d+', line)
        nums = [int(i) for i in nums]
        s = sum(nums)
        list = line.split()
        vcbl[list[0]] = s

    print(vcbl)