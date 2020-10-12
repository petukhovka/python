out_f = open("out_file_task4.txt", "w")
russian = ['Один', 'Два', 'Три', 'Четыре']
with open("in_file_task4.txt") as f_obj:
    s = 0
    i = 0
    list = []
    for line in f_obj:
        list = line.split(' ')
        new_string = russian[i] + ' ' + list[1] + ' ' + list[2]
        out_f.writelines(new_string +'\n')
        i += 1
out_f.close()