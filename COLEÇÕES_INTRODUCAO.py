#coleções sao variaveis que armazenam mais de um valor na variavel
#caracteristicas da colecao:
    #os objetos da minha colecao podem ser de um determinado tipo ou podem ser de tipos diferentes
    #toda coleção é um elemento ITERÁVEL (que pode ser percorrido, ex: através de um "FOR")

#Existem varios tipos de coleções
    #LISTA (mais poderosa das coleções) por que?
        #ela permite varios tipos de operações
        #características
            #mutável (colocar mais de um elemento)
            #expansível
            #ordenadas
            #elementos podem ser acessados por índice
            #acomodam tipos de dados diferentes
            #permite duplicados
            
print('LISTA!')
minhaLista = ['água', 'café', 'palatinose', 'música']
print(minhaLista)
print(type(minhaLista))

                 #0     #1         #2          #3       #4
#ou              #-5    #-4        #-3         #-2      #-1
minhaLista = ['água', 'café', 'palatinose', 'música','água']
#os elementos da linha são acessados por índice começando do '0'

print(minhaLista[2])
print(minhaLista[-3])

#slicing de lista (acessar um pedaço da lista)
pequenaLista = minhaLista[1:3+1] #1:3+1 conceito de intervalo aberto [de:ate+1]
print(pequenaLista)

#mostrando toda a lista com len
print(len(minhaLista))

#acrescentando item ao final da lista
minhaLista.append('canela')
print(minhaLista)

#inserindo item em local específico 3 ficaria o quarto numero: 0 1 2 3 4 5
minhaLista.insert(3, 'nibs de cacau')
print(minhaLista)

#removendo o ultimo item da lista
minhaLista.pop()
print(minhaLista)

#removendo item específico
minhaLista.pop(4)
del minhaLista[-1]
print(minhaLista)
minhaLista.remove('nibs de cacau')
print(minhaLista)

#limpando os dados da lista
minhaLista.clear()
print(minhaLista)

print('Outra Lista')
outraLista = list(('chantilly', 'baunilha'))
print(outraLista)
print(type(outraLista))

print('Extendendo uma lista - acrescentar uma lista ao final')
minhaLista = ['cafe', 'acucar', 'agua']
print(minhaLista)
minhaLista.extend(outraLista)
print(minhaLista)

pequenosMimos = ['canela', 'raspas limao']
meusComplementos = pequenosMimos + outraLista
print(meusComplementos)
print(pequenosMimos)
print(outraLista)

print('Encontrando elementos na lista')
if 'chantilly' in meusComplementos:
    print('Oba tem chantilly')


#percorrer a lista
print('Percorrendo a lista e verificando elemento a elemento')
for elemento in meusComplementos:
print(elemento)
if elemento == 'raspas limao':
print('------> obs: raspas sao amargas')

print('Ordenacao')
#lista permite ordenacao
meusComplementos.sort()
print(meusComplementos)
#o sort so funciona SE TODOS OS ELEMENTOS DA LISTA FOREM DO MESMO TIPO

novaLista = ['Mel', 19, True, 1971, 'Albert Einsten']
print(novaLista)
novaLista.sort()

