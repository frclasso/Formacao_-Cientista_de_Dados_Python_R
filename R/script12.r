# if
a = 10
   b = 20
if (a < b){
   print("verdadeiro")
}else {
   print("falso")
}
print("==========================================")
#ifelse
x = ifelse(a > 10, "A é maior", "B é maior")
print(x)
print("==========================================")
# loop for
for (i in 1:10){
    print(i)
}
print("==========================================")
a =1
while(a <= 10){
    print(a)
    a = a + 1
}
print("==========================================")

parouimpar = function(x) {
    return(ifelse(x %% 2 == 0, "Par", "impar"))
}
print(parouimpar(5))