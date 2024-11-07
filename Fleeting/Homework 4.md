## 1a
$$A * (\overline{A} + B * B) + (\overline{B + A}) * (\overline{A} + B)$$
Indepotent Law
$$A * (\overline{A} + B) + (\overline{A} + \overline{B}) * (\overline{A} + B)$$
DeMorgan's Law $$A * (\overline{A} + B)* + \overline{B} * \overline{A} * (\overline{A} + B)$$
Distributive Law $$(A + \overline{B} * \overline{A}) + (\overline{A} + B)$$
Absorption Law $$(A + \overline{B}) + (\overline{A} + B)$$
Distributive Law $$A\overline{A} + AB + \overline{B}\overline{A} + \overline{B}B$$
Complement Law $$AB + \overline{B}\overline{A}$$
## 1b
$$(\overline{BC}) + (ABC) + (\overline{A + \overline{B} + C})$$DeMorgan's Law $$\overline{B} + \overline{C} + (ABC) + \overline{(A + \overline{B} + C)}$$A
Redundancy Law $$\overline{B} + \overline{C} + BA + \overline{(A + \overline{B} + C)}$$
Redundancy Law $$\overline{C} + \overline{B} + A + \overline{(A + \overline{B} + C)}$$
Absorption Law $$\overline{C} + \overline{B} + A$$
## 1c
$$(A + B) * (\overline{A} + C) * (\overline{C} + B)$$
Distributive Law $$(A\overline{A} + AC + \overline{A}B + BC) * (\overline{C} + B)$$
Complement Law $$(AC + \overline{A}B + BC) * (\overline{C} + B)$$
Distributive Law $$(AC\overline{C} + ABC + \overline{A}B\overline{C} + \overline{A}BB + BC\overline{C} + BBC)$$
Complement Law $$(ABC + \overline{A}B\overline{C} + \overline{A}B + BC)$$
Absorption Law $$BC + \overline{A}B$$
Distributive Law $$B(C + \overline{A})$$
## 2a
$$(\overline{A} + C) * (\overline{B} + D + A) * (D + A * \overline{C}) * (\overline{D} + A) = 1$$
$$(\overline{A} * A * \overline{C} + \overline{A}D + A * C * \overline{C} + CD) * (A + \overline{B} + D) * (A + \overline{D}) = 1$$
$$(\overline{A}D + CD) * (A + \overline{B} + D) * (A + \overline{D}) = 1$$
$$(A * \overline{A} * D + \overline{A} * \overline{B} * D + \overline{A}DD + ACD + \overline{B}CD + CDD) * (A + \overline{D}) = 1$$
$$(\overline{A} * \overline{B} * D + \overline{A}D + ACD + \overline{B}CD + CD) * (A + \overline{D}) = 1$$
$$(\overline{A}D + CD) * (A + \overline{D}) = 1$$
$$(A\overline{A}D + \overline{A}D\overline{D} + ACD + CD\overline{D}) = 1$$
$$ACD = 1$$
$$ACD = ABCD + A\overline{B}CD = 1$$
## 2b
$$(((\overline{K}LN) * (L + M)) + ((\overline{K} + L + N) * (K * \overline{L} * \overline{M}))) * (\overline{K} + \overline{N}) = 1$$
$$(((\overline{K}LLN + \overline{K}LMN)) + ((\overline{K} * K * \overline{L} * \overline{M} + L * K * \overline{L} * \overline{M} + N * K * \overline{L} * \overline{M}))) * (\overline{K} + \overline{N}) = 1$$
$$(((\overline{K}LN + \overline{K}LMN)) + ((N * K * \overline{L} * \overline{M}))) * (\overline{K} + \overline{N}) = 1$$
$$(\overline{K}LN + K * \overline{L} * \overline{M} * N) * (\overline{K} + \overline{N}) = 1$$
$$\overline{K}\overline{K}LN + K * \overline{L} * \overline{M} * N * \overline{N} = 1$$
$$\overline{K}LN = 1$$
$$\overline{K}LN = \overline{K}LMN + \overline{K}L\overline{M}N = 1$$
## 3
$$Q = (\overline{X} * \overline{Y} * Z) + (XY\overline{Z}) + (\overline{X}Y\overline{Z}) + (X * \overline{Y} * \overline{Z})$$
```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[colormap/viridis]
\addplot3[
	surf,
	samples=18,
	domain=-3:3
]
{exp(-x^2-y^2)*x};
\end{axis}
\end{tikzpicture}
\end{document}
```




# 4

| A   | B   | C   | Output |
| --- | --- | --- | ------ |
| F   | F   | F   | T      |
| F   | F   | T   | F      |
| F   | T   | F   | T      |
| F   | T   | T   | T      |
| T   | F   | F   | F      |
| T   | F   | T   | F      |
| T   | T   | F   | F      |
| T   | T   | T   | T      |
$$(\overline{A} * \overline{B} * \overline{C}) + (\overline{A}B\overline{C}) + (\overline{A}BC) + (ABC) = 1$$
$$\overline{A} * \overline{C}(B + \overline{B}) + BC(\overline{A} + A)$$
$$\overline{A} * \overline{C} + BC$$
## 6
![[circ4.png]]

![[circ3.png]]

![[circ2.png]]

![[circ1.png]]
## 7
![[NOR NOT.png]]
![[NOR OR.png]]
![[NOR AND.png]]

# 8a
$$+50.4375 = \underbrace{0}_{\text{sign}}\ \underbrace{110010}_{\text{exponent}}\ \underbrace{0.0111}_{\text{mantissa}}$$
$$\underbrace{0}_{\text{sign}}\ \underbrace{00000110010}_{\text{exponent}}\ \underbrace{0.0111}_{\text{mantissa}} = 032.7$$
## 8b
$$0.0 = \underbrace{0}_{\text{sign}}\ \underbrace{0}_{\text{exponent}}\ \underbrace{0}_{\text{mantissa}}$$
$$\underbrace{0}_{\text{sign}}\ \underbrace{0}_{\text{exponent}}\ \underbrace{0}_{\text{mantissa}} = 000$$
## 8c
$$\text{-Infinity} = \underbrace{1}_{\text{sign}}\ \underbrace{11111111}_{\text{exponent}}\ \underbrace{00000000000000000000000}_{\text{mantissa}}$$
$$\underbrace{1}_{\text{sign}}\ \underbrace{11111111}_{\text{exponent}}\ \underbrace{00000000000000000000000}_{\text{mantissa}} = FF800000$$
## 8d
$$1. 0000001 = \underbrace{0}_{\text{sign}}\ \underbrace{1}_{\text{exponent}}\ \underbrace{0}_{\text{mantissa}}$$
$$\underbrace{0}_{\text{sign}}\ \underbrace{1}_{\text{exponent}}\ \underbrace{0}_{\text{mantissa}} = 1.000001AD7F29ABCAF485$$
## 9a
$$0xc349a000 = 11000011010010011010000000000000$$
$$11000011010010011010000000000000 = 3276382208$$
## 9b
$$0xffe00001 = 11111111111000000000000000000001$$
$$11111111111000000000000000000001 = 4292870145$$
## 9c
$$0x80000000 = 10000000000000000000000000000000$$
$$10000000000000000000000000000000 = 2147483648$$
## 9d
$$0x00400000 = 10000000000000000000000$$
$$10000000000000000000000 = 4194304$$
## 10
So that addition and subtract operations could be done and are reversible. For example adding 5 and 2 is $$0101 + 0010 = 0111$$
and subtracting 5 and 2 is $$0101 + 1110 = 0011$$
