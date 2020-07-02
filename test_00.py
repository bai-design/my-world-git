# foo = "abicdfeboxyz"
# new_foo = [i for i in foo]
# begin = 0
# end = len(new_foo)-1
# while begin < end :
#     while new_foo[begin] not in ['a', 'e', 'i', 'o', 'u']:
#         begin += 1
#     while new_foo[end] not in ['a', 'e', 'i', 'o', 'u']:
#         end -= 1
#     if begin < end:
#         new_foo[begin], new_foo[end] = new_foo[end], new_foo[begin]
#         begin += 1
#         end -= 1
# print(''.join(new_foo))
