
import random

from qlearnexamples import *

# The Q-Learning Algorithm

# EXERCISE ASSIGNMENT:
# Implement the Q-learning algorithm for MDPs.
#   The Q-values are represented as a Python dictionary Q[s,a],
# which is a mapping from the state indices s=0..stateMax to
# and actions a to the Q-values.
#
# Choice of actions can be completely random, or, if you are interested,
# you could implement some scheme that prefers better actions, e.g.
# based on Multi-arm Bandit problems (find more about these in the literature:
# this is an optional addition to the programming assignment.)

# OPTIONAL FUNCTIONS:
# You can implement and use the auxiliary functions bestActionFor and execute
# if you want, as auxiliary functions for Qlearning and makePolicy and makeValues.

# bestActionFor chooses the best action for 'state', given Q values
def argmax(lst):
  return max(enumerate(lst), key=lambda x: x[1])[0]


def bestActionFor(mdp,state,Q):
  actions = mdp.applicableActions(state)
  if not actions:
    return random.choice(mdp.ACTIONS)
  values = [Q[(state,a)] for a in actions]
  return actions[argmax(values)]
# valueOfBestAction gives the value of best action for 'state'

def valueOfBestAction(mdp,state,Q):
  actions = mdp.applicableActions(state)
  if not actions:
    return 0
  values = [Q[(state,a)] for a in actions]
  return max(values)
  

def choose_greedy_action(mdp,s,Q,prob=0.8):
  """choose best action with 0.8 prob, and random action with 0.2 prob"""
  actions = mdp.applicableActions(s)
  a = bestActionFor(mdp,s,Q)
  return random.choices(actions+[a], weights=[(1-prob)/(len(actions)) for _ in range(len(actions))]+[prob])[0]

# 'execute' randomly chooses a successor state for state s w.r.t. action a.
# The probability with which is given successor is chosen must respect
# to the probability given by mdp.successors(s,a).
# It returns a tuple (s2,r), where s2 is the successor state and r is
# the reward that was obtained.

def execute(mdp,s,a):
  succ = mdp.successors(s,a)
  s_ = random.choices(succ, weights=[s_[1] for s_ in succ])[0]
  return (s_[0],s_[2])

# OBLIGATORY FUNCTION:
# Qlearning returns the Q-value function after performing the given
#   number of iterations i.e. Q-value updates.

def Qlearning(mdp,gamma,lambd,iterations):
  # The Q-values are a real-valued dictionary Q[s,a] where s is a state and a is an action.
  state =  0 # Always start from state 0
  Q = dict()
  for s in range(mdp.stateMax+1):
    for a in mdp.ACTIONS:
      Q[(s,a)] = 1
  for i in range(iterations):
    actions = mdp.applicableActions(state)
    if not actions: #stuck in 99 waali state
      state = 0
      continue
    # a = random.choice(actions)
    a = choose_greedy_action(mdp,state,Q, prob=1.0)
    (s_,r) = execute(mdp,state,a)
    
    # update q value for s,a,s_
    Q[(state,a)] = (1-lambd)*Q[(state,a)] + lambd*( r + gamma*max([Q[(s_,a)] for a in mdp.applicableActions(s_)]) )
    state = s_

  return Q

# OBLIGATORY FUNCTION:
# makePolicy constructs a policy, i.e. a mapping from state to actions,
#   given a Q-value function as produced by Qlearning.

def makePolicy(mdp,Q):
  # A policy is an action-valued dictionary P[s] where s is a state
  P = dict()
  for s in range(mdp.stateMax+1):
    P[s] = bestActionFor(mdp,s,Q)
  return P


# OBLIGATORY FUNCTION:
# makeValues constructs the value function, i.e. a mapping from states to values,
#   given a Q-value function as produced by Qlearning.

def makeValues(mdp,Q):
  # A value function is a real-valued dictionary V[s] where s is a state
  V = dict()
  for s in range(mdp.stateMax+1):
    V[s] = max([Q[(s,a)] for a in mdp.ACTIONS])
  return V
