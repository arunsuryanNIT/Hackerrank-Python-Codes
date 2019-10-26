status = ''
while(True):
    var = input("Query ?\n")

    if(var == 'help'):
        print("start for starting the car\n")
        print("stop for stopping\n")
        print("quit to exit\n")

    elif var == 'start':
        print("Car started....\n")
        status = 'Started now'

    elif var == 'stop':
        print("car stopped....\n")
        status = 'stopped'

    elif var == 'status':
        print(status)
        
    else:
        exit(0)
