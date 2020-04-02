# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:54:11 2020

@author: jayja
"""
import random as rd

def inps():
    inputs = input('Enter an initial \nD: Driver\nI: Iron\nP: Putter\n:')
    inputs = inputs.lower()
    if inputs != 'd' and inputs != 'i' and inputs != 'p':
        print('\nIncorrect initial entered')
        inps()
    return inputs
        
def hole_distance():
    hole = 230
    #hole = rd.randint(0, 1000)
    print('Hole is {}m away from you'.format(hole))
    return hole
    
def clubs(inputs, hole):
    flag = 0
    dynamic_hole = hole
    dist_travelled = 0
    while (dynamic_hole) != 0:
        if inputs == 'd':
            dist_travelled = rd.randint(80, 120)
        elif inputs == 'i':
            dist_travelled = rd.randint(24, 36)
        elif inputs == 'p':
            if dynamic_hole < 10:
                dist_travelled = rd.randint(int(0.8*dynamic_hole), int(1.2*dynamic_hole))
                if dist_travelled == 0:
                    dist_travelled = 1
            else:
                dist_travelled = 10
        dynamic_hole = abs(dynamic_hole - dist_travelled)
        flag += 1
        print('Your shot went {}m, you are {}m away from the hole, after {} shot'.format(dist_travelled, dynamic_hole, flag))
        if dynamic_hole != 0:
            inputs = inps()
    return flag

if __name__ == '__main__':
    par = 5
    hole_dist = hole_distance()
    input_club = inps()
    score = clubs(input_club, hole_dist)
    if score < 5:
        print('\nAfter {} hits, the ball is in the hole! Congratulations, you exceeded expectations'.format(score))
    elif score == 5:
        print("\nAfter 5 hits, the ball is in the hole! And that's par.")
    elif score > 5:
        print('\nAfter {} hits, the ball is in the hole! Disappointing. You are {} over par.'.format(score, score-par))
        
        
'''
Hole is 230m away from you

Enter an initial 
D: Driver
I: Iron
P: Putter
:d
Your shot went 119m, you are 111m away from the hole, after 1 shot

Enter an initial 
D: Driver
I: Iron
P: Putter
:d
Your shot went 111m, you are 0m away from the hole, after 2 shot

After {} hits, the ball is in the hole! Congratulations, you exceeded expectations
'''