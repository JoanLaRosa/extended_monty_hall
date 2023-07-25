# Extended Monty Hall Problem
## Introduction

*I was sitting at a dinner table with some friends, and they asked me the following question: "Imagine you are give the chance to win a car by playing a game. You are given the choice of three doors. Behind one door is a car; behind the others, goats. You pick a door, say No. $1$, and the host, who knows what's behind the doors, opens another door, say No. $3$, which has a goat. He then says to you, 'Do you want to pick door No. $2$?' Is it to your advantage to switch your choice?" I realized that this was a tricky question to answer and that by keeping your choice you would have the probability of $1/3$ of winning the car, but I was not sure about the probability of winning if you switch your choice.*  

*It then became very aparent the the answer was $2/3$ (as in $1-2/3$) This is because the host knows where the car is and he will always open a door with a goat. So, if you choose a door with a goat, the host will open the other door with a goat and you will win the car if you switch your choice. If you choose the door with the car, the host will open one of the other doors with a goat and you will lose if you switch your choice. So, if you switch your choice you will win the car with probability $2/3$.*

## Wait a minute!

Then I asked myself "*What is the probability of winning the Monty Hall game if you are allowed to open more than one door? What about having more than one winning choice?*" I was not sure about the answer, so I decided to write a program to simulate the game!

## Extending the Problem
My friend Romain immediately jumped into writing formulas and came up with the following:

### Assume we are taking a strategy in which we **always** switch our choice.
Let the following extend the game:  
* $N$ be the number of doors  
* $W$ the number of winning doors  
* $D$ the number of doors you are allowed to open  

## Deriving a Formula
The probability of winning the game is given by two possible cases:
1. Your original choice is a winning door and you open $D$ doors with goats, then switch your choice.
2. Your  original choice is a losing door and you open $D$ doors with goats, then switch your choice.  

### Case 1
The probability of choosing a winning door after switching given that we originally chose a loosing door is given by:
$$\frac{W}{N-D-1} \times \frac{N-W}{N}$$
Since we are always switching, the probability of choosing a winning door is $\frac{W}{N-D-1}$ . The $-1$ comes from the switch. We multiply this by the initial probability of choosing a losing door $\frac{N-W}{N}$.

###  Case 2
The probability of choosing a winning door given that we originally chose a winning door is given by:
$$\frac{W-1}{N-D-1} \times \frac{W}{N}$$
Notice that we need to do $W-1$ because we are not allowed to open the door we originally chose. The probability of choosing a winning door is $\frac{W-1}{N-D-1}$ . We multiply this by the initial probability of choosing a winning door $\frac{W}{N}$


### Final Formula
Since we can get Case 1 **OR** Case 2, we need to add them together to get the final formula:

$$P(\text{win}) = \frac{W}{N-D-1} \times \frac{N-W}{N} + \frac{W-1}{N-D-1} \times \frac{W}{N}$$

We can simplify this to:
$$P(\text{win}) = \frac{W*(N-1)}{N*(N-D-1)}$$
###### i'm clearly bored