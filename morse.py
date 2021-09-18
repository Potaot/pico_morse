from machine import Pin
import time

led = 15

unit = 0.2

led = Pin(led, Pin.OUT)

a = [1, 3]
b = [3, 1, 1, 1]
c = [3, 1, 3, 1]
d = [3, 1, 1]
e = [1]
f = [1, 1, 3, 1]
g = [3, 3, 1]
h = [1, 1, 1, 1]
i = [1, 1]
j = [1, 3, 3, 3]
k = [3, 1, 3]
l = [1, 3, 1, 1]
m = [3, 3]
n = [3, 1]
o = [3, 3, 3]
p = [1, 3, 3, 1]
q = [3, 3, 1, 3]
r = [1, 3, 1]
s = [1, 1, 1]
t = [3]
u = [1, 1, 3]
v = [1, 1, 1, 3]
w = [1, 3, 3]
x = [3, 1, 1, 3]
y = [3, 1, 3, 3]
z = [3, 3, 1, 1]
alphabet = {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g, "h":h, "i":i, "j":j, "k":k, "l":l, "m":m, "n":n, "o":o, "p":p, "q":q, "r":r, "s":s, "t":t, "u":u, "v":v, "w":w, "x":x, "y":y, "z":z}

msg = list(input("What message would you like to send?\n>>>").lower())


for i in range(len(msg)):
    try:
        if msg[i] != " ":
            for j in range(len(alphabet[msg[i]])):
                led.on()
                time.sleep(unit*(alphabet[msg[i]][j]))
                led.off()
                time.sleep(unit)
            led.off()
            time.sleep(unit*2)
        else:
            time.sleep(unit*6)
    except:
        print("Invalid message.")
