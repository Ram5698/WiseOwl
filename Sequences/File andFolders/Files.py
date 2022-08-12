
####Best way to open a file

# with open(r"C:\Users\Sairam\Desktop\Config.txt","r+") as Filename:
#     for i in Filename:
#         print(i)

#reading a file
ConfigFilePath=open(r"C:\Users\Sairam\Desktop\Config.txt","r+")

 #################################best way (genertor)###############

# for i in ConfigFilePath:
#     i=i.split("=")
#     variable_number,Variable_index=i
#     print(variable_number.strip(),Variable_index.strip())
#     print(type(variable_number),type(Variable_index))

 #################################readlines###############
# lines= ConfigFilePath.readlines()

# for i in lines:
#     i=i.split("=")
#     variable_number,Variable_index=i
#     print(variable_number.strip(),Variable_index.strip())
#     print(type(variable_number),type(Variable_index))

#################################read###############

# lines= ConfigFilePath.read()
# print(lines)
 
 #################################readline###############
# for i in range(1,6):
#  lines= ConfigFilePath.readline()
#  print(lines)



########################Writing a File###################
with open(r"C:\Users\Sairam\Desktop\Config.txt","a") as WriteFile:
    WriteFile.write("Hellow Hi\n")
    WriteFile.writelines("Hellow Hi")

ConfigFilePath.close()
