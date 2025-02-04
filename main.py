'''Известно, что у дракона может быть несколько голов и его сила определяется числом голов. Но как определить силу драконьей стаи, в которой несколько драконов и у 
каждого из них определенное число голов? Вероятно, вы считаете, что это значение вычисляется как сумма всех голов? Это далеко не так, иначе было бы слишком просто 
вычислить силу драконьей стаи. Оказывается, что искомое значение равно произведению значений числа голов каждого из драконов. Например, если в стае 3 дракона,
 у которых 3, 4 и 5 голов соответственно, то сила равна 3*4*5 = 60. Предположим, что нам известно суммарное количество голов драконьей стаи, как нам вычислить 
 максимально возможное значение силы этого логова драконов? Именно эту задачу Вам и предстоит решить.
Входные данные
В единственной строке входного файла INPUT.TXT записано натуральное число N (0 < N < 100) – количество голов драконьей стаи.
Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести максимально возможное значение силы, которая может быть у стаи драконов из N голов.'''
input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
N=int(data)
if N == 1:
    output_data.write("1")
elif N%3==0:
    a=N//3
    out=3**a
    output_data.write(str(out))
elif N%3==1:
    a=(N//3)-1
    out=(3**a)*4
    output_data.write(str(out))
elif N%3==2:
    a=N//3 
    out=(3**a)*2
    output_data.write(str(out))              

output_data.close()
input_data.close()