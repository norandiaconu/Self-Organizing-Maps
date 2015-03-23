#!/usr/bin/env python
# encoding: utf=8
"""
self_organizing.py

Create a self organizing map.

By Noran Diaconu, 2015-03-23.
"""
import random

usage = """
Usage: 
    python self_organizing.py

Example:
    python self_organizing.py
"""

def main():
	lam = 100
	m = 1
	RandomVector = [random.random() for i in range(lam)]
	W = (0, m)
	for s in range (1, lam):
		for i in range (1, m):
			Dt = RandomVector.random()
			self.weights[Dt.multi_index] += g[Dt.multi_index]*(x-self.weights[Dt.multi_index])
			RandomVector = W(RandomVector) + (Dt - W(RandomVector))
	map.title('Self Organizing Maps')
	map.ylim([0,9])
	map.xlim([0,9])
	for i, j in enumerate(mapped):
    	map.text(j[1], j[0], data_names[i], ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5, lw=0))
	map.savefig('map.png');

if  __name__ == '__main__':
    import sys
    try:
		print ""
    except:
        print usage
        sys.exit(-1)
    main()
