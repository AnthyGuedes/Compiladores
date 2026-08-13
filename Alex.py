
caminho = r'C:\Users\laboratorio\Desktop\psata\configAfd.md'

estados = [
    
]

estadosfinais = [
    
]

simbolos = [
    
]

regrastransicao = [
    
]

config = open(caminho, encoding='utf-8')
estados = config.readline().strip().split(' ')
estadoInicial = estados[0]
print(estados)

simbolos = config.readline().strip().split(' ')
print(simbolos)

estadosfinais = config.readline().strip().split(' ')
print(estadosfinais)

linha = config.readline()
while linha:
        regrastransicao.append(linha.strip().split(' '))
        linha = config.readline()
    
print(regrastransicao)

config.close()
 


def reconhecerTermo(lexemas):
    estadoAtual = estadoInicial
    for char in lexemas:
        if char in simbolos:
            estadoAtual = regrastransicao[estadoAtual][char]
        else:
            return False
    return estadoAtual in estadosfinais 
    