# parameters
#   remaining: how many numbers you have
#   amount: 

import pprint
 
def gen_comb(remaining, amount):
    if remaining == 1:
        yield [amount]
    else:
        for i in range(amount+1):
            for tail in gen_comb(remaining-1,amount-i):
                yield [i] + tail
               
pprint.pprint(list(gen_comb(4,5)))
