######################################
#       Caesar Salad Cracker         #
######################################
import collections
text = ''
code = 'shjrvbadvyyplkashavbyjpwolypzavvdlhrvuuleaflzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzffivsvmklhaoputfmhcvypalovsilpulukvwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdgbeoxhsulqwviruydxowdqgdodupghvljgedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']
static_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
list = collections.deque(alphabet)
c = 0
for i in range(0, 25):
    list.rotate(1)
    for x in clue1:
        f = clue1[c]
        n = static_alph.index(f)
        text += list[n]
        c += 1
    c = 0
    print(text[:10])
    print('\npass: ', i)
    text = ''
