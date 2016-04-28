from subprocess import Popen

def stop_player():
    Popen(["mpc", "stop"])

def start_player():
    Popen(["mpc", "play"])
