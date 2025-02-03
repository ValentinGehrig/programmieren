width = int(input("Bitte breite eingeben: "))
height = int(input("Bitte Höhe eingeben: "))

for i in range(height):
    for  j in range(width):
        print(" x ", end="")
    print(" ")
    
print(" ")
print(" ")

count = 1
maxErreicht = False
for i in range(height*2):
    for  j in range(count):
        print(" x ", end="")
    print(" ")
    
    if(maxErreicht == False):
        count += 1
    else:
        count -=1
    if(count == height):
       maxErreicht = True; 

for i in range(1, height + 1):
    kugeln = i * 2  - 1
    leerzeichen = height - i
    line = " " * leerzeichen
    for j in range(kugeln):
        if j % 2 == 0:
            line += "x"
        else:
            line += "o"
    print(line)
print(" " * (height - 1) + "x")
print(" " * (height - 1) + "x")
