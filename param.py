#!/usr/bin/env python
# encoding: utf-8
"""
param.py: global parameters for the simulator

CS266 Ant Sim
"""

import sys, math

# global parameters
class G(object):

	# global datastructures (don't touch these)
	NOANT, NORMAL, SHAKING, DEAD = range(4)
	STRAIGHT_DOWN, RANDOM_WALK = range(2)
	HORIZONTAL_SUPPORT, RANDOM_SUPPORT = range(2)
	state = None
	weight = None
	running = True
	numJoints = 0
	forceData = None
	joints = None
 	EPS = 0.000001	
	# parameters for frontend
	numBlocksX = 20
	numBlocksY = 10
	buttonPanelHeight = 100
	screenHeight = 600
	screenWidth = 500
	lineWidth = 1.0
	jointWidth = 5.0
	sleep = 0.25
	blockWidth = screenWidth/numBlocksX
	blockHeight = (screenHeight-buttonPanelHeight)/numBlocksY
	#blockSize = int(min(screenWidth/numBlocksX,(screenHeight-buttonPanelHeight)/numBlocksY))
	lineColor = (0, 0, 0)
	emptyColor	= (255, 255, 255)
	fillColor	= (0, 0, 200)
	shakeColor	= (100, 0, 200)
	jointColor = (255, 255, 0)
	shakeJointColor = (255, 0, 0)
	deadJointColor = (100, 100, 100)
	deadColor = (0, 0, 0)
	searchColor = (0, 200, 0)

	# parameters for simulator
	antWeight = 1.0
	shakeThreshold = 3*antWeight
	killThreshold = 5*antWeight
	baseMoveAlgo = STRAIGHT_DOWN
	supportAlgo = RANDOM_SUPPORT
	
	# parameters for output
	outfile = sys.stdout
	verbose = None
