"""
Simple eyetracking experiment to test eyetracker.

"""

from eyetracker import Eyetracker
from psychopy.monitors import Monitor
from psychopy.visual import Window
from psychopy.visual.circle import Circle
from psychopy.visual import TextStim
import time
from CONSTANTS import *

# Initiate and calibrate the eyetracker
tracker = Eyetracker()
tracker.connect()
tracker.calibrate()

# Prepare psychopy stuff
monitor = Monitor('Dell') # Monitor('Phillips')
monitor.setSizePix(SIZE)
monitor.setWidth(WIDTH)
monitor.setDistance(DISTANCE)
monitor.saveMon()
disp=Window(size=SIZE, monitor=monitor, units='deg', color=BACKCOL, screen=2, fullscr=True)

# Draw image

fixmark=Circle(disp, radius=0.05 ,edges=32, pos=CENTER, lineColor=FIXCOL)
fixmark.draw()

for letter in [zip(BLOCK1, C1, LS1), zip(BLOCK2, C2, LS2), zip(BLOCK3, C3, LS3)]:
    for stimul in letter:
        stim = TextStim(disp, text=stimul[0], pos=stimul[1], units='deg', height=stimul[2], opacity=0.4)
        stim.draw()

# Start recording
tracker.start_record()
tracker.send_message('TRIALSTART')

# Show image
tracker.send_message('image_onset')
disp.flip()
time.sleep(20)
disp.flip()
tracker.send_message('image_offset')

# Stop recording and save data
tracker.send_message('TRIALSTOP')
tracker.stop_record()
tracker.save_data('Timofey_test_eyetracker')
tracker.disconnect()

disp.close()