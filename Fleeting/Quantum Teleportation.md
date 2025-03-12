20250103175747

Tags: [[Classical Information]], [[Quantum Information]]

Quantum teleportation is a technique that allows for the transferal of information from an unknown [[Quantum States|quantum state]] from one system to another. This is not instantaneous, as classical information still needs to be sent to the sender and receiver. The teleportation part merely means that neither party needs to move. 

## The Mechanism
The working details of quantum teleportation involves the no-cloning theorem, which states that a qubit of unknown quantum state cannot be copied to another qubit without destroying the original qubit. 

## The Steps
Quantum teleportation involves "scanning" a qubit, sending the information to another qubit via quantum entanglement, and recreating the information with the sent information. Put into practice, it starts with two entangled qubits, qubit 1 and qubit 2. One of the entangled qubit (qubit 1) is entangled with a separate, unknown quantum state (qubit 0). This causes the other entangled qubit (qubit 2) to change its information due to the entanglement it has with qubit 1. Measuring qubit 1 causes it to collapse, which puts qubit 0 in entanglement with qubit 2 instead. Based on qubit 1's measurement, qubit 2 is altered with an X gate. Next, qubit 0 is put through a Hadamard gate, which puts it in superposition. Finally, qubit 0 is measured, and the measurement is used to alter qubit 2 with a Pauli Z gate. 

## The Significance of Quantum Teleportation
Quantum teleportation does not allow for instantaneous communication. The true utility of quantum teleportation comes from the fact that it allows for the transferal of quantum information using a classical channel. This enables long distance communication, as without quantum teleportation, the 2 qubits would have to be close and physically interact in order to share quantum information.

## Usages
Quantum teleportation can be used for quantum distillation, a protocol that takes many pairs of entangled qubits and condenses the quantum information out of them in order to create a lesser number of more strongly entangled pairs.
___
# References
[[Quantum Computing for the Quantum Curious]]
[[Quantum Networks Enhanced by Distributed Quantum Memories]]
