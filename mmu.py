class Mmu:
    _memoria_principal_posicoes = []
    _memoria_secundaria_posicoes = []
    _memoria_logica_posicoes = []
    
    def __init__(self, tamanho_frames,tamanho_pages,memoria_principal):
        self.tamanho_frames = tamanho_frames
        self.tamanho_pages = tamanho_pages
        self.memoria_principal = memoria_principal
        #self.memoria_secundaria = memoria_secundaria
    def criar_frame_pagina(self,end_logico,process_name,ops):
        dicionario_ = {}

        dicionario_[end_logico] = (process_name,ops)
        return dicionario_  
    def _iniciar__memoria(self):
        
        mem = self.memoria_principal/self.tamanho_frames
        #print("MEM",mem)
        count = 0
        while(count < mem):
            dic = {}
            ini = self.tamanho_frames * count
            fim = ini + (self.tamanho_frames -1)
            #print("INI,FIM",ini,fim)
            dic[count] = (ini,fim,[])
            self._memoria_principal_posicoes.append(dic)
            
            
            count += 1

    def _iniciar_memoria_logica(self,lista_de_processos):
        n = len(lista_de_processos)
        
        count  = 0
        count2  = 0
        lista_t = 0
        while(count2 < n):
            lista_t += int(lista_de_processos[count2].tamanho)
            count2 += 1
        mem = lista_t/self.tamanho_pages
        print(mem)
        while(count < mem):
            dic = {}
            ini = self.tamanho_pages * count
            fim = ini + (self.tamanho_pages -1)
            #print("INI,FIM",ini,fim)
            dic[count] = (ini,fim,[])
            self._memoria_logica_posicoes.append(dic)
            
            
            count += 1
        
    
        
    
        
