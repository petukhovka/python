import re
import json

with open("in_file_task7.txt") as f_obj:
    list = []
    vcbl = {}
    s = 0
    for line in f_obj:
        nums = re.findall(r'\d+', line)
        nums = [int(i) for i in nums]
        list = line.split()
        vcbl[list[0]] = nums[1] - nums[2]
        s = s + vcbl[list[0]]
    vcbl['average_profit: '] = s / len(vcbl)
    print(vcbl)
with open("out_file_task7.json", "w") as f_obj:
    json.dump(vcbl, f_obj)