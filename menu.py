def menu():
    def oneplayer():
        print("ready to start?")

    def twoplayer():
        print("you can do it together")

    def online ():
        print("lets-a-gooooooooooooooo")

    loop = True
    while loop== True:
        print("welcone to Super Mario Sunshine")
        print("(1) for 1-player")
        print("(2) for 2-player")
        print("(3) for Options")
        print("(4) to Leave. bye")


        choic = int(input("pick option 1,2,3,4, yahoo"))
        if  choic == 1:
            print("1-player starting")
            oneplayer()
        elif choic == 2:
            print("2-player starting")
            twoplayer()
        elif choic == 3:
            print("here are the options")
        elif choic == 4:
            print("bye bye")
            loop = False
        elif choic == 5:
                print("super secret online mode")
                online()
        else:
            print("invalid option")
