20250131101555

Tags: [[Quantum Information]]

An *expectation value* is an average of a measurement taken on a quantum system. 
___

## Position
For position, the expectation value reflects how likely a particle is to be measured at a specific point.
```ad-formula
#### Position Expectation Value
#### $$\langle x \rangle = \int_{-\infty}^{\infty}Ψ^{*}xΨdx$$
where $x$ is the position of the particle the measurement is done on. 
```

## Momentum
The expectation value for momentum is an operation done on the position expectation value. Linear momentum classical is calculated as $p = mv$, where $v$ is the velocity, or change in the position. 
```ad-formula
#### Momentum Expectation Value
#### $$\frac{d\langle x \rangle}{dt} = \int x \frac{\partial}{\partial t} |Ψ|^{2} dx =  \frac{i\hbar}{2m} \int x \frac{\partial}{\partial x} \left( Ψ^{*} \frac{\partial Ψ}{\partial x} - \frac{\partial Ψ^{*}}{\partial x} Ψ \right)dx = $$
```

## Energy
The formula for kinetic energy expectation value is 
```ad-formula
#### Energy Expectation Value
#### $$\langle T_{n} \rangle = \frac{\langle p_{n}^{2} \rangle}{2m} = \frac{1}{2m}\left( \frac{nπh}{L} \right)^{2}$$
```

The lowest allowed energy state is $n = 1$. So the expectation value of kinetic energy is always greater than zero. And since $\langle T \rangle ^{2} - \langle T^{2} \rangle = 0$, the uncertainty regarding energy is zero. 

## Physical Systems
#### Superconducting Qubits (Josephson Junctions)
In superconducting qubits, expectation value is taken by measuring the frequency of the qubit, since the Josephson effect creates a clear correlation between voltage and frequency at near absolute zero.
___
# References
