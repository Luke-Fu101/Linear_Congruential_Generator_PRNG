# Linear Congruential Generator (LCG) Key Stream PRNG

A Linear Congruential Generator (LCG) is one of the oldest and best-known pseudorandom number generator (PRNG) algorithms. It relies on a linear recursive state equation:

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

The system utilizes a constant multiplier ($a$), a constant increment ($c$), and a constant modulus ($m$) which strictly conform to the Hull-Dobell Theorem to guarantee a full period for the generator's internal state space. 

To eliminate structural patterns and low-order bit degradation common in power-of-two LCGs, this implementation isolates the highest-order bit (Bit 31) using bitwise right-shifting rather than taking the standard least significant bit.

The following LCG function has a period length of 4,294,967,296 steps.

The hardcoded parameters for this 32-bit implementation are:
* **Modulus ($m$):** $4294967296$ ($2^{32}$)
* **Multiplier ($a$):** $1664525$
* **Increment ($c$):** $1013904223$

## Project Purpose
The purpose of this project is to generate a secure, pseudo-random bitstream of variable length to act as a key for symmetric encryption. By utilizing an entropy-seeded LCG, this tool produces balanced, chaotic binary sequences tailored for use in a stream cipher.
