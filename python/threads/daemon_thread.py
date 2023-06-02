import threading
def action(max):
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))
t = threading.Thread(target=action, args=(100, ), name='Daemon Thread')
t.daemon = True
t.start()
for i in range(10):
    print(threading.current_thread().name + ' ' + str(i))