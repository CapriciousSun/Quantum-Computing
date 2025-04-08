20241030171420

Tags: [[Quantum Information]], [[Quantum Computing]]

For a system f(x) $$f(x), x \in \{0, 1\}$$
$$f(0) \rightarrow 0\text{ or }1$$
$$f(1) \rightarrow 0\text{ or }1$$
If all inputs to f give the same output, then f is a constant. If half the inputs give 0 as output and half the inputs give 1 as output, then f is balanced. 

## The Deutsch Problem
The stipulation of the Deutsch problem is, given an f that is constant or balanced, determine if it is constant or balanced. This problem cannot be solved classically in less than 2 queries, since both states would need to be tested (this is assuming that there are two possible outputs of f). 

#### The Quantum Solution
In order to test f(0) and f(1), the quantum method offers a solution in the form of the oracle gate, which is a blackbox (or a function where the workings are unknown to the user). Both the 0 and 1 qubits are put in superposition, run through the oracle, and then measured. 

$$ψ_{0} = |01\rangle$$
$$ψ_{1} = \frac{1}{\sqrt{ 2 }}(|0\rangle + |1\rangle) \frac{1}{\sqrt{ 2 }}(|0\rangle - |1\rangle) = \frac{1}{\sqrt{ 2 }}(|00\rangle - |01\rangle + |10\rangle - |11\rangle)$$
This all equals $$\frac{1}{2}\begin{bmatrix}
1 \\
-1 \\
1 \\
-1
\end{bmatrix}$$
$$ψ_{2} = \frac{1}{2}[|0\rangle |0 \oplus f(0)\rangle - |0\rangle | 1 \oplus f(0)\rangle + |1\rangle|0 \oplus f(1) - |1\rangle|1 \oplus f(1)\rangle]$$
$$ψ_{2} = \frac{1}{2} [(-1)^{f(0)}|0\rangle(|0\rangle - |1\rangle)] + [(-1)^{f(1)}|1\rangle(|0\rangle - |1\rangle)]$$

$$ψ_{2} = \frac{1}{2}[(-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle] * (|0\rangle - |1\rangle)$$
$$ψ_{2} = \frac{1}{2}(-1)^{f(0)}[|0\rangle + (-1)^{f(0) \oplus f(1)}|1\rangle]$$
$$ψ_{2} = \frac{1}{2}[|0\rangle + (-1)^{f(0) \oplus f(1)}|1\rangle](|0\rangle - |1\rangle)$$
Now, considering the first qubit only $$\frac{1}{\sqrt{ 2 }}[|0\rangle + (-1)^{f(0) \oplus f(1)}|1\rangle]$$$$ψ_{3} = \frac{1}{2}[|0\rangle + |1\rangle + ]$$
$$\frac{1}{2}[(1 + (-1)^{f(0) \oplus f(1)})|0\rangle + (1 - (-1)^{f(0) \oplus f(1)})|1\rangle]$$
The result of this is that if $$f(0) \oplus f(1) = 0$$
then f(0) = f(1), and f is constant. The state would be $$\frac{1}{2}(2|0\rangle + 0|1\rangle)$$If the result is $$f(0) \oplus f(1) = 1$$
then f(0) ≠ f(1), and f is balanced. The state would be $$\frac{1}{2}(0|0\rangle + 2|1\rangle)$$
