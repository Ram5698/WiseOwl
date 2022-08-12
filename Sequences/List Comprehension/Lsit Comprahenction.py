
# # for i in range(1,100,2):
# #  print(i**2)

#  #list comprahension

# # List_numbers=[i**2 for i in range(1,101) if i%2==0]
# # print(List_numbers)

# # List_numbers=[i**2 for i in range(2,101,2) ]
# # print(List_numbers)



# Poem ="""Whose woods these are I think I know.   
# His house is in the village though;   
# He will not see me stopping here   
# To watch his woods fill up with snow.   
# My little horse must think it queer   
# To stop without a farmhouse near   
# Between the woods and frozen lake   
# The darkest evening of the year.   
# He gives his harness bells a shake   
# To ask if there is some mistake.   
# The only other sound’s the sweep   
# Of easy wind and downy flake.   
# The woods are lovely, dark and deep,   
# But I have promises to keep,   
# And miles to go before I sleep,   
# And miles to go before I sleep  Finnally."""


# # poem_List=Poem.split()
# # print(poem_List)

# # for word in poem_List:
# #     y_Exist= False
# #     for char in word:
# #         if char=="y":
# #             y_Exist= True
# #             break
# #     if y_Exist== True:
# #       print(word[::-1])    


# #list comprahension

# # y_Words =[i[::-1] for i in Poem.split() if "y" in i]
# # print(y_Words)
# # print(y_Words)


# import requests
# reposnse = requests.get("https://webscraper.io/test-sites")
# print(reposnse.status_code)
# code_type= "02"
# if reposnse.status_code==200:
#     if code_type== "01":
#         Lines= reposnse.text.splitlines()
        
#         for i in Lines:
#               if "<a " in i:
#                 print(i.strip())
#     else:
#         Lines= reposnse.text.splitlines()
#         for L in [i.strip() for i in Lines if "<a " in i]:
#          print(L)

#even squares

# Even_Squares= [i**2 for i in range(2,21,2)]
# print(Even_Squares)



print(",".join([str(i**2) for i in range(2,21,2)]))
