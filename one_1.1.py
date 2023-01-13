#below line is read input from user
l=input()
#replace method is indirectly used to remove chaar from string

l=l.replace(l[-1],"")
l=l.replace(l[-1],"")
#reverse the string using ::-1 
print(str(l[::-1]))