# Game-Theory-Toolkit
Collection of algorithms, environments, and examples of applications of Game Theory and Reinforcement Learning.

## Structure
- /algorithms: Contains fast Python implementions of all the algorithms used. 
- /environments: Contains various games for each of the parameter combinations.
- /examples: Contains Jupyter notebooks presenting the use of successful algorithms on various environments.

## Basic Description

Here is a guide for the different kind of games we'll encounter. For each combination of the following parameters, I provide example environments and the best algorithm to use in that case. 
This repository is meant to act as a first-stop resource for anyone who wants to apply game-theory to an actual problem, and as a survey for any researcher looking to develop new algorithms for 
cases currently that don't have a good algorithm.

Here are the parameters I'll be considering:

- Number of Players:
  - 1 player: Agent vs Environment.
  - 2 player: Player vs Player.
  - N player: Player vs N-1 players.
  
- Dynamics:
  - Normal Form: Single-simultaneous turn.
    - Stackelberg Option: The agent is able to reveal the strategy it'll commit to before the other player makes a decision.
  - Extensive Form: Turn by turn games.
  - Simultaneous Action: Multiple simultaneous turns.
    - Stackelberg Option: The agent is able to reveal the strategy it'll commit to before the other player makes a decision.
  
 
- Information Type:
  - Perfect Information: Each player knows the current state.
  - Imperfect Information: Some states look identical to some players.

- Reward Type:
  - Zero-Sum: Total reward of all players add to 0.
  - General-Sum: All Players can have any reward.

- Randomness:
  - Deterministic: All state transitions are deterministic.
  - Stochastic: Some state transitions are chance-based.
 
- Model available:
  - Model-based: Game mechanics are known and the game can be simulated.
  - Model-free On-policy: Game mechanics aren't known to the agent but the game can be simulated.
  - Model-free Off-policy: Game mechanics aren't known to the agent and the game can't be simulated.

- State Space Size:
  - Finite Discrete: Number of states is bounded. We'll discuss which algorithms to use for various scales. 
  - Infinite Discrete: Number of states is countably infinite.
  - Continuous: Number of states is uncountably infinite.

- Action Size:
  - Finite Discrete: Number of actions is bounded.
  - Infinite Discrete: Number of actions is countably infinite.
  - Continuous: Number of actions are uncountably infinite.



