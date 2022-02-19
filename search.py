#!/usr/bin/env python3
'''DFS and BFS to solve sliding puzzle problem'''
'''comment out the 3d search to see 2d'''
'''the 3d take a long time to load to give it time'''
from depth_first_search import DepthSearch

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'

def main():
    '''the main function'''
    list_2d = [0, 3, 2, 1]
    search1 = DepthSearch(list_2d)
    search1.depth_search()

    list_3d = [1, 4, 3, 7, 0, 6, 5, 8, 2]
    #list_3d = [1, 2, 3, 4, 5, 6, 7, 0, 8] #this one is easier to test
    search2 = DepthSearch(list_3d)
    search2.depth_search()

if __name__ == '__main__':
    main()