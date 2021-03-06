# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:47:06 2017

@author: apron
"""

import os

DISPTYPE = 'pygame' # The DISPTYPE can be either ‘pygame’ or ‘psychopy’
DISPSIZE=(1680, 1050)
SCREENNR = 1
TRACKERTYPE = 'smi' # The TRACKERTYPE should be 'smi' (for recording) or 'dummy'
DUMMYMODE = True # The DUMMYMODE should be True if no tracker is attached

FGC = (255, 255, 255) # Foreground colour set to white
BGC = (0, 0, 0) # Background colour set to black

FIXTIME = 2000 # Fixation mark time (milliseconds) 2000
#TXTTIME = 10000 # Image time (milliseconds) 10000

DIR = os.path.dirname(os.path.abspath(__file__)) # Path to the current folder
TXTDIR = os.path.join(DIR, 'text') # Path to the folder with text
TXTNAMES = os.listdir(TXTDIR) # List of all names
TXTNAMES.sort()

IP_IVIEWX = '192.168.2.43'
IP_STIM = '192.168.2.173'

SIZE = (1680,1050) # monitor screen resolution (2560, 1440)
WIDTH = 47.5 # (25.41 deg) monitor screen width, 59.5 cm 
DISTANCE = 50 # distance between subject and screen, cm

BACKCOL=(-1,-1,-1) # background color
FIXCOL=(1,1,1) # fixation mark color

CENTER = (0,0) # fixation mark coordinates, deg
PHOTOSENSOR_POS = (25, 14.4) # photosensor stimulus coordinates, deg

STIM_GROUP_NUMBER = 3 # number of groups in which target shall flash (2 for row-column speller)
STIM_NAMES = [item for item in u'abcdefghijklmnopqrstuvwxyz_1234567890!?.,;:"()+=-~[]\/'] # available stimuli names, unicode
STIM_SIZE = None
STIM_POS = None

# for x in [3.5, 7, 10]:
#     y = 10*(0.046*x - 0.031) # x - distance from the center
#     print y 
LS1 = [1.5]*9  # letter size, deg
LS2 = [3.5]*9  # letter size, deg
LS3 = [5.5]*9  # letter size, deg
BLOCK1=['D', 'K', 'O', 'Y', 'N', 'L', '*', 'H', 'P']
BLOCK2=['E', 'F', 'X', 'A', 'M', 'J', 'I', 'W', 'U']
BLOCK3=['S', 'B', 'Z', 'T', 'R', 'V', 'C', 'Q', 'G']
C1=[(0,-3.500), (-2.250,-2.681), (-3.447,-0.608), (-3.031,1.750), (-1.197,3.289),
    (1.197,3.289), (3.031,1.750), (3.447,-0.608), (2.250,-2.681)]  # coordinates of inner circle, deg
C2=[(0,7.000), (4.500,5.362), (6.894,1.216), (6.062,-3.500), (2.394,-6.578),
    (-2.394,-6.578), (-6.062,-3.500), (-6.894,1.216), (-4.500,5.362)]  # coordinates of middle circle, deg
C3=[(0,-12.000), (-7.713,-9.193), (-11.818,-2.084), (-10.392,6.000), (-4.104,11.276),
    (4.104,11.276), (10.392,6.000), (11.818,-2.084), (7.713,-9.193)]  # coordinates of outer circle, deg
