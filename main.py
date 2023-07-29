import time
import socket

try:
    import core
    import hdd
    import ram
    import operationsystem as os
except:
    print('//BSoD\\')
    print('BOS got error:\ncomputer module not found')
    print('//BSoD\\')
    time.sleep(4)



class pc:
    cpu = {'cores': core.cores, 'streams': core.streams}

    drive = {'memory': hdd.memory, 'count': hdd.count}

    RAM = {'memory': ram.memory, 'count': ram.count}


def run():
    
    if pc.RAM['memory'] < 1024:
        if pc.RAM['count'] != 'mb':
            print('/BSoD\\')
            print('Your RAM is not enough to run the system, or there is too much of it')
            print('/BSoD\\')
            time.sleep(4)
        else:
            print('//BSoD\\')
            print('Your RAM is not enough to start the system')
            print('//BSoD\\')
            time.sleep(4)
    else:
        if pc.drive['memory'] < 4 and pc.drive['count'] != 'gb' or pc.drive['memory'] < 4 and pc.drive['count'] != 'tb':
            print('//BSoD\\')
            print('Your hard drive does not have enough memory to start the system')
            print('//BSoD\\')
            time.sleep(4)
        else:
            #Лимиты
            global limit

            limit = pc.cpu['streams'] // pc.cpu['cores'] / 5

            print(f'{os.name} is loading...')
            time.sleep(limit * 3)
            
            while True:
                command = input(f'enter the desired command\n{os.un}@{socket.gethostname()}~')

                time.sleep(limit * 2)

                if command.lower() == 'ipconfig':
                    print(f'Your ip: {socket.gethostbyname(socket.gethostname())}')
                elif command.lower() == 'stats':
                    print(f'CPU:\n{pc.cpu}\nhard drive:\n{pc.drive}\nRAM:\n{pc.RAM}')
                else:
                    time.sleep(limit)
                    try:
                        exec('os.funcs.%s()' % command)
                    except:
                        print('This command does not exist!\n')


run()
