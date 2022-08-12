# EvenNumbers=[]
# EvenNumbers=range(1,100,1)

# for number in EvenNumbers[::2]:
#     print(number)

Poem="Language Arts is a professional journal for elementary and middle school teachers and teacher educators. It provides a forum for discussions on all aspects of language arts learning and teaching, primarily as they relate to children in pre-kindergarten through the eighth grade. Issues discuss both theory and classroom practice, highlight current research, and review children’s and young adolescent literature, as well as classroom and professional materials of interest to language arts educators. (Published September, November, January, March, May, and July)"

print(Poem.split()[4][-1::-1])