import sys, time, math, turtle, geometry
#is just useful stuff to have
addition = "addition"
#variable joka tekee ohjelmasta enemmän user friendly
factoriall = "factorial"
#sama kun yläpuolella
geometrr = "geometry"
yes = ["Yes", "1. Yes"]
no = {"No", "2. No"}
list = []
#lista vastausten tallentamissen ja .txt documenttiin printtaamiseen jos käyttäjä haluaa
additionlist = []
def f_print(srt):
    for let in srt:
        sys.stdout.write(let)
        sys.stdout.flush()
        time.sleep(0.05)
# mukavamman näköistä teksti printtausta

def factorial(x):
    fact = 1
    for num in range(2, x +1):
        fact *= num
    return fact
#kertoma funtio koska miksi ei0
#joka ei nököjään halua toimia
#wip

def summ(l):
  total = 0
  for val in l:
    total = total + val
  return total
#random function for addition
f_print("choose the operation")
print("")
f_print("1. addition")
print("")
f_print("2. substraction")
print("")
f_print("3. factorial")
print("")
f_print("4. geometry")
print("")
f_print("0 to exit")
#AAAAAAAAAAAAA

while True:
    print("")
    choice = input("operation: ")
    if choice == "1" or choice.lower() == addition:
        #addition
        while True:
            try:
                number = int(input(f_print("Num: ")))
            except ValueError:
                print("please give a number")
                continue
            else:
                additionlist.append(number)
                f_print("Do you want to add another number? ")
                print("")
                print("1. Yes")
                print("2. No")
                anser = input(" ")
                if anser == "yes" or anser == "yes" or anser == "1":
                    print("")
                    continue
                elif anser == "no" or anser == "No" or anser == "2":
                    break
                else:
                    print("")
                    f_print("give a proper answer")
                    print("")
        ans = summ(additionlist)   
        print(ans)
        addlist = ''.join(map(str,additionlist))
        var1 = "addition of numbers " + addlist + " is " + str(ans)
        list.append(var1)
        #welp this doesnt work
        # gotta fix summ to work with lists
    if choice == "3" or choice.lower() == factoriall:
        while True:
            try:
                number = int(input(f_print("Num: ")))
                #note to self, try to make f_print work with input without writing None
            except ValueError:
                print("please give a number")
                continue
            else:
                break
        factnum = factorial(number)
        f_print(f"Factorial of {number} is {factnum}")
        var1 = "factorial of " + str(number) + " is " + str(factnum)
        list.append(var1)
        #stuff happens here, dont ask me wat
    if choice == "4" or choice.lower() == geometrr:
        f_print("1. triangles")
        print("")
        choice = input("operation: ")
        if choice == "1" or choice.lower() == "Triangles":
            print("What type of triangle")
            f_print("1. equilateral triangle")
            print("")
            choice = input("")
            if choice == "1" or choice.lower() == "equilateral triangle":
                while True:
                    try:
                        lenght = int(input("Lenght of the triangle? "))
                    except ValueError:
                        print("please give a number: ")
                    else:
                        break
                geometry.draw_equilateral_triangle(lenght)

        
    if choice == "0":
        break
print(list)
f_print("Would you like to save your answers to a txxt document")
print("")
f_print("1. Yes")
print("")
f_print("2. No")
print("")
while True:
    #tektsi tiedostoon tallentaminen
    ans = input(("Answer: "))
    if ans == "1" or ans in yes:
        print("ok")
        print("")
        f = open("ans.txt", "w+")
        #magic
        for item in list:
            f.write(item+ "\n")
        f.close
        break
    elif ans == "2" or no:
        break
    else: 
        f_print("please answer correctly")
        print("")
        continue
print("Thank you for using this programm")