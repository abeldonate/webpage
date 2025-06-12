+++
title = "On the efficiency of the Grid of Barcelona (Eixample)"
date = 2025-06-10
draft = true
[taxonomies]
categories = ["software"]
tags = ["programming"]
+++

The idea behind this post began a random day talking with a friend while we were walking in [Barcelona Eixample](https://en.wikipedia.org/wiki/Eixample) (_Eixample_ in Catalan, _Ensanche_ in Spanish). Such grid has chamfered corners, which leads us to cover:
- More path if we are traveling on straight line
- Less path if we are traveling diagonally and we choose wisely

Thus, since my professional formation on mathematics included a course on statistics that I vaguely remember, I wanted to test my own limits trying to figure out if this chamfered design actually improves the traveled distance on the grid. (Also, I have finished my undergrad studies, it is summer and I am desperated to lose my worthless free time on shitty projects).

The grid will have 3 distinct paramenters, whose names are introduced here:
- $l_0$ is the side length of the square blocks
- $l$ is the side length of the blocks after the chamfer
- $d$ is the length of the chamfer

---

# The most efficient path in the grid

First, we will perform the following reduction. We can think of an intersection of the grid just merging the streets, since the crossroads and lanes can be skipped for our purpose. Thus, the grid can be transformed as

{{ img(path="@/projects/barcelona-grid/figures/crossings.png", class="bordered", alt="", caption="Transformation of the grid") }}

Obviously, on a regular grid, for going from point $(a_1, b_1)$ to point $(a_2, b_2)$, there are plenty of efficient paths, all of them zigzaging within the rectangle defined by the points. However, on a grid with chamfers, this set is reduced. Basically, one can take profit of the chamfers and _diagonalize_.

{{ img(path="@/projects/barcelona-grid/figures/twopaths.png", class="bordered", alt="", caption="Manhattan and chamfered walks") }}

where the path in red represents the _manhattan_ distance and the path in blue represents the _chamfered_ distance.

Thus, given $(a,b)$, whith $b \ge a$ the moved blocks horizontally and vertically, the efficient discances in both cases are:
$$
    d_m = (a+b)l_0  \quad \text{and}  \quad
    d_c = (a+b)l + 2(b-1)d + (l_0-l) \approx (a+b)l + 2bd
$$
where $d_m$ is the distance in the perfect grid and $d_c$ is the distance in the chamfered grid. 

From now on, we propose two ways of solving the problem, first analytically, and then numerically via a simulation.

---

# Analytic approach

This method will assume a grid sufficiently large. Then, we can pass to the limit and make a continuous analysis for simplicity.

The function to study is the ratio of the distances $d_c$ and $d_m$
$$
  f(a,b) = \frac{d_c}{d_m} = \frac{(a+b)l+2bd}{(a+b)l_0}
$$

If this function is less than 1, then the chamfered grid is more efficient than the perfect one. However, this function heavily depens on $(a,b)$. More specificaly, it does depend on the ratio $frac(a,b)$.

$$
  f(r = \frac{a}{b}) = \frac{(a+b)l + 2 b }{(a+b)l_0} = 
  \frac{l}{l_0} + \frac{2d}{(1+r)l_0} =  \frac{l}{l_0} + \frac{\sqrt{2}}{ 1+r} \left(1- \frac{l}{l_0}\right)
$$

As we have seen, the function $f(r)$ depends on the ratio $r = \frac{a}{b}$. Thus, we compute for which values of $r$ this fuction is less than 1.

$$
  f(r) < 1 \quad \Rightarrow \quad \frac{\sqrt{2}}{1+r} \left(1-\frac{l}{l_0}\right) < 1 - \frac{l}{l_0} \quad \Rightarrow\quad r + 1 > \sqrt{2} \quad \Rightarrow \quad r > \sqrt{2}-1
$$

Surprisingly, this is independent of the chamfer length $d$.

Since the ratio $\frac{d_c}{d_m}$ heavily depends just on the ratio $r = \frac{a}{b}$, we can just study the distribution of this ratio. Thus, one can model it as follows:

(drawing)

Then, notice that given arbitrary points $(x_1, y_1), (x_2, y_2)$, the distance between them is 
$$
  (a, b) = (|x_1 - x_2|, |y_1 - y_2|)
$$
Thus, supposing a uniform distribution of the points
$$
  \textbf{x}_i = U(0,1) \quad \text{and} \quad \textbf{y}_i = U(0,1)
$$
then, the probability distribution of the distance $(a, b) = (|x_1 - x_2|, |y_1 - y_2|)$ given $a \le b$ is
$$
  p((a,b)) = 8(1-a)(1-b)
$$
confined withing the region

(drawing)

## Density of cases in which chamfer is efficient

Thus, for computing the probability distribution of the ratio $r = frac(a,b)$ we perform the following change of variables:
$$
  r = \frac{a}{b}, \quad b = b, \quad J = \frac{\partial(a,b)}{\partial(r,b)} = "continue" = b
$$

and the pdf of $r$ is then
$$
  p(r) = \int_0^1 8 (1-r b) (1-b) b d b = \frac{4}{3} - \frac{2}{3} r
$$
Thus, if we consider only the region $r > \sqrt(2)-1$, we can compute the probability of having a ratio $r$ larger than this value:
$$
p(r > \sqrt{2} - 1) = \int_{\sqrt{2}-1}^{1} \left( \frac{4}{3} - \frac{2}{3} r \right) \, dr = \frac{10}{3} - 2\sqrt{2} \approx 0.505
$$

meaning, finally, that the chamfered grid is slightly more efficient, statistically speaking, than the perfect one.

---

## Expected value

We compute the expected values of the distances $(a, b)$ given the known probability distribution:

$$
\langle d_m \rangle = \int_{0}^{1} \int_{0}^{b} 8 (1 - a)(1 - b)(a + b) l_0 da db = \frac{2}{3} l_0
$$

and

$$
\langle d_c \rangle = \int_{0}^{1} \int_{0}^{b} 8 (1 - a)(1 - b)\left( (a + b) l + 2 b d \right)  da  db = \frac{2}{3} l + \frac{14}{15} d = \frac{2}{3} l + \frac{7 \sqrt{2}}{15} (l_0 - l)
$$

Considering the ratio between the two expected values, we have:

$$
\frac{d_c}{d_m} = \frac{7 \sqrt{2}}{10} + \left(1 - \frac{7 \sqrt{2}}{10} \right) \frac{l}{l_0} \approx 0.98995 + (1-0.98995)\frac{l}{l_0}
$$

Plotting this function, we realize that—as one would expect—the expected value of the chamfered grid is slightly smaller than the perfect one. But this value now depends on the ratio $\frac{l}{l_0}$. The more chamfered the grid is, the more efficient it is.

*(plot)*

In the previous article \[CITE], we saw that the ratio of the chamfer is \[CITE].

---


# Numerical approach

For the numerical approach we consider a big grid and we randomize the choice of starting and ending points. Notice here we have more flexibility, since we don't have to deal with complicated analytical expressions on distribution functions.

We start defining the size of the grid and the number of random samples

    import numpy as np
    import matplotlib.pyplot as plt

    N = 1000000 # Size of the grid
    M = 1000000 # Number of random samples

Now we construct the functions that transform the random points into the manhattan and chamfered distance:

    def to_abcoord(p1, p2):
        return (abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

    def dist_manhattan(a,b):
        return a+b

    def dist_eixample(a,b,l):
        d = np.sqrt(2)/2 * (1-l)
        if a == 0 and b == 0:
            return 0
        if a == b:
            return l*(a+b) + d*(2*a-1) + (1-l)
        if a < b:
            return l*(a+b) + 2*d*(a) + 2*d*(b-a-1) + (1-l)
        return dist_eixample(b,a, l)

Once the management of the distances is done, we iterate over different values of the grid parameter $l$, making $M$ simulations for each case. We store the results on an array and plot them for visual clarity.

    def eixample():
        stats = []
        for j in range(10):
            l = 0.6 + j * 0.04

            samples = []
            for i in range(M):
                p1 = np.random.randint(0, N, size=2)
                p2 = np.random.randint(0, N, size=2)
                a, b = to_abcoord(p1, p2)
                d_m = dist_manhattan(a, b)
                d_e = dist_eixample(a, b,l)
                samples.append((d_m, d_e, d_e < d_m))
    
            good_cases = sum(s[2] for s in samples)
            expected_m = sum(s[0] for s in samples) / M
            expected_e = sum(s[1] for s in samples) / M
            stats.append((l, good_cases/M, (M-good_cases)/M, expected_e/(expected_m))) 

        # Plotting the results
        # First plot: Good vs Bad cases
        plt.figure(figsize=(10, 6))
        plt.plot([s[0] for s in stats], [s[1] for s in stats], label='Good cases', marker='o')
        plt.plot([s[0] for s in stats], [s[2] for s in stats], label='Bad cases', marker='x')
        # Theoretical value
        plt.axhline(y=0.505, color='r', linestyle='--', label='Theoretical 0.505')
        plt.xlabel('l (Grid parameter)')
        plt.ylabel('Number of cases')
        plt.title('Grid Distance Efficient vs Unefficient Cases')
        plt.legend()
        plt.grid()

        # Second plot: Expected distances ratio
        plt.figure(figsize=(10, 6))
        plt.plot([s[0] for s in stats], [s[3] for s in stats], label='Expected Manhattan / Eixample', marker='o')
        # Theoretical line
        x_vals = np.array([s[0] for s in stats])
        plt.plot(x_vals, 7*np.sqrt(2)/10 + (1-7*np.sqrt(2)/10) * x_vals, 'g--', label='y = Theoretical line')
        # Actual value l of Barcelona Grid
        plt.axvline(x=0.735, color='b', linestyle='--', label='x = 0.735')  # <-- Add this line
        plt.xlabel('l (Grid parameter)')
        plt.ylabel('Expected Grid / Manhattan Distance Ratio')
        plt.title('Expected Distances Ratio for Grid')
        plt.legend()
        plt.grid()
        plt.show()

    eixample()

Two plots are generated by the code:
- The first one shows the slight advantage in using the chamfered grid
- The second one shows how the expected value of the ratio changes linearly depending on the grid parameter $l$

{{ img(path="@/projects/barcelona-grid/figures/plotefficient.png", class="bordered", alt="", caption="Advantage of chamfered grid") }}

{{ img(path="@/projects/barcelona-grid/figures/plotl.png", class="bordered", alt="", caption="Expected value of ratio") }}


---
---
---
---




Here’s a polished version of your text, preserving your tone and technical detail while improving flow, grammar, and clarity:

---

The idea for this post began on a random day, during a walk with a friend through [Barcelona’s Eixample](https://en.wikipedia.org/wiki/Eixample) district (*Eixample* in Catalan, *Ensanche* in Spanish). This iconic grid layout features chamfered corners, which raises an interesting geometric question:

* We walk a longer distance if traveling along a straight line.
* We walk a shorter distance if moving diagonally—provided we choose our path wisely.

Since my academic background in mathematics included a statistics course I now only vaguely recall, I decided to challenge myself: does this chamfered design *actually* reduce the average distance traveled across the grid?

(Also, I’ve just finished my undergraduate studies, it's summer, and I’m desperate to waste my free time on pointless side projects.)

The grid model will be characterized by three parameters:

* $l_0$: the side length of the original square blocks,
* $l$: the side length after the chamfer is applied,
* $d$: the chamfer length.

---

# The Most Efficient Path in the Grid

Let’s simplify the problem. At intersections, we can conceptually merge the streets—the exact layout of crossroads and lanes doesn't affect our analysis. So, the grid can be abstracted as follows:

{{ img(path="@/projects/barcelona-grid/figures/crossings.png", class="bordered", alt="", caption="Transformation of the grid") }}

On a regular grid, to go from point $(a_1, b_1)$ to $(a_2, b_2)$, many shortest paths exist, all zigzagging within the rectangle defined by those two points. However, with chamfers, this set of efficient paths narrows. The chamfers allow for a more diagonal-like movement—a sort of "diagonalization."

{{ img(path="@/projects/barcelona-grid/figures/twopaths.png", class="bordered", alt="", caption="Manhattan and chamfered walks") }}

In the figure above, the red path shows the standard Manhattan distance, while the blue path leverages the chamfered corners.

Given a displacement of $(a, b)$, where $b \ge a$, the corresponding distances are:

$$
d_m = (a + b) l_0 \quad \text{(Manhattan)} \\
d_c = (a + b) l + 2(b - 1)d + (l_0 - l) \approx (a + b) l + 2 b d
$$

From here, we’ll explore two ways to analyze the efficiency of chamfers: analytically and numerically.

---

# Analytical Approach

Assume the grid is sufficiently large, so we can use a continuous model for simplicity. We analyze the ratio:

$$
f(a, b) = \frac{d_c}{d_m} = \frac{(a + b)l + 2bd}{(a + b)l_0}
$$

If $f(a, b) < 1$, then the chamfered grid is more efficient. Interestingly, this function primarily depends on the ratio $r = \frac{a}{b}$, since:

$$
f(r) = \frac{l}{l_0} + \frac{2d}{(1 + r)l_0}
$$

Assuming $d = \frac{\sqrt{2}}{2}(l_0 - l)$, we substitute and get:

$$
f(r) = \frac{l}{l_0} + \frac{\sqrt{2}}{1 + r} \left(1 - \frac{l}{l_0}\right)
$$

To find when $f(r) < 1$, we solve:

$$
\frac{\sqrt{2}}{1 + r} \left(1 - \frac{l}{l_0} \right) < 1 - \frac{l}{l_0} \Rightarrow r > \sqrt{2} - 1
$$

Remarkably, the threshold ratio is independent of the specific chamfer length $d$.

---

## Distribution of Path Ratios

To quantify how often $r > \sqrt{2} - 1$, consider two points randomly placed in the unit square:

$$
\mathbf{x}_i, \mathbf{y}_i \sim U(0, 1)
$$

The displacement $(a, b) = (|x_1 - x_2|, |y_1 - y_2|)$, assuming $a \le b$, has the probability density:

$$
p(a, b) = 8(1 - a)(1 - b)
$$

We now change variables to analyze the ratio $r = \frac{a}{b}$. Let $b = b$ and $a = r b$, with Jacobian $J = b$. The resulting PDF becomes:

$$
p(r) = \int_0^1 8 (1 - r b)(1 - b) b \, db = \frac{4}{3} - \frac{2}{3} r
$$

Now compute the probability that $r > \sqrt{2} - 1$:

$$
P(r > \sqrt{2} - 1) = \int_{\sqrt{2} - 1}^{1} \left(\frac{4}{3} - \frac{2}{3}r\right) dr = \frac{10}{3} - 2\sqrt{2} \approx 0.505
$$

So, **slightly more than half the time**, a chamfered grid is more efficient.

---

## Expected Value Comparison

Let’s compute the expected distances under this uniform distribution:

For the regular grid:

$$
\langle d_m \rangle = \int_{0}^{1} \int_{0}^{b} 8(1 - a)(1 - b)(a + b)l_0 \, da \, db = \frac{2}{3} l_0
$$

For the chamfered grid:

$$
\langle d_c \rangle = \int_{0}^{1} \int_{0}^{b} 8(1 - a)(1 - b)[(a + b)l + 2bd] \, da \, db = \frac{2}{3}l + \frac{14}{15}d = \frac{2}{3}l + \frac{7\sqrt{2}}{15}(l_0 - l)
$$

Taking the ratio:

$$
\frac{\langle d_c \rangle}{\langle d_m \rangle} = \frac{7\sqrt{2}}{10} + \left(1 - \frac{7\sqrt{2}}{10} \right)\frac{l}{l_0} \approx 0.98995 + (1 - 0.98995)\frac{l}{l_0}
$$

As expected, this ratio decreases as the chamfer becomes more pronounced (i.e., as $l/l_0$ decreases).

*(plot)*

In a previous article \[CITE], we examined the actual chamfer ratio in the Eixample district. \[CITE]

---

# Numerical Approach

To simulate this behavior, we define a large grid and randomly choose pairs of points. Numerical simulations allow more flexibility, avoiding the complexity of analytical probability densities.

First, define grid size and sample count:

```python
N = 1000000  # Grid size
M = 1000000  # Number of samples
```

Define distance functions:

```python
def to_abcoord(p1, p2):
    return abs(p1[0] - p2[0]), abs(p1[1] - p2[1])

def dist_manhattan(a, b):
    return a + b

def dist_eixample(a, b, l):
    d = np.sqrt(2)/2 * (1 - l)
    if a == 0 and b == 0:
        return 0
    if a == b:
        return l*(a + b) + d*(2*a - 1) + (1 - l)
    if a < b:
        return l*(a + b) + 2*d*a + 2*d*(b - a - 1) + (1 - l)
    return dist_eixample(b, a, l)
```

Now run simulations:

```python
def eixample():
    stats = []
    for j in range(10):
        l = 0.6 + j * 0.04
        samples = []
        for _ in range(M):
            p1 = np.random.randint(0, N, size=2)
            p2 = np.random.randint(0, N, size=2)
            a, b = to_abcoord(p1, p2)
            d_m = dist_manhattan(a, b)
            d_e = dist_eixample(a, b, l)
            samples.append((d_m, d_e, d_e < d_m))
        good_cases = sum(s[2] for s in samples)
        expected_m = sum(s[0] for s in samples) / M
        expected_e = sum(s[1] for s in samples) / M
        stats.append((l, good_cases/M, 1 - good_cases/M, expected_e/expected_m))

    # Plotting results
    ...
```

The plots generated confirm our expectations:

* The **first plot** shows how often chamfers provide a shorter route.
* The **second plot** shows that the expected distance improves linearly with increasing chamfer.

{{ img(path="@/projects/barcelona-grid/figures/plotefficient.png", class="bordered", alt="", caption="Advantage of chamfered grid") }}

{{ img(path="@/projects/barcelona-grid/figures/plotl.png", class="bordered", alt="", caption="Expected value of ratio") }}

---

Let me know if you'd like help turning this into a formal blog post with LaTeX formatting, citations, or more refined visuals.


