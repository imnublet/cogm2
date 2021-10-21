import ccm
from ccm.lib.actr import *


log=ccm.log()

class Hanoi_env(ACTR):
    A = Buffer()
    B = Buffer()
    C = Buffer()
    hand = Buffer()
    steps = Buffer()

    # Initialize the towers, hand and amount of steps
    def init():
        A.set('top:3 mid:2 bot:1')
        B.set('top:None mid:None bot:None')
        C.set('top:None mid:None bot:None')
        hand.set('disc:None')
        steps.set('step:0')

    # If all discs are placed in tower C the program ends
    def hanoi_finished(C='top:3 mid:2 bot:1'):
        A.clear()
        B.clear()
        C.clear()
        hand.clear()
        total_steps = steps.__getitem__('step')
        f = open("results.txt", "a")
        f.write(total_steps+'\n')
        f.close()
        print 'finished'
        print 'this took', total_steps, 'steps to complete'

    # Pickup a disc from tower A if it contains a disc and place it in hand
    def pick_from_A(hand='disc:None'):
        step_int = int(steps.__getitem__('step'))
        steps.modify(step=str(step_int+1))
        if A.__getitem__('top') != 'None':
            hand.modify(disc=str(A.__getitem__('top')))
            A.modify(top='None')
        elif A.__getitem__('mid') != 'None':
            hand.modify(disc=A.__getitem__('mid'))
            A.modify(mid='None')
        elif A.__getitem__('bot') != 'None':
            hand.modify(disc=A.__getitem__('bot'))
            A.modify(bot='None')

    # Pickup a disc from tower B if it contains a disc and place it in hand
    def pick_from_B(hand='disc:None'):
        step_int = int(steps.__getitem__('step'))
        steps.modify(step=str(step_int+1))
        if B.__getitem__('top') != 'None':
            hand.modify(disc=str(B.__getitem__('top')))
            B.modify(top='None')
        elif B.__getitem__('mid') != 'None':
            hand.modify(disc=B.__getitem__('mid'))
            B.modify(mid='None')
        elif B.__getitem__('bot') != 'None':
            hand.modify(disc=B.__getitem__('bot'))
            B.modify(bot='None')

    # Pickup a disc from tower B if it contains a disc and place it in hand
    def pick_from_C(hand='disc:None'):
        step_int = int(steps.__getitem__('step'))
        steps.modify(step=str(step_int+1))
        if C.__getitem__('top') != 'None':
            hand.modify(disc=str(C.__getitem__('top')))
            C.modify(top='None')
        elif C.__getitem__('mid') != 'None':
            hand.modify(disc=C.__getitem__('mid'))
            C.modify(mid='None')
        elif C.__getitem__('bot') != 'None':
            hand.modify(disc=C.__getitem__('bot'))
            C.modify(bot='None')


    # Move a disc from hand to tower A if possible
    def move_to_A(hand='disc:?d', A='top:?x mid:?y bot:?z'):
        step_int = int(steps.__getitem__('step'))
        steps.modify(step=str(step_int+1))
        if hand.__getitem__('disc') != 'None':
            if str(z) == 'None':
                A.modify(bot=str(d))
                hand.modify(disc='None')
            elif str(y) == 'None' and str(z)!= 'None' and int(d) > int(z):
                A.modify(mid=str(d))
                hand.modify(disc='None')
            elif str(x) == 'None' and str(y)!= 'None' and int(d) > int(y):
                A.modify(top=str(d))
                hand.modify(disc='None')

    # Move a disc from hand to tower B if possible
    def move_to_B(hand='disc:?d', B='top:?x mid:?y bot:?z'):
        step_int = int(steps.__getitem__('step'))
        steps.modify(step=str(step_int+1))
        if hand.__getitem__('disc') != 'None':
            if str(z) == 'None':
                B.modify(bot=str(d))
                hand.modify(disc='None')
            elif str(y) == 'None' and str(z)!= 'None' and int(d) > int(z):
                B.modify(mid=str(d))
                hand.modify(disc='None')
            elif str(x) == 'None' and str(y)!= 'None' and int(d) > int(y):
                B.modify(top=str(d))
                hand.modify(disc='None')

    # Move a disc from hand to tower C if possible
    def move_to_C(hand='disc:?d', C='top:?x mid:?y bot:?z'):
        step_int = int(steps.__getitem__('step'))
        steps.modify(step=str(step_int+1))
        if hand.__getitem__('disc') != 'None':
            if str(z) == 'None':
                C.modify(bot=str(d))
                hand.modify(disc='None')
            elif str(y) == 'None' and str(z)!= 'None' and int(d) > int(z):
                C.modify(mid=str(d))
                hand.modify(disc='None')
            elif str(x) == 'None' and str(y)!= 'None' and int(d) > int(y):
                C.modify(top=str(d))
                hand.modify(disc='None')


#Run model
model=Hanoi_env()

ccm.log_everything(model)
model.A.set('top:3 mid:2 bot:1')
model.run()
