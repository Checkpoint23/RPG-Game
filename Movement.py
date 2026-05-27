import MovementManager
import random
import startBattle

rooms = []
inventory=[]
questlog=[]

class moving:
    def addRoom(x,y,worldType,treasure,encounterPossible,encounterChance,desc,gate,boss,worldGate,quest):
        global rooms
        rooms.append((x,y,worldType,treasure,encounterPossible,encounterChance,desc,gate,boss,worldGate,quest,False))
        ##Tag out when not testing errors
#        for room in rooms:
#            print(f"An X of {room[0]}")
 #           print(f"A Y of {room[1]}")
  #          print(f"World {room[2]}")
   #         if room[3] == "none":
    #            print(f"No treasure")
     #       else:
      #          print(f"A treasure of {room[3]}")
       #     if room[4] == True:
        #        print("With a possible encounter,")
         #       print(f"And a chance of {room[5]},")
          #  else:
           #     print("With no possible encounter")
            #print(f"With a description of {room[6]},")
#           if room[7] != "none":
 #               print(f"With a gate requiring the {room[7]} key(s),")
  #          if room[8] != "none":
   #             print(f"With a boss called {room[8]}")
    #        if room[9] != "none":
     #           print(f"And is a world gate to world {room[9]}")
      #      print("")
    def roomFunctions(currentRoomX, currentRoomY):
        for room in rooms:
            if room[0] == currentRoomX and room[1] == currentRoomY:
                if room[11] != True:
                    beenHere = False
                else:
                    beenHere = True
                room[11] = True
                desc = room[6]
                encounter = room[4]
                encounterChance = room[5]
                world = room[2]
                treasure = room[3]
                quest = room[10]
                gate = room[7]
        if beenHere == False:
            print(desc)
        else:
            print("You've been here before!")
        if encounter == True and beenHere == False:
            doAFight = random.randint(1,100)
            if doAFight <= encounterChance:
                startBattle.battle.selectEnemyWorld(world=world)
                startBattle.battle.runBattle()
        elif beenHere == True:
            doAFight = random.randint(1,200)
            if doAFight <= encounterChance:
                startBattle.battle.selectEnemyWorld(world=world)
                startBattle.battle.runBattle()
        if treasure != "none" and beenHere == False:
            if treasure == "R":
                print("You got the Red Key!")
                inventory.append("Red Key")
            if treasure == "G":
                print("You got the Green Key")
                inventory.append("Green Key")
            if treasure == "B":
                print("You got the Blue Key")
                inventory.append("Blue Key")
            if treasure == "Y":
                print("You got the Yellow Key")
                inventory.append("Yellow Key")
            if treasure == "H-5":
                print("PLACEHOLDER REMOVE LATER")
            if treasure == "G-50":
                print("PLACEHOLDER REMOVE LATER")
                inventory.append("50 Gold Pieces")
            if treasure == "Ring":
                print("Ring has been added to your inventory!")
                inventory.append("Ring")
        if quest != "none":
            if quest == "Ring" and beenHere != False:
                print("I've lost my precious ring! Can you find it for me! If you do, I'll teach you about hitting stronger consistently!")
                print("This seems important. Quest added to your questlog!")
                questlog.append("Help find the ladies missing ring! If you do, you'll be taught how to hit stronger more consistently.")
            else:
                for i in questlog:
                    if i == ("Help find the ladies missing ring! If you do, you'll be taught how to hit stronger more consistently."):
                        for i in inventory():
                            if i == "Ring":
                                print("You've found my precious ring! Thank you so much! Let me teach you.")
                                inventory.remove(i)
                                #minDamage += 1
                                #maxDamge += 1
                                print("Your minimum and maximum damage increased by 1!")
        if gate != "none":
            print("We have a gate")
            if gate == "RGBYN":
                numberOfKeys = 0
                for i in inventory:
                    if i == "Red Key":
                        print("You have the red key.")
                        numberOfKeys += 1
                    if i == "Blue Key":
                        print("You have the blue key")
                        numberOfKeys += 1
                    if i == "Yellow Key":
                        print("You have the yellow key")
                        numberOfKeys += 1
                    if i == "Green Key":
                        print("You have the green key.")
                        numberOfKeys += 1
                if numberOfKeys == 4:
                    print("You have all the keys. The gate is unlocked.")
                    for room in rooms:
                        if room == "RGBYN":
                            room = "none"
                    for i in inventory:
                        if i == "Red Key":
                            inventory.remove(i)
                        if i == "Blue Key":
                            inventory.remove(i)
                        if i == "Yellow Key":
                            inventory.remove(i)
                        if i == "Green Key":
                            inventory.remove(i)
    def fromRoom(currentRoomX, currentRoomY):
        global rooms
        allowedRooms = []
        totalRooms = 1
        for room in rooms:
            if room[0] == currentRoomX - 1 and room[1] == currentRoomY:
                allowedRooms.append("E")
                totalRooms += 1
            if room[0] == currentRoomX + 1 and room[1] == currentRoomY:
                allowedRooms.append("W")
                totalRooms+=1
            if room[1] == currentRoomY - 1 and room[0] == currentRoomX:
                for room in rooms:
                    if room == "RGBYN":
                        print("You cannot go north from here. It is blocked by a gate.")
                    else:
                        allowedRooms.append("N")
                        totalRooms += 1
            if room[1] == currentRoomY + 1 and room[0] == currentRoomX:
                allowedRooms.append("S")
                totalRooms += 1
            exitRoom = False
            while exitRoom == False:
                print("You can go to areas:")
                for rooms in allowedRooms:
                    if rooms == "N":
                        print("North from here")
                for rooms in allowedRooms:
                    if rooms == "E":
                        print("East from here, (E)")
                for rooms in allowedRooms:
                    if rooms == "S":
                        print("South from here, (S)")
                for rooms in allowedRooms:
                    if rooms == "W":
                        print("West from here, (W)")
                print("Please pick which room corrosponding to the letter.")
                roomChosen = input("")
                if roomChosen in allowedRooms:
                    if roomChosen == "N":
                        print("You move North.")
                    if roomChosen == "E":
                        print("You move East")
                    if roomChosen == "S":
                        print("You move South.")
                    if roomChosen == "W":
                        print("You move West.")
                        MovementManager.roomMovement.SetCurrentRoom(currentRoomX + 1, currentRoomY)
                    exitRoom = True
                    return
                else:
                    print("bro")