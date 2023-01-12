import threading
def worker(n, sema):
    sema.acquire()
    print('Working : ', n)
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema))
    t.start()
for n in range(nworkers):
    sema.release()