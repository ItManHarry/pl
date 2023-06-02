import threading
def action(max):
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))
threading.Thread(target=action, args=[100], name='New Thread').start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=[100], name='Joined Thread')
        jt.start()
        jt.join()
    print(threading.current_thread().name+' '+str(i))