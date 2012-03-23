#!/bin/env python

import sys
import pygame
import re
import time

class LogBeat():

    samplePaths = ['samples/bassdrum.wav', 'samples/hihat.wav', 'samples/snaredrum.wav'] 
    logRegex = ['.*Rest query:.*', '.*retrieved.*', '.*Converter.*']
    delays = {0 : 0.06, 1 : 0.06, 2 : 0.007}

    def __init__(self):
        pygame.init()
        self.sound = []
        for path in self.samplePaths:
            self.sound.append(pygame.mixer.Sound(path))

    def justBeatIt(self, thefile):

        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.001)    # Sleep briefly
                continue
            for i in range(len(self.logRegex)):
                if re.findall(self.logRegex[i], line):
                    print '### ' + str(i) + ' ###'
                    print line
                    self.sound[i].play()
                    time.sleep(self.delays.get(i))
        
        
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print 'Usage:\n' + sys.argv[0] + ' log_file'
    
    rb = LogBeat()
    rb.justBeatIt(open(sys.argv[1], 'r'))
    
    


