20241015170711

Tags: [[Quantum Systems]]

The reason physical simulation needs to be done with quantum simulation is due to the innate quantum properties the world has. The [[Hilbert Space|Hilbert space]] issue results in growth that is unsustainable, as the universe reaches a hard limit.

## Hamiltonian Dynamics
[[Schrodinger's Equation]] describes the time evolution of a quantum system. The generic state of a Hamiltonian is time dependent. In order to simulate Hamiltonian dynamics on a quantum system, there are a few steps that needs to be taken. 
- Mapping the $|Φ(t)\rangle$ state to a state on a quantum computer
- Calculating or performing measurements of a physical observable at a time
	- The inner product is involve in making measurements based on observables

## Properties
There are five powerful properties (not formally proven) about quantum simulations
- if $\hat{{H}}$ can be simulated efficiently, then so can $c\hat{H}$ with $c \in \mathbb(R)$
- If $\hat{H}_{1}$ and $\hat{H}_{2}$ can be simulated efficiently, then so can $\hat{H}_{1} + \hat{H}_{2}$
- if $\hat{H}$ is diagonal, $\hat{H}$ can be simulated efficiently
- if $\hat{H}$ can be simulated efficiently and $\hat{U}$ is a unitary operator that can be implemented efficiently on quantum hardware, then $\hat{H}' = \hat{U}\hat{H}\hat{U}^{-1}$ can be simulated efficiently
- Pauli matrices are exponential in terms of mapping
Both Pauli X and Y gates can be represented with Pauli Z gates. 

## Trotterization
If the terms of the Hamiltonian commute, then $[\hat{H}_{i}, \hat{H}_{j}] = 0$, then the time evolution is given by 

If the terms of the Hamiltonian do not commute, $[\hat{H}_{i}, \hat{H}_{j}] ≠ 0$


## Digital Quantum Simulation
###### Example
Three spin-1/2 particles prepared in the state $|\uparrow\uparrow\uparrow\rangle$ with the Hamiltonian 
#### $$\hat{H}_{s} = ω(\hat{σ}_{x} \otimes \hat{σ}_{y} \otimes \hat{σ}_{z})$$
Since there are only spin-1/2 particles, each particle can be represented by a qubit. The map is just the identity $$\hat{J}|\uparrow\uparrow\uparrow\rangle = |000\rangle\ \ \ \ \ \ \hat{H}_{s} = \hat{H}$$
The Hamiltonian can be simplified down to
#### $$\hat{H} = ω\hat{A}\hat{B}(\mathbb{1} \otimes \mathbb{1} \otimes \hat{s}_{z})\hat{B}^{\dagger}\hat{A}^{\dagger}$$
## Spin Boson Model
A spin-boson model is a system of bosons that have their own interactions that can be used to model various physical systems. 
- quantum impurities
- quantum superradiance
There are three observables for a spin-boson model, average magnetization, occupation number, and spin correlation. 
Since there is an infinite number of boson modes, low-energy dynamics are truncated away. There are then two established modes for encoding boson modes. Unary encoding, whose formula is $$|m\rangle \rightarrow |00\dots 1 \dots 00$$
and binary encoding, whose formula is $$|m\rangle \rightarrow Π \left|\left[ \frac{m}{2^i} mod 2|\right]\right\rangle$$
In qubit number, unary vs binary goes as O(m) vs O(logm), but with gate number, unary vs binary goes as O(m) vs O(mlogm). The relationship between max occupation number and ratio of two-qubit depth unary and binary encoding is inverse log. 
___
# References
[[Quantum Simulation of Physical Systems]]

