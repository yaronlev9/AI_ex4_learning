# analysis.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Change these default values to obtain the specified policies through
# value iteration.

def question2():
  answerDiscount = 0.9
  answerNoise = 0.005
  return answerDiscount, answerNoise

def question3a():
  answerDiscount = 0.12
  answerNoise = 0.00001
  answerLivingReward = 0.75
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3b():
  answerDiscount = 0.05
  answerNoise = 0.0005
  answerLivingReward = 0.9
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3c():
  answerDiscount = 0.2
  answerNoise = 0.00001
  answerLivingReward = 0.75
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3d():
  answerDiscount = 0.9
  answerNoise = 0.1
  answerLivingReward = 0.9
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3e():
  answerDiscount = 1
  answerNoise = 0.01
  answerLivingReward = 1
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question6():
  answerEpsilon = None
  answerLearningRate = None
  # return answerEpsilon, answerLearningRate
  return 'NOT POSSIBLE'
  # If not possible, return 'NOT POSSIBLE'
  
if __name__ == '__main__':
  print('Answers to analysis questions:')
  import analysis
  for q in [q for q in dir(analysis) if q.startswith('question')]:
    response = getattr(analysis, q)()
    print('Question %s:\t%s' % (q, str(response)))
