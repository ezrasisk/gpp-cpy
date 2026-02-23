the gpp-cpu is modeled as a complex manifold M, a toric calabi-yau thifold realized physically as the octilayer S(i_3)N_4 stack with 33.6 million gng(s). 
the state of the machine at any moment is a global section of the structure sheaf where the state S is an element of the zeroth cohomology, H(^0)(M, O).
the zeroth cohomology is the space of coherent light amplitudes across all modes and layers, C(^(2048^3)*8). higher cohomology vanishes to guarantee local operations extend
globally without obstruction, giving a coherent and stable system.

booting begins with the trivial lambda injection at 1530nm, E_boot = A(_0)exp(i(K_0)z)exp(-((t^2)/(2(sigma^2)))), with phi_0 = zero.
this trivial section, s_0, equals one as an element of H(^0)(M, O(1)), which is the coherent reference field that anchors all subsequent phases. after one propagation U(t) or
after one 213ps wavefront, the manifold is in the state s = s_0, with norm preserved and phase locked to zero.

subsequent computation is performed by overlaying new pulses from the vcel array: E_op = the sum from i=1 to 2048 of a(_i)exp(i(phi(_i)+k(_0)lambda(_i)z)), where a_i is amplitude or
data value, phi_i is phase or sign or complex component and lambda_i is the wavelength or opcode plus channel. the total field at any point is the coherent superposition with the 
reference E_total = s_0 + E_op.

all computation is expressed as holomorphic morphisms acting on sheaf sections, the routing morphism (awg + mirrors), the propagation morphism (wavefront evolution), the
kerr nonlinearity morphism (the gate operator), the interference operator (bilinear map no sections).

inside a single gng, the computation is as parabolic mirror focuses E_1 & E_2 to the cavity, the cavity amplifies intensity by Q [ I_cav = (Q|E(_in)|(^2))/(omega(_0)V_mode), the
optical kerr effect applies phase shift and then recombination at output mzi/tir prism routes based on deltaPhi, deltaphi less than pi/2 -> constructive (bar port) and
deltaphi greater than pi/2 -> destructive (cross port). for nand gate this becomes: nand(A,B) = 1-theta(|A+B|(^2)-I(_th)*exp(i*pi*theta(|AB|(^2)-I_th))

the overall operation for a task is the composition of morphisms on the sheaf: s_out = U(t)comp(mu)comp(phi(_lambda)(s(_0)+E(_op))) while s_0 provides the coherent reference or phase anchor, E_op
carries data dn opcode, the geometry of the gng array applies the morphisms in parallel across all 33.6 million cells. the final intensity pattern at the pd array or pram is the encoding
of the result.
