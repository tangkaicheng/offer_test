"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
思路一：将范围内的数字转为字符串拼接，获得里面出现1的次数
思路二：1 到 10 范围内，个位数出现1的次数为：1 * 10 ** （1-1）次
        1 到100范围内，十位数出现1的次数为：1* 10 ** （2 - 1）次
        1到1000范围内，百位数出现1的次数为：1*10 ** （3-1）次。。。
        所以当n为2134 = 2000 + 100 + 30 + 4
        2000在范围1到10000范围内
        在个位上，从1到2130，包含了213个10，因此1出现了213次(1, 11, 21, ... 2121, 2130)，加上2131出现的一次，故在各位上出现了213 + 1 = 214次
        规律：在个位上是4，4 > 1,则在个位上包含1的数目为（高位数字+1）*10^(i-1)=(213+1)*10^0 = 214

        在十位上，从1到2100，包含了21个100，因此出现了21次(10， 110， 210，310，410... 2100)，剩下的数字2101~2134中出现了10次1，故出现了210+10=22-
        规律：在十位上是3>1,则在十位上包含1的数目为（高位数字+1）*10^(i-1)=(21+1)*10^(2-1)=220

        在百位上为1=1，则在百位上包含1的数目为(高位数字) * 10 ^ (i-1) +(低位数字+1)=2*10^(3-1) + (34+1)=235
        在千位上为2>1，则在前位上包含1的数目为（高位数字+1）*10^(i-1)=(0+1)*10^(4-1)=1000
"""


def number_of_between_1_and_n_solution(n, m=1):
    str_num = ''
    for i in range(m, n+1):
        str_num += str(i)
    return str_num.count('1')


def number_of_between_1_and_n_solution_2(n):
    total = 0
    i = 1       # 个位
    j = 1       # 从后往前数第几位
    while n // i != 0:
        high_num = n // (i * 10)
        current_num = (n // i) % 10     # 第一次循环除以10取余为个位数，第二次循环除以1--取余为十位数
        low_num = n - (n // i) * i
        if current_num > 1:     # 对于数字n，计算它的第i(i从1开始，从右边开始计数)位数上包含的数字1的个数
                                # 如果x > 1的话，则第i位数上包含的1的数目为：(高位数字 + 1）* 10 ^ (i-1) (其中高位数字是从i+1位一直到最高位数构成的数字)
            total += (high_num + 1) * 10 ** (j - 1)
        elif current_num == 1:  # 如果x == 1的话，则第i位数上包含1的数目为：(高位数字) * 10 ^ (i-1) +(低位数字+1) (其中低位数字时从第i - 1位数一直到第1位数构成的数字)
            total += high_num * 10 ** (j - 1) + low_num + 1
        else:           # 如果x < 1的话，则第i位数上包含的1的数目为：(高位数字 ）* 10 ^ (i-1)
            total += high_num * 10 ** (j - 1)
        j += 1
        i *= 10
    return total


if __name__ == '__main__':
    print(number_of_between_1_and_n_solution(2134))
    print(number_of_between_1_and_n_solution_2(2134))