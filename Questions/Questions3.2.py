#获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
#Questions3.2.py
s = input()
ls = s.split("-")
print("{}+{}".format(ls[0], ls[-1]))