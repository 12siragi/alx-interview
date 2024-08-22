Approach:
Factorization Insight: The key observation is that the minimum number of operations required corresponds to the sum of the factors of n.

If n is prime, the only way to reach n 'H' characters is by performing n paste operations after a single copy.
If n is composite, we can break it down into smaller steps by using its factors.
Algorithm:

Start by initializing the number of operations to 0.
For each integer i starting from 2, repeatedly divide n by i until n is no longer divisible by i.
Add i to the operation count for each division, as each division represents a series of paste operations after a copy.
