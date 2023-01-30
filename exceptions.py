# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print('D')
#     except C:
#         print("C")
#     except B:
#         print('B')

# import sys

# try:
#     f = open('db.sqlite3')
#     s = f.readline()
#     i = str(s.strip())
# except OSError as err:
#     print('OS error: {0}'.format(err))
# except ValueError:
#     print("the input data cannot be converted to string type")
# except:
#     print('Unexpected error: ', sys.exc_info()[0])
#     raise


# try:
#     raise NameError("HiTHere")
# except NameError:
#     print("AN outsiding error occurred")
#     raise

with open('db.sqlite3') as f:
    for line in f:
        print(line, end=" ")