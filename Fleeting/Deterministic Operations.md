20240511203853

Tags: [[Classical Information]]

Deterministic operations are operations where the state of the system is entirely dependent on the state of the system before the operation and that nothing is left to chance. Deterministic operations are described by functions, notated by f, where $Σ\rightarrowΣ$ that transforms a classical state a to a state f(a) for every $a \in Σ$. For this function, there is a unique matrix M that satisfies $$M\ket{a} = \ket{f(a)}$$for every $a \in Σ$. In this matrix, it has one 1 for each column, and 0 for all other entries, like $$M(b, a) = \begin{cases}
1\ \ \ b = f(a)\\
0\ \ \ b \neq f(a)
\end{cases}$$If there were a probabilistic system v, then a matrix-vector multiplication can then be performed on it, resulting in a deterministic system Mv.
	For a set $Σ = {0, 1}$, there are four possible functions, with matrices $$$$
___
# References
[[Understanding Quantum Information and Computation - Lesson 1 - Single Systems]]
