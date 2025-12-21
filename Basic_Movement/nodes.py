import pygame 
from vector import Vector2
from constants import *
import numpy as np
class Node(object):
    def __init__(self,x,y):
        self.position=Vector2(x,y)
        self.neighbors={UP:None,DOWN:None,LEFT:None,RIGHT:None,PORTAL:None}
    def render(self,screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_str=self.position.asTuple()
                line_end=self.neighbors[n].position.asTuple()
                pygame.draw.line(screen,WHITE,line_str,line_end,4)
                pygame.draw.circle(screen,RED,self.position.asInt(),12)

class NodeGroup(object):
    def __init__(self,level):
        # self.nodeList = []
        self.level=level
        self.nodeLUT={}
        self.nodeSymbols = ['+']
        self.pathSymbols = ['.']
        data = self.readMazeFile(level)
        self.createNodeTable(data)
        self.connectHorizontally(data)
        self.connectVertically(data)
    def readMazeFile(self,testFile):
        with open(testFile, 'r') as f:
            lines = [line.strip().split() for line in f.readlines()]
        return np.array(lines, dtype=str)
    
    def createNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    x, y = self.constructKey(col+xoffset, row+yoffset)
                    self.nodeLUT[(x, y)] = Node(x, y)

    def constructKey(self, x, y):
        return x * TILEWIDTH, y * TILEHEIGHT

    def connectHorizontally(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            key = None
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodeLUT[key].neighbors[RIGHT] = self.nodeLUT[otherkey]
                        self.nodeLUT[otherkey].neighbors[LEFT] = self.nodeLUT[key]
                        key = otherkey
                elif data[row][col] not in self.pathSymbols:
                    key = None
    def connectVertically(self, data, xoffset=0, yoffset=0):
        dataT = data.transpose()
        for col in list(range(dataT.shape[0])):
            key = None
            for row in list(range(dataT.shape[1])):
                if dataT[col][row] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodeLUT[key].neighbors[DOWN] = self.nodeLUT[otherkey]
                        self.nodeLUT[otherkey].neighbors[UP] = self.nodeLUT[key]
                        key = otherkey
                elif dataT[col][row] not in self.pathSymbols:
                    key = None
    def getNodeFromPixels(self, xpixel, ypixel):
        if (xpixel, ypixel) in self.nodeLUT.keys():
            return self.nodeLUT[(xpixel, ypixel)]
        return None

    def getNodeFromTiles(self, col, row):
        x, y = self.constructKey(col, row)
        if (x, y) in self.nodeLUT.keys():
            return self.nodeLUT[(x, y)]
        return None
    
    def getStartTempNode(self):
        nodes=list(self.nodeLUT.values())
        return nodes[0]

    def render(self, screen):
        for node in self.nodeLUT.values():
            node.render(screen)
    
    def setPortalPair(self, pair1, pair2):
        # * unpack the key mean if pair is (2,3) is use give without unpacking it will be one agument but with star is is 2 
        key1 = self.constructKey(*pair1)
        key2 = self.constructKey(*pair2)
        if key1 in self.nodeLUT.keys() and key2 in self.nodeLUT.keys():
            self.nodeLUT[key1].neighbors[PORTAL] = self.nodeLUT[key2]
            self.nodeLUT[key2].neighbors[PORTAL] = self.nodeLUT[key1]

