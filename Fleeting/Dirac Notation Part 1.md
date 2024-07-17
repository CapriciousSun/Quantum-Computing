20231101716

Tags: [[Classical Information]]

The Dirac Notation, or the bra-ket notation, is used in describing vectors, and it is central to the way quantum information is described. In the notation, Σ can be any ordered classical state set. The ordering is important. Many classical states have a standard ordering, and for those that don't, one can be chosen. The simplest form is $$\ket{Ψ} = α\ket{0} + β\ket{1}$$where for some possibility ψ, there is a α possibility of 0 and a β possibility of 1. Whatever is in the ket operator represents the value, and the coefficient (the amplitude) represents the possibility of getting the value.
The matrix representation of the probability state would be like $$\ket{Ψ} = \begin{pmatrix}α\\β\end{pmatrix}$$$\ket{a}$ is denoted as the column vector with a 1 in an entry corresponding to $a \in Σ$, with 0 for every other entry. 
As an example, if Σ = {0, 1}, then $$\ket{0} = \begin{pmatrix}1\\0\end{pmatrix}\ \ \ and\ \ \ \ket{1} = \begin{pmatrix}0\\1\end{pmatrix}$$
An example of a regularly unordered set would be if Σ = {♣,♦,♥,♠}, then
$$\ket{♣} = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}\ \ \ \
  \ket{♦} = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}\ \ \ \ 
  \ket{♥} = \begin{pmatrix}0\\0\\1\\0\end{pmatrix}\ \ \ \ 
  \ket{♠} = \begin{pmatrix}0\\0\\0\\1\end{pmatrix}$$
Classical states mean set means that the sets are always non-empty and finite, and they are called standard basis vectors, something that any vector can be expressed by, for example $$\begin{pmatrix}\frac{3}{4}\\\frac{1}{4}\end{pmatrix} = \frac{3}{4}\ket{0} +\ \frac{1}{4}\ket{1}$$Since total possibility of finding a value is 100%, $$|α|^2\ +\ |β|^2 = 1$$It would be impossible to find α and β from a single qubit, since a single qubit would collapse once the answer is found, so multiple qubits of the same configuration would be needed to find a general probability, like sampling. 
___
# References
[[Understanding Quantum Information and Computation - Lesson 1 - Single Systems]]
[[Quantum Computing for the Quantum Curious.pdf]]