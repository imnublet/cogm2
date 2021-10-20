import ccm
import random
from ccm.lib.actr import *
log=ccm.log(html=True)


class Hanoi_env(ACTR):
    A = Buffer()
    B = Buffer()
    C = Buffer()
    hand = Buffer()
    # goal = Buffer()
    #goal = Buffer()


    def init():
        A.set('top:3 mid:2 bot:1')
        B.set('top:None mid:None bot:None')
        C.set('top:None mid:None bot:None')
        hand.set('disc:None')

    def hanoi_finished(C='top:3 mid:2 bot:1'):
        print random.randint(2,10)
        A.clear()
        B.clear()
        C.clear()
        hand.clear()
        print 'finished'

    def pick_from_A(hand='disc:None'):
        # print 'werkt deze functie'
        print 'value A_top: ', A.__getitem__('top')
        if A.__getitem__('top') != 'None':
            print 'wejow'
            hand.modify(disc=str(A.__getitem__('top')))
            A.modify(top='None')
            print 'value hand: ', hand.__getitem__('disc')
        elif A.__getitem__('mid') != 'None':
            hand.modify(disc=A.__getitem__('mid'))
            A.modify(mid='None')
        elif A.__getitem__('bot') != 'None':
            hand.modify(disc=A.__getitem__('bot'))
            A.modify(bot='None')


    def pick_from_B(hand='disc:None'):
        # print 'werkt deze functie'
        print 'value A_top: ', B.__getitem__('top')
        if B.__getitem__('top') != 'None':
            print 'wejow'
            hand.modify(disc=str(B.__getitem__('top')))
            B.modify(top='None')
            print 'value hand: ', hand.__getitem__('disc')
        elif B.__getitem__('mid') != 'None':
            hand.modify(disc=B.__getitem__('mid'))
            B.modify(mid='None')
        elif B.__getitem__('bot') != 'None':
            hand.modify(disc=B.__getitem__('bot'))
            B.modify(bot='None')

    def pick_from_C(hand='disc:None'):
        # print 'werkt deze functie'
        print 'value A_top: ', C.__getitem__('top')
        if C.__getitem__('top') != 'None':
            print 'wejow'
            hand.modify(disc=str(C.__getitem__('top')))
            C.modify(top='None')
            print 'value hand: ', hand.__getitem__('disc')
        elif C.__getitem__('mid') != 'None':
            hand.modify(disc=C.__getitem__('mid'))
            C.modify(mid='None')
        elif C.__getitem__('bot') != 'None':
            hand.modify(disc=C.__getitem__('bot'))
            C.modify(bot='None')



    def move_to_A(hand='disc:?d', A='top:?x mid:?y bot:?z'):
        print 'handje_A:', hand.__getitem__('disc')
        if hand.__getitem__('disc') != 'None':
            # print 'handje:', hand.__getitem__('disc')
            if str(z) == 'None':
                # hand.modify('disc:None')
                A.modify(bot=str(d))
                hand.modify(disc='None')
            elif str(y) == 'None' and str(z)!= 'None' and int(d) > int(z):
                A.modify(mid=str(d))
                hand.modify(disc='None')
            elif str(x) == 'None' and str(y)!= 'None' and int(d) > int(y):
                A.modify(top=str(d))
                hand.modify(disc='None')


    def move_to_B(hand='disc:?d', B='top:?x mid:?y bot:?z'):
        print 'handje_B:', hand.__getitem__('disc')
        if hand.__getitem__('disc') != 'None':
            # print 'handje:', hand.__getitem__('disc')
            if str(z) == 'None':
                # hand.modify('disc:None')
                B.modify(bot=str(d))
                hand.modify(disc='None')
            elif str(y) == 'None' and str(z)!= 'None' and int(d) > int(z):
                B.modify(mid=str(d))
                hand.modify(disc='None')
            elif str(x) == 'None' and str(y)!= 'None' and int(d) > int(y):
                B.modify(top=str(d))
                hand.modify(disc='None')

    def move_to_C(hand='disc:?d', C='top:?x mid:?y bot:?z'):
        print 'handje_C:', hand.__getitem__('disc')
        if hand.__getitem__('disc') != 'None':
            # print 'handje:', hand.__getitem__('disc')
            if str(z) == 'None':
                # hand.modify('disc:None')
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

# model.A.set('top:3 mid:2 bot:1')
# model.B.set('top:None mid:None bot:None')
# model.C.set('top:None mid:None bot:None')
# model.hand.set('disc:None')
ccm.log_everything(model)
model.A.set('top:3 mid:2 bot:1')
model.run()
