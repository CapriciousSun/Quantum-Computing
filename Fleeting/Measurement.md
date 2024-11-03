 20240924162510

Tags: [[Classical Information]], [[Quantum Information]]

Measurement is projective, as if casting a shadow onto the state vector. It's innately a matrix operator, extracting the probability amplitude of a basis state. $$|0\rangle \langle 0| = P_{0} = \begin{pmatrix}
1 & 0
\end{pmatrix}\ \ \ \ \begin{pmatrix}
1 \\
0
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\
0  & 0
\end{pmatrix}$$
$$|1\rangle \langle 1| = P_{1} = \begin{pmatrix}
0 & 1
\end{pmatrix}\ \ \ \ \begin{pmatrix}
0 \\
1
\end{pmatrix} = \begin{pmatrix}
0 & 0 \\
0  & 1
\end{pmatrix}$$
A coordinate transformation would result in a measurement in other bases. Physically, it's a Z measurement and the results would be the same if other basis were measured. The expectation value is what the average of many results should be. 

In [[Qiskit]], observables are defined as a set of Pauli matrices. A Z-observable is the standard basis measurement, and the expectation values are within the range -1~1. To get a expectation value within the range of 0~1 $$\begin{pmatrix}
\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }}
\end{pmatrix}\begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix}\begin{pmatrix}
\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }}
\end{pmatrix} = \frac{1}{2}$$
An SparsePauliOp on the X basis would result in 1, whereas the Y basis and Z basis would result in an answer close to 0. 