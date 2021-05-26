from enum import Enum

class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

c = 'c'
b = 'b'
p = 'p'
t = 't'

rewards = {
    b: 100,
    p: -1000,
    c: -100,
    t: 500
}

environment = [
	[b, c, c, c, b, c, b, b, c, b],
	[b, p, b, b, b, b, b, p, b, p],
	[b, c, c, b, c, c, b, b, b, c],
	[b, b, b, b, b, b, c, c, b, c],
	[c, p, p, c, b, p, b, b, b, b],
	[b, b, b, c, b, b, c, c, c, b],
	[b, c, c, c, p, b, c, c, p, b],
	[b, b, b, p, c, b, p, b, b, b],
	[c, p, b, b, b, b, b, b, b, c],
	[p, c, b, c, c, b, b, c, b, p]
]

symbolToUnicode = {
	c: '🚗',
	b: ' ',
	p: '🕴',
	t: '👫',
	0: '↑',
	1: '→',
	2: '↓',
	3: '←'
}
