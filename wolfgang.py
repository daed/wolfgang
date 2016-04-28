import switch
import cmds

play = False

while True:
    if switch.button_state():
        if play is False:
            play = True
            # start playing
            cmds.start_player()
        else:
            play = False
            # stop playing
            cmds.stop_player()
