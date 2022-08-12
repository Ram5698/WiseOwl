import glob

inputFolders= glob.glob(r"C:\Users\Sairam\Desktop\ABC\\**\*.txt",recursive=True)

for i in inputFolders:
    print(i)