input = ["1","3","5","7","9"]
output =[]
#print(len (input))
i=0
while i < len (input):
    j=i+1
    while j< len (input):
        #print(j)
        #print (input[i], input[j])
        output.append(input[i]+","+input[j])
        j+=1
    else:
        i += 1
print(output)