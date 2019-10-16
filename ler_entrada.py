
entrada = 'teste_entrada.txt'
saida = 'teste_saida.txt'

def pegar_arq_entrada():
    return open('teste_entrada.txt', 'r')




def pegar_arq_saida():
    return open('teste_saida.txt', 'w')

def pegar_processos(entrada):
    dict_processos = {}
    arq_entrada = open(entrada, 'r')
    texto_entrada = arq_entrada.readlines()

    for linha in texto_entrada:
        processo = ""
        operacao = ""
        instrucao = ""
        x = 0
        
        while linha[x] != ' ':
            processo += linha[x]
            x += 1
        x += 1
        while linha[x] != ' ':
            operacao += linha[x]
            x += 1
        x+=1
        while x < len(linha):
            if linha[x] != '\n':
                instrucao += linha[x]
            x+=1
        if processo not in dict_processos:
            lista = [(operacao,instrucao)]
            dict_processos[processo] = lista
        else:
            lista = dict_processos[processo]
            lista.append((operacao,instrucao))
            dict_processos[processo] = lista
    
    arq_entrada.close()
    return dict_processos
    
    


# texto_saida = []
# texto_entrada = arq_in.readlines()
# arq_in.close()
# arq_out.close()
# texto.append('Lista de Alunos\n')
# texto.append('---\n')
# texto.append('João da Silva\n')
# texto.append('José Lima\n')
# texto.append('Maria das Dores')
# arq.writelines(texto)
# arq.close()