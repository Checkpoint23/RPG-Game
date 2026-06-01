import Movement
import time

class roomMovement:
    def SetCurrentRoom(newRoomX, newRoomY):
        global roomX
        global roomY
        roomX = newRoomX
        roomY = newRoomY
    def setUpRooms():
        Movement.moving.addRoom(
            1, #x
            1, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "Around you, you see a chest to the west of your position, about 2 kilometers away. The trees have leaves as green as the grass, and the sunshine beams down on you.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            2, #x
            1, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "As you look around, you see that you're only about a kilometer away from the chest.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            3, #x
            1, #y
            1, #world
            "B", #treasure (bluekey)
            False, #encounterEnemy?
            0, #chanceofEncounter
            "You arrive at the chest. Inside, sits the blue key.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            5, #x
            1, #y
            1, #world
            "none", #treasure
            False, #encounterEnemy?
            0, #chanceofEncounter
            "You arrive at the World Gate, showing you the path to a brand new area. After defeating the mimic, something stirs inside of you. A longing, for adventure. TO BE CONTINUED!!!", #description
            "none", #Gate?
            "none", #Boss
            "2", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            7, #x
            1, #y
            1, #world
            "G", #treasure green key
            False, #encounterEnemy?
            0, #chanceofEncounter
            "You arrive at the chest, inside, sits the Green key!", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            8, #x
            1, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "As you look around, you see a chest about a kilometer down the valley.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            1, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "To the west of you sits a lush green valley, filled with bushes, and even a few waterfalls..", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            1, #x
            2, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "To the north of you sits a narrow creek which seems to suddenly turn east about half a kilometer in.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            5, #x
            2, #y
            1, #world
            "none", #treasure
            False, #encounterEnemy?
            0, #chanceofEncounter
            "You encounter a chest beyond the gate. You open it. All of a sudden, a tongue jumps out at you! It was no chest, it was a mimic!", #description
            "RGBYN", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            2, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "Northward lies the entrance of a valley.", #description
            "none", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            1, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "As you enter the field, you notice you are about a kilometer away from the mountains. Northward lies a split between the two mountains. Southward, more plains. Eastward lies more plains as well.", #description
            "none", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            2, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "As you enter the field, you notice you are surrounded by fields on all sides, except for northwards, which has mountains.", #description
            "none", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            3, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            40, #chanceofEncounter
            "As you leave the mountain pass, you notice that the fields strech out in the directions in which the mountains aren't present.", #description
            "none", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            4, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            20, #chanceofEncounter
            "As you leave the area of the gates, you enter a pass between the two mountains. In front of you appears to be a large stretch of fields.", #description
            "none", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            5, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            40, #chanceofEncounter
            "You approach a gate. It has four locks on it. A red lock, a green lock, a blue lock, and a yellow lock.", #description
            "none", #Gate?
            "Mimic", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            6, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            20, #chanceofEncounter
            "To the east of you sits a large amount of fields.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            7, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "As you enter the fields, you notice the fields continue east and south and southeast. Mountains appear to have crafted a path throughout this reigon.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            8, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "You continue through the fields.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            3, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "You continue through the fields, arriving at the mountain edge. Northward appears to lead into a valley, while southward seems to continue into fields, eventually arriving at a tunnel into the mountains.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            1, #x
            4, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "Southward lies a water creek between two mountains. You feel like there is something important somewhere in an area southward. ", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            2, #x
            4, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            40, #chanceofEncounter
            "You continue moving through the fields. The sun is shining bright today.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            3, #x
            4, #y
            1, #world
            "none", #treasure
            False, #encounterEnemy?
            0, #chanceofEncounter
            "You arrive at a village. It seems someone is in distress.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "Ring" #quest
        )
        Movement.moving.addRoom(
            5, #x
            4, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "You continue through to the end of the valley. Up north, something is glinting, though its hard to make it out", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            7, #x
            4, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "You reach a corner of the mountains. Northwards is fields, and eastward is fields.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            8, #x
            4, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "Continuing through the fields, you feel like the sunshine sure feels nice today.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            4, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "Southward appears to have a tunnel. You feel something is down there, like another large portion of valleys in between mountains.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            1, #x
            5, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "Moving through the creek ", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            5, #x
            5, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "As you continue walking through the valley, you hear a rustling in the bushes.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            5, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            50, #chanceofEncounter
            "Continuing to walk through the tunnel, it's quite dark.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            1, #x
            6, #y
            1, #world
            "none", #treasure
            False, #encounterEnemy?
            50, #chanceofEncounter
            "Exiting the creek, there is a mountain blocking the way south and west. The only new direction is east. In the east, something is glittery.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            2, #x
            6, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "Moving east, the glittering thing gets closer. Southward lies a valley now.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            3, #x
            6, #y
            1, #world
            "Y", #treasure (yellowkey)
            False, #encounterEnemy?
            0, #chanceofEncounter
            "The glittering thing turned out to be the Yellow Key!", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            5, #x
            6, #y
            1, #world
            "none", #treasure
            False, #encounterEnemy?
            0, #chanceofEncounter
            "You wake up in a valley. The only way is north. You do not remember how you got here. You do not remember who you are. All you know, is that you have a sword in your hand, and you need to accoplish something of greatness.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            7, #x
            6, #y
            1, #world
            "R", #treasure (redkey)
            False, #encounterEnemy?
            0, #chanceofEncounter
            "As you arrive at the chest, inside appears a red key!", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            8, #x
            6, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "Arriving further west, the glittering thing in the distance unblurs and it appears to be a chest!", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            6, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "Arriving at the end of the tunnel, the only way to progress is west. Something is glittering west.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            2, #x
            7, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "The south has more fields, and then mountains.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            3, #x
            7, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "The fields are a bit colder at this side of the mountains. ", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            7, #x
            7, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "As you continue, a sudden chill goes down your spine.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            8, #x
            7, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "As you continue, you notice that the sun isn't shining that bright over here.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            1, #x
            8, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "The chest you saw over here gets closer. But as you get closer, you realize it was painted onto a wall! It was a trap!", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            2, #x
            8, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "Westward you see a treasure chest. Eastward, you see something. You aren't sure what it is, but you haven't seen something similar in a long time, it feels.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            3, #x
            8, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "Eastward, there is something glowing. You haven't seen something like this in a long time, you think.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            4, #x
            8, #y
            1, #world
            "H-5", #treasure
            False, #encounterEnemy?
            0, #chanceofEncounter
            "The glowing thing gets closer, closer. Then you touch it. You can't remember what happens next. You wake up. The glowing thing is gone now. You feel stronger. (Max Health has increased by 5!)", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            6, #x
            8, #y
            1, #world
            "G-50", #treasure
            True, #encounterEnemy?
            0, #chanceofEncounter
            "You arrive at the treasure chest. Inside, sits 50 gold pieces! That's worth a lot in the trading areas.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            7, #x
            8, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            60, #chanceofEncounter
            "Westward is a chest.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            8, #x
            8, #y
            1, #world
            "none", #treasure
            True, #encounterEnemy?
            100, #chanceofEncounter
            "Eastward, you see something in the corner of your eyes glint.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "none" #quest
        )
        Movement.moving.addRoom(
            9, #x
            8, #y
            1, #world
            "Ring", #treasure
            False, #encounterEnemy?
            0, #chanceofEncounter
            "Continuing through the fields, you find a ring hidden in the grass. It does not appear to have any magical properties.", #description
            "none", #Gate?
            "none", #Boss
            "none", #worldGate
            "questFindRing" #quest
        )
    def gameplayLoop():
        global roomX
        global roomY
        game = True
        while game == True:
            time.sleep(0.05)
            Movement.moving.roomFunctions(currentRoomX=roomX, currentRoomY=roomY)
            Movement.moving.fromRoom(currentRoomX=roomX, currentRoomY=roomY)