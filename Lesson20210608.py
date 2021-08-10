#for x in range(11):
#    print(x)

#for x in range(4,56):
#    print(x)

#for x in range(0,201,10):
#   print(x)

# for x in range(4):
#output = ""
#for y in range(6): 
#    output= "* " + output        
# 0 "* "
# 1 "* * "
# 2 "* * * "
# ..6 "* * * * * * "
#print(output)

#Exercise 1
#output = ""
#for x in range(4):
#    output = ""
#    for y in range(6): 
#        output= "* " + output  
#    print(output)

#Exercise 2
#output = ""
#for x in range(6):
#    output = ""
#    for y in range(x): 
#        output= "* " + output  
#    print(output)

#Exercise 3
#output = ""
#for x in range(5):
#    output = ""
#    for y in range(x): 
#        output= "* " + output  
#    print(output)


for x in range(3,0,-1):
    output = ""
    for y in range(x): 
        output= "* " + output  
    print(output)

#Exercise 4
#output = ""
#for x in range(6):
#    output = ""
#    for y in range(6): 
#        if x<= y:
#            output= "  " + output
#        else:
#            output= "* " + output
#    print(output)