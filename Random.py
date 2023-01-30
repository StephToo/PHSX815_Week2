#! /usr/bin/env python

import math
import numpy as np

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            return 1
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0

    # function returns a random double (0 to infty) according to an exponential distribution
    def Exponential(self, beta=1.):
      # make sure beta is consistent with an exponential
      if beta <= 0.:
        beta = 1.

      R = self.rand();

      while R <= 0.:
        R = self.rand()

      X = -math.log(R)/beta

      return X
    
    
    
    
    #function returns a Multinoulli/Multinomial Distribution
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22, 'figure.autolayout': True, 'figure.figsize': (15,5)})
# set seed for reproductibility
np.random.seed(5890) 


n = 12                      # number of trials in one cycle
pvals = [0.4, 0.35, 0.25]   # probabilities on a single trial
 

sizes =[] # number of cycles
p = []    # a list to hold ratios (converge to prob) that player 1 wins 7 times, player 2 wins 2 times and 3 ties

for size in np.logspace(2,4):
    # generate discrete random variables according the multinomial distribution
    outcomes = np.random.multinomial(n, pvals, size=int(size))
    
    # ratio of the expected outcome over all the outcomes
    prob = sum((outcomes[:,0]==7)&(outcomes[:,1]==2)&(outcomes[:,2]==3))/len(outcomes)
    
    p.append(prob)
    sizes.append(int(size))

# Plotting
fig1 = plt.figure()
plt.plot(sizes,p,'o-')
plt.plot(sizes,[0.0248]*len(sizes),'--r')
plt.grid()
plt.xlim(xmin=0)
plt.xlabel('Number of Drawings')
plt.ylabel('p(X=K)')
plt.title('Theoretical p(X=K) = 0.0248')

plt.show()

fig1.savefig('multinomial.png')


