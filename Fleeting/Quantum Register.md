20250103211056

Tags: [[Classical Information]], [[Quantum Information]]

A quantum register is any sort of representation or abstraction of quantum information. The [[Quantum States|state]] of a register is the contents of said register at any given moment. Registers imply that the information stored within the register can be stored and manipulated. 

## Register Types
There are two types of registers, simple registers and compound registers. 
```ad-note
### Simple Registers
A simple register X would be any alphabet Σ

The classical register set of a simple register X is Σ where X = Σ.
```

```ad-note
### Compound Registers
A compound register is a tuple of X = (Y$_{1}$, ..., Y$_{n}$), where n is some natural number.

The classical register set of a compound register is the Cartesian product Σ = Γ$_{1} \times \dots \times$ Γ$_{n}$ where Γ$_{k}$ denotes a classical state set associated with the register Y$_{k}$ for each k $\in$ {1, ..., n}
```

A compound register can be organized into a tree of sorts, where every sub-register is a leaf on said tree. 

## Probabilistic States
For a quantum register X, the probabilistic states refer to the probability distribution of the various classical states it has. For a classical state set of X where the register is some alphabet Σ, a probabilistic state of X is done so with the probability vector $p \in \mathcal{P}(\text{Σ})$, where the value of $p(a)$ represents the probability that the classical state $a \in \text{Σ}$. 

Probabilistic states are different from quantum states in the sense that probabilistic states are represented with probability vectors, whereas quantum states are represented with [[Density Operators|density operators]]. 

## Complex Euclidean Space
The complex Euclidean space associated with a register X is defined as $\mathbb{C}^{\text{Σ}}$ where $\text{Σ}$ is the classical state set of X and is denoted as $\mathcal{X}$. For a compound register with registers Y$_{1}$, ..., Y$_{n}$ will be denoted by $\mathcal{Y}_{1}, \dots, \mathcal{Y}_{n}$. If X = (Y$_{1}$, ..., Y$_{n}$), then the complex Euclidean space $\mathcal{X}$ is given by $\mathcal{X} = \mathcal{Y}_{1} \otimes \dots \otimes \mathcal{Y}_{n}$. This is derived from the fact that $\mathcal{X} = \mathbb{C}^{\text{Σ}} = \mathbb{C}^{\text{Γ}_{1} \times \dots \times \text{Γ}_{n}} = \mathcal{Y}_{1} \otimes \dots \otimes \mathcal{Y}_{n}$, since $\mathcal{Y}_{1} = \mathbb{C}^{\text{Γ}_{1}}$, $\mathcal{Y}_{2} = \mathbb{C}^{\text{Γ}_{2}}$, and so on. 

For every complex Euclidean space $\mathcal{X}$ there is a convex set $\text{D}(\mathcal{X})$ where for an alphabet $\text{Γ}$ has a collection $\{ρ_{a} : a \in \text{Γ}\} \subseteq \text{D}(\mathcal{X})$ of quantum states and a probability vector $p \in \mathcal{P}(\text{Γ})$. Therefore, the convex combination $ρ = \sum_{a \in \text{Γ}}p(a)ρ_{a}$ is an element of $\text{D}(\mathcal{X})$.
___
# References
[[The Theory of Quantum Information]]
