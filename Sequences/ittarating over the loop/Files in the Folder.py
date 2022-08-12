# import os

# files= os.walk(r"D:\D_Drive_Backup\\")
# for File in files:
#     file=str(File).partition("\\")
#     print(file[-1])


# import sys

# modules= sys.builtin_module_names

# for module in modules:
#     if module[0]!="_":
#      print(module)

# from os import urandom
# import requests

# response = requests.get('https://webscraper.io/test-sites/')

# print(response.status_code)

# if response.status_code !=200:
#     quit()

# UrlList = response.text.splitlines()    

# for page in UrlList:
#     trim_page = page.strip()
#     if "<a" in trim_page:
#      print(trim_page)