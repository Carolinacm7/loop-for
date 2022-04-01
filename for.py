

# range(10) 0,1,2,3,4,5,6,7,8,9
# range (2,10)  2,3,4,5,6,7,8,9
# range(2,12,2) 2,4,6,8,10

mostrar = ""
for r1 in range(10):
    mostrar = mostrar + str(r1) + ","
print("range(10) -> ",mostrar)

mostrar = ""
for r2 in range(2,10):
    mostrar = mostrar + str(r2) + ","
print("range(2,10) -> ",mostrar)

mostrar = ""
for r3 in range(2,12,2):
    mostrar = mostrar + str(r3) + ","
print("range(2,12,2) -> ",mostrar)

mostrar = ""
for r4 in range(12,1,-2):
    mostrar = mostrar + str(r4) + ","
print("range(12,1,-2) ->",mostrar)
