num1=int(input("digite o primeiro numero"))
operacao=input("insira a sua operacao(+,-,*,/)")
num2=int(input("digite o segundo numero"))

if operacao=='+':
    resultado=num1+num2
    print(num1,operacao,num2,"=",resultado)

elif operacao=='-':
    resultado=num1-num2
    print(num1,operacao,num2,"=",resultado)

elif operacao=='*':
    resultado=num1*num2
    print(num1,operacao,num2,"=",resultado)
    
elif operacao=='/':
    resultado=num1/num2
    print(num1,operacao,num2,"=",resultado)