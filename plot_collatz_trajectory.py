import random
import matplotlib.pyplot as plt
from logging import getLogger, DEBUG, StreamHandler
logger = getLogger()
logger.setLevel(DEBUG)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)


MAX_INT = 1000000000
TRIAL = 20

for i in range(TRIAL):
    x = []
    longest = []
    n = random.randint(2, MAX_INT)
    x.append(n)
    logger.debug(f"{i}th trial: {n}")
    while n>1:
        if n%2==0:
            n = n//2
        else:
            n = n*3+1
        logger.debug(f"{i}th trial: {n}")
        x.append(n)
        plt.plot(range(len(x)),x)
    # if len(longest)<len(x):
    #     longest = x
    
# plt.plot(range(len(x)),x)
plt.show()
    
        