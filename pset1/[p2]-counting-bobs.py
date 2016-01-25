s = "bobobadsfadfbob"

bob_cntr = 0
for i in range (0,len(s)):
    print s[i]
    if s[i] == "b":
        if s[i+1:i+3] == "ob":
            bob_cntr+=1

print ("Number of times bob occurs is: " + str(bob_cntr))