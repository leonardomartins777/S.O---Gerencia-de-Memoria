class Descritor_processo:
    def __init__(self, estado_atual,prioridade,inicio_memoria,tamanho_memoria,arquivos_abertos,tempo_cpu,proc_pc,proc_sp,proc_acc,proc_rx,proximo):
        self.estado_atual = estado_atual 
        self.prioridade = prioridade
        self.inicio_memoria = inicio_memoria
        self.tamanho_memoria = tamanho_memoria
        self.arquivos_abertos = arquivos_abertos
        self.tempo_cpu = tempo_cpu
        self.proc_pc = proc_pc 
        self.proc_sp = proc_sp
        self.proc_acc = proc_acc
        self.proc_rx = proc_rx
        self.proximo = proximo

    
    