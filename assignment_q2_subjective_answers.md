# ES654-2020 Assignment 2

*Kshitij Gajapure* - *16110055*

------

> Write the answers for the subjective questions here

We have to compute (X<sup>T</sup>X)<sup>-1</sup> X<sup>T</sup>Y

Let X be an *m* x *n* matrix
- Calculating (X<sup>T</sup>X) takes O(m*n<sup>2</sup>) time
- Calculating inverse of (X<sup>T</sup>X) takes n<sup>3</sup> time
- Calculating (X<sup>T</sup>Y) takes O(m*n) time
- Multiplication of (X<sup>T</sup>X)<sup>-1</sup> and (X<sup>T</sup>Y) takes O(n<sup>3</sup>) time
- Hence the overall running time is O(mn<sup>2</sup> + n<sup>3</sup>)
