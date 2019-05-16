
The purpose of this project is to create a more efficient means for a  solution for Partially Observable Markov Decision Processes (POMDPs) .We wish to find the existence of a best possible solution if it exists otherwise we wish to provide an excellent approximation for the same.Potential applications inlcude a better quantification of uncertainty commonly encountered in Reinforcement Learning Applications ranging from co-operative usage in drones to designing better agents for more interactive gaming to more dynamic environments such as Weather Modelling and disease prediction.


One of the crucial issues that has ensured a very low adaptation of POMDPs despite their wide range of applicability involves the issue of scalability to real-world systems with an enormous range of uncertain states and observations.

We wish to tackle this process steadily by increasing the complexity of our testing environments as a step by step process.Therefore we choose to begin with what is arguably the classical training ground for POMDPs (analogous to the knapsack problem in Dynamic Problem or one of the standard datasets used extensively in ML research )

The Tiger Problem which is our training ground broadly involves the following situations:

A tiger is put with equal probability behind one of two doors, while treasure is put behind the other one. You are standing in front of the two closed doors and need to decide which one to open. If you open the door with the tiger, you will get hurt by the tiger (negative reward), but if you open the door with the treasure, you receive a positive reward. Instead of opening a door right away, you also have the option to wait and listen for tiger noises. But listening is neither free nor entirely accurate. You might hear the tiger behind the left door while it is actually behind the right door and vice versa.

The states of the system are tiger behind the left door (tiger-left) and tiger behind the right door (tiger-right).

Available actions are: open the left door (open-left), open the right door (open-right) or to listen (listen).

Rewards associated with these actions depend on the resulting state: +10 for opening the correct door (the door with treasure), -100 for opening the door with the tiger. A reward of -1 is the cost of listening.

As a result of listening, there are two observations: either you hear the tiger on the right (tiger-right), or you hear it on the left (tiger-left). 

Now the tiger problem has already been solved by various methods and one standard method used today extensively in a wide range of situations is the Point Based Value Iteration.We shall take the performance of this algorithm as the benchmark in our journey to find a possibly better algorithm 

Our implementation is python based and we base it on the excellent  interface and implementation given by Malayandi at https://github.com/malayandi/Tiger-Problem-POMDP

The first approach that we are going to use is to model the POMDP as a hidden markov model acting on a point process .We choose to do this for the following reasons:
1.The approximation of POMDP as a hidden markov model has proved to pretty useful to researrchers in the past
2 The point based decomposition used in Point Based Value Iteration inspires the usage of a point process moreover considering the dependence on the past histories we prefer a self exciting or Hawkes Process
