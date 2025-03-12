20240511231850

Tags: [[Quantum Information]]

A quantum state is the state of an isolated system at any given time t. It is defined in conjunction with a [[Quantum Register|quantum register]], and it is represented by a[[Density Operators|density operator]]. In a simplified form, it is represented by $|ψ\rangle$ belonging to a [[Hilbert Space|Hilbert space]] $H$ called the state space using complex numbers. The state space is composed of vectors with lengths 1. 
## Defintion
For a quantum register X, the state is some $ρ \in \text{D}(\mathcal{X})$ for some choice of [[Quantum Register#Complex Euclidean Space|complex Euclidean space]] $\mathcal{X}$ that is associated with the register X. Here, the term state is always used to refer to quantum state, as classical states would always be emphasizes as being classical. 

From the complex Euclidean space proofs that show a probability vector $ρ$ is a mixture of states, it can be reasoned that random selections of quantum states are represented by convex combinations of density operators. 
## Qubit States
There are a few different types of qubit states, namely standard basis and plus/minus states
```ad-note
### Standard Basis States
$$|0\rangle = \begin{pmatrix}
1 \\
0
\end{pmatrix}\ \ \ \ |1\rangle = \begin{pmatrix}
0 \\
1
\end{pmatrix}$$
```

```ad-note
### Plus/Minus States
$$|+\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle\text{     and   } |-\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle$$
```

The Bell state is developed by John S. Bell in 1964 and it demonstrates superposition and entanglement, whilst ruling out the hidden variable theory. This is the building block of quantum computing.
![[Pasted image 20240917162154.png]]
```ad-note
### The four Bell states
$$|\Phi^+\rangle = \frac{1}{\sqrt{ 2 }}(|00\rangle + |11\rangle)$$
$$|\Phi^-\rangle = \frac{1}{\sqrt{ 2 }}(|00\rangle - |11\rangle)$$
$$|\Psi^+\rangle = \frac{1}{\sqrt{ 2 }}(|01\rangle + |10\rangle)$$
$$|\Psi^-\rangle = \frac{1}{\sqrt{ 2 }}(|01\rangle - |10\rangle)$$
```

The Hadamard gate places $q_0$ into superposition and the node connecting $q_0$ and $q_1$ entangles both qubits. 
___
# References
[[Understanding Quantum Information and Computation - Lesson 1 - Single Systems]]
[[F24_0x02 Measurements, Estimators, and Circuits]]
[[The Theory of Quantum Information]]
[[Understanding Quantum Technologies 6th Edition]]
