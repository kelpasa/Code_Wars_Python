'''
In the previous Kata we discussed the OR case.

We will now discuss the AND case, where rather than calculating the probablility for either of two (or more) possible results, we will calculate the probability of receiving all of the viewed outcomes.

For example, if we want to know the probability of receiving head OR tails in two tosses of a coin, as in the last Kata we add the two probabilities together. However if we want to know the probability of receiving head AND tails, in that order, we have to work differently.

The probability of an AND event is calculated by the following rule:

P(A ∩ B) = P(A | B) * P(B)

or

P(B ∩ A) = P(B | A) * P(A)

That is, the probability of A and B both occuring is equal to the probability of A given B occuring times the probability of B occuring or vice versa. If the events are mutually exclusive like in the case of tossing a coin, the probability of A occuring if B has occured is equal to the probability of A occuring by itself. In this case, the probability can be written as the below:

P(A ∩ B) = P(A) * P(B)

or

P(B ∩ A) = P(B) * P(A)

Applying to the heads and tails case:

P(H ∩ T) = P(0.5) * P(0.5)

or

P(H ∩ T) = P(0.5) * P(0.5)
'''



from collections import defaultdict

def ball_probability(balls):
    d = defaultdict(int)
    bag, given_balls, putback = balls
    ball1, ball2 = given_balls

    for ball in bag:
        d[ball] += 1

    p_ball1 = float(d[ball1] / len(bag))
    if not putback:
        d[ball1] -= 1
    p_ball2 = float(d[ball2] / (len(bag) - 0 if putback else len(bag) - 1))
    p_ball1_and_ball2 = p_ball1 * p_ball2
    return round(p_ball1_and_ball2, 3)
