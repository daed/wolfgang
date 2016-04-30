# wolfgang
A raspberry pi music player

Install (from hackaday.io project at https://hackaday.io/project/11186-wolfgang)

Got drunk the other night and figured, why not, now is the time for this. It turned out to be a reasonably straightforward project really. First step was going to be babbling about the microswitch, but actually, first step is my long list of assumptions!

Assumptions:

You have basic linux knowledge.
You are running raspbian.
You have already set up whatever internet connection you are happy with and it gets an ip on boot.
First... err, second step was the microswitch. I didn't want to have to look at a screen or fight with remembering commands when I was half asleep and trying to figure out how to turn this on/off at any give point in the future, so I figured a momentary pushbutton to control playback was ideal. In the interest of keeping things simple, I rummaged around for a piece of pcb with a mounting hole and got to work.

After drilling a corresponding hole in the case for the mounting hole, I set out putting several holes in the case for the wires to feed through. I would widen these out to the size of the entire pcb with a knife later to allow for future use. As a side note, if you're working with things on a drill press, clamp them down. If they get ripped out of your hands, they're going to sting, even if it's just a lightweight raspberry pi case. About this point, I got another beer to deal with the stinging in my hand. Anyway, so there's a good mounting hole for the screw, and you have a window to the underside of the pcb. At this point I soldered the components on. ...there's no anecdote here. You start out careful and well ventilated when using a soldering iron and you don't stop. I soldered the microswitch on, wires to its contacts, and also a resistor and led that are not connected to anything as of now that I might use in the future.

After screwing it together, I attached the wires to the pins I wanted to use and screwed the case down. The astute reader will note from the code in switch.py that I used logical pin 16 for one pin in pullup mode. I used the ground pin right next to it for the other one. You can see this in the picture, kinda. The pin you use isn't that important as long as you change switch.py to reflect which pin it's supposed to be using. Further enhancements to this (if there are any) will probably result in the pin assignment being moved into the main python module being passed into the switch module as an argument.

So now we have a hardware button, let us consider setup. To handle the heavy lifting, I used the fantastic commandline based mpd/mpc to actually play music, and just used the python subprocess module to handle sending commands to it. You'll probably want to run "sudo apt-get install mpc mpd" while you're here (and also maybe install python3 while you're at it, because I don't remember if it's standard on Raspbian).

Once that's done, in your home directory, you'll want to "git clone https://github.com/daed/wolfgang.git" to get the source code. You'll also want to find some music. Mpd can play music from *.mpd files, but it can't directly recognize the mpd files itself. I used the fantastic WQXR streaming channel for my music, which has an mpd file available at (http://www.wqxr.org/stream/wqxr/mp3.pls). So I ran "wget http://www.wqxr.org/stream/wqxr/mp3.pls" to get the pls. Inside, you'll note the URL assigned to "File1". Copy that url, and run the command "mpc add <URL>" or in my case "mpc add http://stream.wqxr.org/wqxr". Memory of this playlist should survive reboots, so we're about good here now. Connect some speakers and run "mpc play" to confirm it is working. Running "mpc stop" will stop the music again. If it works, all is well so far, if not, maybe check the url you're using, and try mine. If it's still not working, try to get a local file, mp3 or something, to work.

So now we have a button, code, and a playlist. Lets try actually running the code and see if it works! Go into the wolfgang directory and run "python3 wolfgang.py" and press your button a few times. There's a one second delay on the button, so give it some time between presses. Make sure that it responsively turns on and off your music. Good? Good. Hit ctrl+c. We're going to set this up to run in the background on boot from now on, so a running instance isn't good for much more than testing.



We're almost done at this point. You need to open /etc/rc.local, probably with sudo, and add the line "nohup python3 /home/pi/wolfgang/wolfgang.py &> /dev/null &" to the file just above where it says "exit 0". This will make sure that it runs at boot, and makes sure that it discards any output text (which mpc will create every time the button is pressed).

After that, reboot, and then hit the button. Does it play? Hit it again? Does it stop? Winning!
