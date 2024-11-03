20241001162633

Tags: [[Quantum Systems]], [[Quantum Information]], [[Classical Information]]

Density matrices are a system with a lot of qubits or a single state that's prepared and measured many times. It gives a unified representation of quantum coherence and classical mixtures. 

For example, with a Hadamard state, the density matrix would show a 50-50 classical mixture that looks like $$\rho_{+} = \begin{pmatrix}
\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2}
\end{pmatrix}$$
The quantum part of the density matrix can have its states detected and estimated. Environmental effects can cause decoherence, when the qubit either becomes entangled with something within the environment or the qubit measurement is incorrect. Schrodinger's equation assumes a perfectly isolated quantum system, but in the real world, there is constant chaos. The Lindbladian is a formula that measures open quantum systems $$\frac{d\rho}{dt} = -i[H,\rho]+\sum_{k}\left( L_{k}\rho L^{\dagger}_{k}-\frac{1}{2}\{L^{\dagger}_{k}L_{k},\rho\}\right)$$
