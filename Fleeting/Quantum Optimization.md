20241015171742

Tags: [[Classical Information]], [[Quantum Information]]

There are several applications that quantum computing could offer an advantage to. This includes [[RSA Decryption]], [[Grover's Algorithm]], and. other uses of quantum problem solving. 

Fields of logistics and operations research, as well as industrial engineering, have factorial level problems as their worst case. Quantum computing does not guarantee an exponential speedup, but it can help provide problem-specific advantages. There are some uses today, like superconducting quantum annealers and the QAOA algorithm. 

## Matrix Solving
Matrix solving is what most engineering calculations are on. Systems of partial differential equations are important to engineering as well. For example, the Harrow-Hassidim-Lloyd algorithm solves sparse matrices in O(log N) time. However, it's O(N) to just solve the problem regularly, and the output wouldn't be a solution field, only an expectation value, so consideration needs to be made regarding using quantum computing here. 

## Continuous Optimization
Continuous optimization are done by iterating over a problem many times in order to reach the best solution. It can typically be done with analytical means. 

## Discrete/Combinatorial Optimization
Combinatorial optimization have a certain number of parts, and they have to be permuted in order to find a solution. Example problems include the max-cut problem and the traveling salesman problem. 

## Adiabatic Theorem
Quantum computing can offer advantages to a combinatorial optimization problem. This is rooted in the adiabatic theorem of quantum computing, which puts the answer to a problem at the lowest possible energy state, and the calculations bring it closer to the lowest energy state. 
#### Annealing
Annealing is the idea of starting out with a chaotic system given a higher "temperature" and then lowering the temperature, which causes rearrangement within the system and then finally hopefully arriving at an approximated optimal solutions. Quantum annealing algorithms are commercially available and could be used in logistics applications currently. 

## Quantum Approximate Optimization Algorithm
This is a gate based version of quantum annealing, where an ansatz is given with two Hamiltonians, one which simulates the objective function and the second simulates cross-qubit interactions, and the measurement is gathered. That process is run over again with new parameters until a suitable answer is reached. 

## Applications
Some fields have have a strong emphasis in optimization is industrial engineering and operations research, since they involve optimizing a single component and seeing how it can fit into a larger system. 
___
# References
[[F24_0x05 Fault Tolerance & Applications]]
