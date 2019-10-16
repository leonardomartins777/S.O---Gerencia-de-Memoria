import time
from processo import Processo
from descritor_processo import Descritor_processo
#from ler_entrada import *
import ler_entrada
from mmu import Mmu

entrada = 'teste_entrada2.txt'
saida = 'teste_saida.txt'

#posicoes memoria principal
memoria_principal = 8
#(frames) memoria principal
tamanho_frames= 4
#RAM
#frame_0 = 0-3 
#frame_1 = 4-7
#frame_2 = 8-11
#frame_3 = 12-15
#posicoes(frames) memoria secundaria
#memoria_secundarias = 4

#LOGICA
#pagina_0 = 0-3 
#pagina_1 = 4-7
#pagina_2 = 8-11
#pagina_3 = 12-15
#pagina_4 = 16-19
#pagina_5 = 22-23
#pagina_6 = 24-27
#pagina_7 = 28-31


tabela_de_paginas = {}

lista_de_descritores_de_processos = []
lista_de_processos = []#livres_aptos
lista_de_processos_bloqueados = []
lista_de_processos_executando = []
max_de_processos = 20
num_processos = 0
tempo = 0

def adicionar_descritor(estado_atual,prioridade,inicio_memoria,tamanho_memoria,arquivos_abertos,tempo_cpu,proc_pc,proc_sp,proc_acc,proc_rx,proximo):
    novo_descritor = Descritor_processo(estado_atual,prioridade,inicio_memoria,tamanho_memoria,arquivos_abertos,tempo_cpu,proc_pc,proc_sp,proc_acc,proc_rx,proximo)
    if len(lista_de_descritores_de_processos) < max_de_processos:
        lista_de_descritores_de_processos.append(novo_descritor)
        return True
    else:
        return False
def executar_uma_instrucao():
    time.sleep(0.5)
    global tempo
    tempo += 0.5


def main():
    dicionario_de_processos = ler_entrada.pegar_processos(entrada)
    #criando_processos

    for chave in dicionario_de_processos:
        processo_instrucoes = dicionario_de_processos[chave] 
        nome = chave
        tamanho = processo_instrucoes[0][1]

        
        processo_temp = Processo(tamanho,nome,processo_instrucoes)
        lista_de_processos.append(processo_temp)
    #num_processos = len(lista_de_processos)

    # for x in lista_de_processos:
    #     x._print_processo()
    mmu = Mmu(tamanho_frames,tamanho_frames,memoria_principal)

    mmu._iniciar__memoria()
    # for x in mmu._memoria_principal_posicoes:
    #     print(x)

    mmu._iniciar_memoria_logica(lista_de_processos)
    # for x in mmu._memoria_logica_posicoes:
    #     print(x)
    i_lista_proc = 0
    i_lista_proc_exec = 0
    #i_lista_proc_block = 0
    for x in lista_de_processos:
        del x.instrucoes[0]
    print("loop")    
    while True:
        print("loop_inicio")
        
        if len(lista_de_processos) > 0:
            lista_de_processos_executando.append(lista_de_processos[i_lista_proc])
            del lista_de_processos[i_lista_proc]
        
        for x in lista_de_processos_bloqueados:
            print("pdovjspdoivjpiov",x.tempo_bloqueio)
            if tempo >= x.tempo_bloqueio:
                x.tempo_bloqueio = 0
                del x.instrucoes[0]
                lista_de_processos.append(x)
                lista_de_processos_bloqueados.remove(x)
            
        if len(lista_de_processos_executando) > 0:
            proc_temp = lista_de_processos_executando[i_lista_proc_exec]
            del lista_de_processos_executando[i_lista_proc_exec]
            if len(proc_temp.instrucoes) > 0:
                if "I" not in proc_temp.instrucoes[0][0]:
                    regiao_logica = proc_temp.instrucoes[0][1]
                    page_to_frame = -1
                    for x in range(len(mmu._memoria_principal_posicoes)):
                        if (len(mmu._memoria_principal_posicoes[x][3]) == 0):
                            page_to_frame = x
                    if page_to_frame == -1:
                        
                    executar_uma_instrucao()
                    del proc_temp.instrucoes[0]
                    lista_de_processos.append(proc_temp)
                else:
                    proc_temp.tempo_bloqueio = tempo + int(proc_temp.instrucoes[0][1])
                    lista_de_processos_bloqueados.append(proc_temp)
            

        print("lista_de_processos")
        for x in lista_de_processos:
            x._print_processo()
        print("lista_de_processos_bloc")
        for x in lista_de_processos_bloqueados:
            x._print_processo()
        print("lista_de_processos_exec")
        for x in lista_de_processos_executando:
            x._print_processo()
        if len(lista_de_processos) == 0 and len(lista_de_processos_bloqueados) == 0 and len(lista_de_processos_executando) ==0:
            break
        print(len(lista_de_processos) , len(lista_de_processos_bloqueados) , len(lista_de_processos_executando))
        print("TEMPO",tempo)
        executar_uma_instrucao()

    
        
    
    
    
    


main()