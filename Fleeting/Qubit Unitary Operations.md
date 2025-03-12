20241224194553

Tags: [[Quantum Systems]]

A qubit unitary operation is essentially mathematical representation of a [[Quantum Gates|quantum gate]], where some [[Unitary Operations|unitary gate]] is done on a qubit. There are a few standard operations. 

## Pauli Matrices
Pauli matrices, a set of four unitary operations $$\mathbb{1} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}\ \ σ_{x} = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}\ \ σ_{y} = \begin{pmatrix}
0 & -i \\
-i & 0
\end{pmatrix}\ \ σ_{z} = \begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}$$
The $σ_{x}$ operation is a NOT gate, or a bit flip. The $σ_{z}$ operation is a phase flip. In practice, their operations look like $$σ_{x}|0\rangle = |1\rangle\ \ σ_{x}|1\rangle = |0\rangle\ \ σ_{z}|0\rangle = |0\rangle\ \ σ_{z}|1\rangle = -|1\rangle$$

## Hadamard Operation
The Hadamard operation, is a unitary operation that looks like $$\mathcal{H} = \begin{pmatrix}
\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }} & -\frac{1}{\sqrt{ 2 }}
\end{pmatrix}$$

## Phase Operation
A phase operation is a unitary operation on the phase rotation with formula $$\mathcal{P}_{θ} = \begin{pmatrix}
1 & 0 \\
0 & e^{iθ}
\end{pmatrix}$$
where θ is any real number. There are two specific phase operations, a rotation of $\frac{π}{2}$ and a rotation of $\frac{π}{4}$, called an S gate and a T gate $$\mathcal{S} = \mathcal{P}_{\frac{π}{2}} = \begin{pmatrix}
1 & 0 \\
0 & i
\end{pmatrix}\text{ and }\mathcal{T} = \mathcal{P}_{\frac{π}{4}} = \begin{pmatrix}
1 & 0 \\
0 & \frac{1 + i}{\sqrt{ 2 }}
\end{pmatrix}$$

## Operations
The [[Dirac Notation|Dirac notation]] can be used when doing operations with unitary operators. For example, with the T gate the 0 and 1 states $$\mathcal{T}|0\rangle = |0\rangle\ \ \mathcal{T}|1\rangle = \frac{1 + i}{\sqrt{ 2 }}|1\rangle$$
The T gate can also be applied to the + and - states $$\mathcal{T}|+\rangle = \mathcal{T}\left( \frac{1}{\sqrt{ 2 }}|0\rangle + \frac{1}{\sqrt{ 2 }}|1\rangle \right) = \frac{1}{\sqrt{ 2 }}\mathcal{T}|0\rangle + \frac{1}{\sqrt{ 2 }}\mathcal{T}|1\rangle = \frac{1}{\sqrt{ 2 }}|0\rangle + \frac{1 + i}{2}|1\rangle$$
Hadamard gates can be applied to the operation as well $$\mathcal{HT}|+\rangle = \mathcal{H}\left( \frac{1}{\sqrt{ 2 }}|0\rangle + \frac{1 + i}{\sqrt{ 2 }}|1\rangle \right) = \frac{1}{\sqrt{ 2 }}\mathcal{H}|0\rangle + \frac{1 + i}{2}\mathcal{H}|1\rangle$$
Since $\mathcal{H}|0\rangle = |+\rangle$ and $\mathcal{H}|1\rangle = |-\rangle$, the above expression can be further simplified to $$\frac{1}{\sqrt{ 2 }}|+\rangle + \frac{1 + i}{2}|-\rangle = \left( \frac{1}{2}|0\rangle + \frac{1}{2}|1\rangle \right) + \left( \frac{1 + i}{2\sqrt{ 2 }}|0\rangle - \frac{1 + i}{2\sqrt{ 2 }} |1\rangle\right)$$
___
# References
[[Understanding Quantum Information and Computation - Lesson 1 - Single Systems]]