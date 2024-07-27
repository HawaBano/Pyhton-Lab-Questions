# try:
#     with open("C:\\Users\\Murtaza\\Desktop\\file handling\A.text", "r") as f2:
#         with open("C:\\Users\\Murtaza\\Desktop\\file handling\ B.text", "w") as f3:
#             for i in f2:
#                 f3.write(i)

# except:
#     print("the file not exits ....plz create a file!")
# else:
#     f2.close()
#     print("the file is closed!.....")

import os
if os.path.exists("C:\\Users\\Murtaza\\Desktop\\file handling\C.text"):
    os.remove("C:\\Users\\Murtaza\\Desktop\\file handling\C.text")
    print("delete the file successusfully.")
else:
    print("the file is not exist!......")


