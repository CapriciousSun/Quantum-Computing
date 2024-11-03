20241015163210

Tags: [[Quantum Information]], [[Quantum Systems]]

Physical qubits are what people are working with when using a quantum system. Therefore, they are influenced by noise and are not completely accurate. Logical qubits, on the other hand, are perfect and have no leakages to classical systems via [[Errors & Decoherence]]. 

Logical qubits, nowadays, are made with ancilla qubits, which are redundant physical qubits. If noise affects a single physical qubit, ancilla qubits can detect that error and restore the state. Currently, better error correction code is an important area of research. 

```python
cirq = QuantumCircuit(5)
cirq.cx(0, 1)
cirq.cx(0, 2)
cirq.x(1)

cirq.cx(0, 3)
cirq.cx(1, 4)

cirq.cx(0, 4)
cirq.cx(2, 4)

cirq.measure_active()

```

The above code snippet is a basic ancilla qubit circuit. This creates the system $$|ψ_{L}\rangle = α|000\rangle + β|111\rangle$$

The Threshold Theorem is a theorem that stiplates the ancilla qubits are error-prone themselves. However, this is only a theorem, a provably error correction would enable the creation of true logical qubits. 

There are some recent experiments that have demonstrated the creation of logical qubit systems. 
___
# References
[[F24_0x05 Fault Tolerance & Applications]]
