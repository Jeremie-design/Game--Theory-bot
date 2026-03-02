# Adaptive Prisoner’s Dilemma Learning Agent

An adaptive machine learning agent that plays repeated rounds of the Prisoner’s Dilemma against a human opponent.  
The agent uses online logistic regression with gradient descent to learn behavioral patterns and dynamically adjust its strategy over time.

---

## Overview

This project investigates how lightweight machine learning models can be applied to classical problems in game theory and strategic decision-making.

Rather than relying on fixed heuristics such as Tit-for-Tat, the agent learns directly from interaction. By observing both its own past actions and those of its opponent, the model adapts in real time to maximize long-term payoff under repeated play.

The goal of the project is not to build a maximally strong agent, but to explore **interpretability, learning dynamics, and emergent behavior** in a minimal neural architecture.

---

## Technical Approach

### State Representation
The agent maintains a fixed-size sliding memory of the previous **nine rounds**, consisting of:
- Its own past actions
- The opponent’s past actions

Each action is encoded numerically (`0 = Cooperate`, `1 = Defect`).  
A bias term is appended, resulting in a 19-dimensional input vector:


---

### Model Architecture
The decision-making model is a **single-neuron logistic regression classifier**:

 (`σ(w⋅x)`)
 
- X input vector of its last moves and opponent's last move 
- W The weight vector (Learing part)
- σ The sigmoid output represents the probability of defection. The final action is selected deterministically by rounding the output

This design choice prioritizes interpretability and analytical clarity over raw performance.

---

### Learning Rule
After each round, the agent receives a reward from the Prisoner’s Dilemma payoff matrix and updates its weights using **online gradient descent**:

- Prediction error is computed as `reward − output`
- The sigmoid derivative is applied during backpropagation
- No replay buffer or offline training is used

This allows the agent to adapt continuously in non-stationary environments.

---

## Game Flow

Each round proceeds as follows:

1. The human player selects **Cooperate (C)** or **Defect (D)**
2. The agent predicts its action based on recent interaction history
3. Both players receive rewards according to the payoff matrix
4. The agent updates its internal weights
5. Cumulative scores are tracked over time

---

## Payoff Matrix

| Player Action | Agent Action | Player Reward | Agent Reward |
|--------------|-------------|---------------|--------------|
| Cooperate | Cooperate | 3 | 3 |
| Cooperate | Defect | 0 | 5 |
| Defect | Cooperate | 5 | 0 |
| Defect | Defect | 0 | 0 |

---

## Key Features

- Online learning with no pre-training
- Adaptive behavior against diverse opponent strategies
- Sliding temporal memory for pattern recognition
- Interpretable neural model
- Fully interactive command-line interface

---

## Getting Started

### Requirements
- Python 3.x
- NumPy

Install dependencies:
```bash
pip install numpy
python adaptive_prisoner_bot.py
