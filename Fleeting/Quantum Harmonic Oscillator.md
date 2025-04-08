20250404203113

Tags: [[Quantum Systems]]

A quantum harmonic oscillator is a quantum analog of the classical harmonic oscillator. It is an important concept used to model wavefunction and energy of a particle.

## Formalism
The way to calculated a quantum harmonic oscillator is quite similar to a classical harmonic oscillator.
```ad-formula
#### General Form of a Quantum Harmonic Oscillator
Knowing the potential energy a quantum harmonic oscillator is the first step to solving the total energy of the system.
#### $$V(x) = \frac{1}{2}mω^{2}x^{2}$$
This can be plugged into the [[Schrodinger's Equation|Schrodinger equation]].
#### $$-\frac{\hbar^{2}}{2m} \frac{\partial^{2} ψ}{\partial x^{2}} + \frac{1}{2}mω^{2}x^{2}ψ = Eψ$$
Move around the the variables to isolate the double derivative.
#### $$\frac{\partial^{2} ψ}{\partial x^{2}} = \frac{2m}{\hbar^{2}} \left(\frac{1}{2}mω^{2}x^{2} - E \right)ψ $$
The energy variable can be removed for assuming $x$ to be sufficiently big.
#### $$\frac{\partial^{2} ψ}{\partial x^{2}} \approx \frac{mω^{2}x^{2}}{\hbar^{2}}ψ $$
Solving for the differential equation here yields the wavefunction. The reason we have two waves here is because general solutions to wavefunctions have one wave going in the positive direction and another going in the negative direction.
#### $$ψ(x) = Ax^{n}e^{-mωx^{2}/2\hbar} + Bx^{n}e^{mωx^{2}/2\hbar} $$
Since there is no barrier of sorts to stop the positive exponential from growing infinitely, so we would need to get rid of the second wave in order to preserve physical plausibility.
#### $$\psi_{0}x = A_{0}e^{-m\omega x^{2}/2\hbar} $$
Solving for energy gives us a pretty convenient energy equation.
#### $$E_{n} = \left(n + \frac{1}{2}\right)\hbar \omega : n = 0, 1, 2, \dots$$
```

## Ladder Operators
The ladder operator method, or algebraic method, to solving quantum harmonic oscillators uses two operators, the creation and annihilation operators. The two operators should both commute and anti-commute. 
```ad-formula
#### General Form of Ladder Operators
Creation and annihilation operators are defined by the variable $\hat{a}$ and $\hat{a}^{\dagger}$. Since they commute and anti-commute, the difference of $[\hat{a}, \hat{a}^{\dagger}]$ and $\{\hat{a}, \hat{a}^{\dagger}\}$ should be 0. We will define these operators in terms of matrices to make simulation on Qiskit easier later on.
#### $$\hat{a} = \begin{pmatrix}0 & 1 \\ 0 & 0 \end{pmatrix},\ \ \hat{a}^{\dagger} = \begin{pmatrix}0 & 0 \\ 1 & 0 \end{pmatrix} $$
```

