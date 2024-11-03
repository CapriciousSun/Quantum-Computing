20241001170709

Tags: [[Quantum Systems]]

The decoherence of a qubit comes in several "channels". This includes amplitude damping, depolarization, and dephasing. 
#### Amplitude damping
By measuring $T_{1}$ of individual qubits or with many in parallel. When all the $T_{1}$s are measured, it can be plotted onto a chart. 

#### Phase damping
When a qubit is put in superposition, it has a very well defined phase. As information regarding the phase leaks into the classical elements of the density matrix, phase damping occurs. $T_{2}$ is what determines phase damping, and it can be measured using the Hahn Echo sequence. By applying a Hadamard gate, waiting, applying an X gate, waiting,  applying another Hadamard gate and measuring, the decoherence can be measured. Another is $T_{2}^*$, which involves applying a Hadamard gate, waiting, applying an $R_{z}$ gate, waiting, and then measuring. 

The combination of $T_{1}$ and $T_{2}$ processes lead to single-qubit errors, or when the statevector is not aligned with where it's supposed to be. Bit flips and phase flips are $T_{1}$ and $T_{2}$ errors respectively. 

Aside from environmental errors, gate noise can also cause errors. Gate fidelity can be measured to measure how many gates can be run before decoherence. 
___
# References
