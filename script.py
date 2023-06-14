# def average(n):
#     return sum(n) / len(n)
    
# n = int(input("n ="))
# s =0.0
# for i in range(1,n+1):
#     x=float(input("number" + str(i) + " = "))
#     s += x
# m = s/n
# print("average = " , m)
# __________________
# [Complex data type]:
# real = float(input("real = "))
# imaginary = float(input("imaginary = "))
# complex_number = str(real) + '-' + str(imaginary) + 'j'

# print("Complex number formed: ", complex_number)
#____________________
# tedad = 0
# count = 0.0
# x = float(input("x = "))
# while x != -1:
#     count = count + x
#     tedad = tedad +1
#     x = float(input("x = "))
# print(count / tedad)
#___________________
#bazi hads adad
# import random
# javab = random.randint(1,1000)

# hads = int(input("waht is your hads??"))

# while hads != javab:
#     if hads > javab:
#         print("bozorge ha")
#     elif hads < javab:
#         print('kochike ha')
#     hads = int(input("what is your hads?"))
#     if hads == javab:
#         break
# print("you ween")
#___________________
#ax bazi bala
# a,c = (1,1000)
# import random
# hads = random.randint(a,c)
# print(hads)
# javab = input("Dorost ast?")
# while javab != "d":
#     if javab == "b":
#         a = hads
#         print("hooooffffff")
#         hads = random.randint(a,c)
#         print(hads)
#         javab = input("Dorost ast?")
#     if javab == "k":
#         c = hads
#         print("hooooofffff")
#         hads = random.randint(a,c)
#         print(hads)
#         javab = input("dorost ast?")
#     if javab == "d":
#         break
# print("yesss")
#____________________________
#calculator
# def jam(a,c):
#     return a + c
# def kam(a,c):
#     return a - c
# def zarb(a,c):
#     return a * c
# def tqsim(a,c):
#     return a / c
# def tavan(a,c):
#     return a ** c 
# def mqsom(a,c):
#     return a % c
# print("0.0")
# a = float(input("Adade Aval : "))
# b = input("Amale Morde Nazar : ")
# while b == "end" :
#     print("OH! End. " "\nGlad To See You <3 (:")
#     break
# c = float(input("Adade Dovom : "))
# while b != "end":
#     if b == "+":
#         a = jam(a,c)
#         print("a + c = " , a)
#         b = input("Amale Morde Nazar : ")
#         if b == "end":
#             print("OH! End. " "\nGlad To See You <3 (:")
#             break
#         c = float(input("Adade Dovom : "))
#     elif b == "-":
#         a = kam(a,c)
#         print("a - c = " , a)
#         b = input("Amale Morde Nazar : ")
#         if b == "end":
#             print("OH! End. " "\nGlad To See You <3 (:")
#             break
#         c = float(input("Adade Dovom : "))
#     elif b == "*":
#         a = zarb(a,c)
#         print("a * c = " , a)
#         b = input("Amale Morde Nazar : ")
#         if b == "end":
#             print("OH! End. " "\nGlad To See You <3 (:")
#             break
#         c = float(input("Adade Dovom : "))
#     elif b == "/":
#         a = tqsim(a,c)
#         print("a / c = " , a)
#         b = input("Amale Morde Nazar : ")
#         if b == "end":
#             print("OH! End. " "\nGlad To See You <3 (:")
#             break
#         c = float(input("Adade Dovom : "))
#     elif b == "**":
#         a = tavan(a,c)
#         print("a ** c = " , a)
#         b = input("Amale Morde Nazar : ")
#         if b == "end":
#             print("OH! End. " "\nGlad To See You <3 (:")
#             break
#         c = float(input("Adade Dovom : "))
#     elif b == "%":
#         a = mqsom(a,c)
#         print("a % c = " , a)
#         b = input("Amale Morde Nazar : ")
#         if b == "end":
#             print("OH! End. " "\nGlad To See You <3 (:")
#             break
#         c = float(input("Adade Dovom : "))
#     if b == "end":
#         print("OH! End. " "\nGlad To See You <3 (:")
#     else:
#         print("OH! Error!")
#         break
#________________________________
#project1
# print("welcome")
# a = input("whats's name of city you grew up in ? \n")
# x = input("what's your pet name ? \n")
# print("your band name could be" , a ,x )
#______________________________________
#tabe average dast saz
# def average(a,b):
#     return a / b 
# b = int(input("Tedad =\n"))
# a = 0.0
# for i in range(1,b+1):
#     x = float(input("Number" + str(i) + " = \n"))
#     a = a + x
# m = average(a,b)
# print("average" , m)
#//////////////////////////////////////////
