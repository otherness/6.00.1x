s = "aabbcciddee"

vowels = ("a","e","i","o","u")
vowels_cntr = 0
for i in s:
    if i in vowels:
        vowels_cntr+=1

print ("Number of vowels: " + str(vowels_cntr))