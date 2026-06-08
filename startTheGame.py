import MovementManager
import Movement
import json
import startBattle
from pathlib import Path


class start:
    FILE_PATH = Path("Save1.json")
    print("Welcome to the unamed RPG game! Current names include Goblin game, RPG Game, etc")

    if FILE_PATH.is_file():
        print("You appear to have played before.")
        choice = "unchosen"
        while choice != "C" and choice != "N":
            print("Do you want to:")
            print("Start a new game, getting rid of your old file? (N)")
            print("Or")
            print("Continue with your current save? (C)")
            choice = input("")
        if choice == "C":
            print("Good choice! Reverting to your last save file.")
            with open(FILE_PATH, "r") as file:
                loadedData = json.load(file)
            startBattle.battle.setPlayerStats(
                loadedData["Current HP"],
                loadedData["Current Mana"],
                loadedData["Current Minimum Damage"],
                loadedData["Current Maximum Damage"],
                loadedData["Current Bonus Damage"]
            )
            Movement.moving.movementLoad(
                roomsBeenTo=loadedData["Rooms the player has been to"],
                inventorySave=loadedData["Inventory"]
            )
            startBattle.battle.setPlayerStats(loadedData["Current HP"],loadedData["Current Mana"],loadedData["Current Minimum Damage"],loadedData["Current Maximum Damage"],loadedData["Current Bonus Damage"])
            MovementManager.roomMovement.SetCurrentRoom(
                newRoomX=loadedData["Current X"], 
                newRoomY=loadedData["Current Y"]
            )
            MovementManager.roomMovement.setUpRooms()
            MovementManager.roomMovement.gameplayLoop()
        if choice == "N":
            print("Deleting old file.")
            FILE_PATH.unlink()
            print("File deleted successfully.")
            startBattle.battle.setPlayerStats(15,15,1,5,2)
            MovementManager.roomMovement.SetCurrentRoom(5, 6)
            MovementManager.roomMovement.setUpRooms()
            MovementManager.roomMovement.gameplayLoop()
    else:
        print("Since you haven't played before (Or you have no save data), lets start a new game!")
        startBattle.battle.setPlayerStats(
            15, #Health level
            15, #Mana Level
            1,  #Min Damage
            5,  #Max Damage
            2   #Bonus Damage
            )
        MovementManager.roomMovement.SetCurrentRoom(5, 6)
        MovementManager.roomMovement.setUpRooms()
        MovementManager.roomMovement.gameplayLoop()