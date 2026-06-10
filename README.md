# Linear_Congruential_Generator_PRNG
A Linear Congruential Generator (LCG) is one of the oldest and best-known pseudorandom number generator (PRNG) algorithms. It relies on a linear recursive state equation:

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

The system utilizes a constant multiplier ($a$), a constant increment ($c$), and a constant modulus ($m$) which strictly conform to the Hull-Dobell Theorem to guarantee a full period. The hardcoded parameters for this implementation are:

Modulus ($m$): $65536$

Multiplier ($a$): $137$

Increment ($c$): $13$
