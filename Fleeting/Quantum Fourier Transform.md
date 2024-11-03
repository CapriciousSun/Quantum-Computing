20241016121150

Tags: [[Quantum Algorithm]], [[Quantum Information]]

The basis of the Fourier Transform is the Fourier Integral $$f(t) = \int_{0}^{\infty}{[A(ω)\cos(ωt) + B(ω)\sin(ωt)]}dω$$
It is a function that synthesizes a wave function in smaller wave functions. The frequency components of a time function can be obtained with the inverse of the synthesis $$$$On a computer, the discrete form of the Fourier Integral is used $$f(j) = \sum_{k = 0}^{N - 1}{t(k)e^{\frac{i2π}{Ν}jk}};\ \ \ \ j = 0\text{ to }N - 1$$When expanding all the frequencies out, it becomes a series of exponential functions. This can be organized into a matrix with the horizontal being the k-index and the vertical being the j-index $$\begin{bmatrix}
1 & 1 & 1 & \dots & 1 \\
1 & p^{1* 1} & p^{1 * 2} & \dots & p^{1 * (N - 1)} \\
. & . & . & . & . \\
. & . & . & . & . \\
. & . & . & . & . \\
1 & p^{1 * (N - 1)} & p^{n * (N - 1)} & \dots & P^{(N - 1)*(N - 1)}
\end{bmatrix}\begin{bmatrix}
t(0) \\
t(1) \\
. \\
. \\
. \\
t(N - 1)
\end{bmatrix}$$A Quantum Fourier Transform (QFT) is based on the matrix form of the classical Fourier Transform. The exponentials of the Quantum Fourier Transform differ only in the j and k indices and that can be represented as qubit spin in the form of phase rotation. 