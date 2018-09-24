from liblo import *
from synthesizer import Player, Synthesizer, Waveform 
import sys
import time
import random as ra


class MuseServer(ServerThread): 

	#opens in port 5000
	def __init__(self):
		ServerThread.__init__(self, 5000)

	@make_method('/muse/eeg', 'ffff')
	def eeg_callback(self, path, args):
		lE, lF, rF, rE = args
		print "%s %f %f %f %f" % (path,lE, lF, rF, rE)
		player = Player() 
		player.open_stream() 
		synthesizer = Synthesizer(osc1_waveform = Waveform.sine, osc1_volume = 1.0, use_osc2 = False)
		number = ra.uniform(0.2, 1.0)
		player.play_wave(synthesizer.generate_constant_wave((lF - 1200)*((600-200)/(1200-750)) + 200), number)
		player.play_wave(synthesizer.generate_constant_wave((rF - 1200)*((600-200)/(1200-750)) + 200), number)

try:
    server = MuseServer()
except ServerError, err:
    print str(fatal_error)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
