import threading
import queue
import time

# 1. La CODA dei compiti da fare (come RabbitMQ, ma in memoria)
coda_lavori = queue.Queue()

# 2. Il WORKER: prende un lavoro dalla coda e lo esegue
def operaio(nome_operaio):
    while not coda_lavori.empty():
        sito = coda_lavori.get()
        print(f"[{nome_operaio}] Sto analizzando {sito}...")
        time.sleep(1)  # Simula un lavoro lento da 1 secondo
        print(f"[{nome_operaio}] Finito {sito}!")
        coda_lavori.task_done()

# Mettiamo 6 siti nella coda
for i in range(1, 7):
    coda_lavori.put(f"Sito-Web-{i}")

inizio = time.time()

# 3. Creiamo 3 OPERAI (Thread) che lavorano CONTEMPORANEAMENTE
thread1 = threading.Thread(target=operaio, args=("Operaio-1",))
thread2 = threading.Thread(target=operaio, args=("Operaio-2",))
thread3 = threading.Thread(target=operaio, args=("Operaio-3",))

thread1.start()
thread2.start()
thread3.start()

# Aspettiamo che finiscano tutti
thread1.join()
thread2.join()
thread3.join()

print(f"Tutti e 6 i siti analizzati in {round(time.time() - inizio, 2)} secondi (invece di 6)!")
