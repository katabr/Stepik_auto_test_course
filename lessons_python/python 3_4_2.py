import os
import collections

file = os.path.join('D:','ЮDK', 'lessons_python', 'file_in.txt')

# открываем входящий файл, записываем его в строку
with open( file , 'r') as inf:
    in_string = inf.readline()
l = len(in_string)
c = collections.Counter()
i = 0
out_string = ''
num = ''
num1 = 0
while i<l :
    if in_string [i] > 'A' :
        out_string = out_string  + in_string [i]
    else :
        num = num + in_string [i]
        while in_string [i+1] < A :
            num = num + in_string[i]
    num1 = int(num)
    for j in num1-1:
        out_string = out_string  + in_string [i]
    num = ''
    num1 = 0

    print(out_string )



#os.path.join('python3_4_2.py')

with open('file_out.txt', 'w') as ouf:
    ouf.write(out_string )