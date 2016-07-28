import switch
import cmds
from time import sleep

play = False

while True:
    sleep(0.02)
    if switch.button_state():
        if play is False:
            play = True
            # start playing
            cmds.start_player()
            sleep(1)
        else:
            play = False
            # stop playing
            cmds.stop_player()
            sleep(1)
