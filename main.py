import time
from processo import Processo
from descritor_processo import Descritor_processo
#from ler_entrada import *
import ler_entrada
from mmu import Mmu
import mmu

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
#pagina_5 = 20-23
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
def swap(elem,mmu,tabela_de_paginas):
    temp = (list(mmu._memoria_principal_posicoes[0])[0])
    temp_proces = mmu._memoria_principal_posicoes[0][temp][2]
    page_to_frame = -1
    indice_dict = -1
    print("mmu._memoria_secundaria_posicoes",mmu._memoria_secundaria_posicoes)
    for x in range(len(mmu._memoria_secundaria_posicoes)):
        for y in mmu._memoria_secundaria_posicoes[x]:
            print("ysecundaria_posicoes[x][y]",y,mmu._memoria_secundaria_posicoes[x][y])
            if (len(mmu._memoria_secundaria_posicoes[x][y][2]) == 0) and page_to_frame == -1:
                indice_dict = y
                page_to_frame = x
    print("PTF,INDICE",page_to_frame,indice_dict)
    tupla_to_list = list(mmu._memoria_secundaria_posicoes[page_to_frame][indice_dict])
    tupla_to_list[2] = temp_proces                            
    mmu._memoria_secundaria_posicoes[page_to_frame][indice_dict] = tuple(tupla_to_list)
    mmu._memoria_principal_posicoes[0][temp][2] = elem
    return True

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
    mmu._iniciar_memoria_secundaria(lista_de_processos)
    # for x in mmu._memoria_logica_posicoes:
    #     print(x)
    i_lista_proc = 0
    i_lista_proc_exec = 0
    #i_lista_proc_block = 0
    for x in lista_de_processos:
        del x.instrucoes[0]
    print("loop")
    a = 0    
    while a < 10:
        a += 1
        print("loop_inicio")
        
        if len(lista_de_processos) > 0:
            lista_de_processos_executando.append(lista_de_processos[i_lista_proc])
            del lista_de_processos[i_lista_proc]
        
        for x in lista_de_processos_bloqueados:
            #print("pdovjspdoivjpiov",x.tempo_bloqueio)

            if tempo >= x.tempo_bloqueio:
                x.tempo_bloqueio = 0
                del x.instrucoes[0]
                lista_de_processos.append(x)
                lista_de_processos_bloqueados.remove(x)
            
        if len(lista_de_processos_executando) > 0:
            proc_temp = lista_de_processos_executando[i_lista_proc_exec]
            if len(proc_temp.instrucoes) > 0:
                if "I" not in proc_temp.instrucoes[0][0]:
                    regiao_logica = proc_temp.instrucoes[0][1]
                    page_to_frame = -1
                    for x in range(len(mmu._memoria_principal_posicoes)):
                        for y in mmu._memoria_principal_posicoes[x]:
                            print("y",y)
                            if (len(mmu._memoria_principal_posicoes[x][y][2]) == 0) and page_to_frame == -1:
                                page_to_frame = x
                    if page_to_frame == -1:
                        swap(regiao_logica,mmu,tabela_de_paginas)
                    else:
                        indice_logico = (int(proc_temp.instrucoes[0][1]) - (int(proc_temp.instrucoes[0][1]) % tamanho_frames)) / tamanho_frames
                        tabela_de_paginas[page_to_frame] = int(indice_logico)
                        chave = list(mmu._memoria_principal_posicoes[page_to_frame])[0]
                        tupla_to_list = list(mmu._memoria_principal_posicoes[page_to_frame][chave])
                        tupla_to_list[2] = [proc_temp.instrucoes[0]]
                        print("AQUI",tupla_to_list)
                        mmu._memoria_principal_posicoes[page_to_frame][chave] = tuple(tupla_to_list)
                        executar_uma_instrucao()
                        del proc_temp.instrucoes[0]
                        lista_de_processos.append(proc_temp)
                        del lista_de_processos_executando[i_lista_proc_exec]

                else:
                    proc_temp.tempo_bloqueio = tempo + int(proc_temp.instrucoes[0][1])
                    lista_de_processos_bloqueados.append(proc_temp)
                    del lista_de_processos_executando[i_lista_proc_exec]

            

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
        print("TABELA-DE-PAGINAS",tabela_de_paginas)

    
        
    
    
    
    


main()