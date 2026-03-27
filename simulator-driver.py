from mabwiser.mab import MAB, LearningPolicy

## Whatever you want to define
arms = ["Arm1", "Arm2"]
decisions = []
rewards = []
# TODO: Please adjust the decisions and rewards accordingly.
# TODO: ...or you may as well integrate into the driver

epg = MAB(arms, LearningPolicy.EpsilonGreedy(epsilon=0.5)) # Example Epsilon Greedy
smx = MAB(arms, LearningPolicy.Softmax(tau=1)) # Example Softmax
linUCB = MAB(arms, LearningPolicy.LinUCB(alpha=1.25)) # Linear UCB, for contextual.
linTS = MAB(arms, LearningPolicy.LinTS(alpha=1.25)) # Linear Thompson Sampling, for contextual.

# TODO: According to your needs, do whatever adjustment you like.