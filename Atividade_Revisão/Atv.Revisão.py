questão 1-
n = 0
while cont<100:
 n = n + 2
 print "%d" % (n)

questão 2- 
VPo = list()
VNe = list()
for i in range(6):
    valor = int(input())
    if (valor < 0): ln.append(valor)
    else:vp.append(valor)
print("Valores Positivos: ",VPo )
print("Valores Negativos: ",VNe)

questão 3-
v = int(input())
for i in range(n):
    v1 = float(input())
    v2 = float(input())
    v3 = float(input())

print(((v1*2)+(v2*3)+(v3*5))/10)

questão 4-
po = 0
ma = 0
for i in range(15):
    n = int(input("imforme o valor: "))
    
    if n > ma:
        ma = n
        po = i+1
        
print("%d\n %d"%(ma,po))

questão 5-
lista = list()
for i in range(6):
    valor = float(input("valor: "))
    if (valor >=1):
        lista.append(valor)
soma = sum(lista)
print('Média dos valores positivos: %.1f' %(soma/len(lista) ))

questão 6-

qtdPizza = int(input())
prcPizza = float(input())
prcTotal = qtdPizza * prcPizza
imposto = 8 * prcPizza / 100
total = prcPizza + imposto
print(total)

questão 7-

vlr = int(input("informe o valor: "))
ttl = list()
ttln = 1

for i in range(1,vlr+1,1):
    ttln = ttln*i

print(ttln)

questão 8-

b = int(input("digite a base: "))
e = int(input("digite o expoente: "))

print(b**e)


questão 9-

a = int(input("informe o núúmero: "))
soma = 0
for i in range(1, a):
    soma += i
    
print(soma)

questão 10-

nCigarro = int(input("Número de Cigarros: "))
anosF = int(input("Anos Fumando: "))
totalCigarro = (anosF * 365)*nCigarro
qtdDias = (totalCigarro * 10)/24

print (qtdDias)

questão 11-
j = int(input("Número: "))
o = str(j)
print (len(o))

questão 12-

totald = list()
vlrpresta = float(input("digite o valor da prestação: "))
while (vlrpresta != 0):
    diast = int(input())
    if (diast==0):
        print("O valor total da Prestação: R$ %.2f" %(vlrpresta))
        totald.append(vlrpresta)
    else:
        j = vlrpresta+(10*0.3)+((10*0.01)*diast)
        print("O valor total da Prestação: R$ %.2f" %(j))
        totald.append(j)
    vlrpresta = float(input())


calculoF = sum(totald)

print("Total de Prestações pagas: R$ %.2f" %(calculoF))

















