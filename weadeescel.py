text="="
for i in range (4,61):
    text=text+("SI(V"+str(i)+">5;$B"+str(i)+";0)+")
text=text[:-1]
print (text)
