+++
title = "Maths in daily life"
date = 2026-05-05
draft = false

[taxonomies]
categories = ["philosophy"]
+++

This post stems from the frustration of not being able to give some examples on a pub conversation when I was asked the question "but do you use math on your daily life?".

I remember trying to think about some enlightening examples, but I wasn't as fast as I wish. 


Bullet points sketch:
- Pizza and gauss curvature
- Rejection of the first n/e (37%) candidates
- Benford's law
- Balancing the chair by rotating it (application of bolzano)
- Expected value at the railways. Know if I should wait or go underneath
- Law of big numbers (average)
- Central limit theorem

## Some statistics

### Law of big numbers
Estimating things might seem boring at first, but sometimes it turns out to be really useful. I am a little bit obsessed with logistics, so whenever I see a delivery truck entering the narrow streets of the old town full of restaurants and pubs, I wonder how much food and how packed is it. 

Imagine you're interested in knowing how many menus has a restaurant cooked, or how many beers has a pub sold on a single day. Of course you can take an educated guess performing a few computations, and I sometimes do so when I am on my own. However, it turns out that if you ask some people and average the result, the outcome will be surprisingly accurate. 

This phenomenon is known as the _law of big numbers_, and it is based on the fact that some people will tend to underestimate, whether some other will tend to overestimate, thus, cancelling the errors out.

### Central limit theorem



### Benford's law
I am passionate about geography. I usually enjoy knowing (and estimating beforehand) the population of each city / country that I visit, or that I just talk about. But something fascinating happens when we just focus our attention on the most significant digit of that number. I really encourage you to make this experiment: think about 10 cities and look for their population. Then write down just each first digit. 

It turns out that if you repeat this enough, the most common digit will be the 1, followed by the 2, and so on until 9. This is call as Benford's law, and this logarithmic behavior is observed on each real world dataset. The exact distribution that one gets is 

(complete)

One of the most widely use application of this phenomenon is on detecting tax fraud. Bills of companies are regularly checked if they follow Benford's law or, on the other hand, someone is making up the bills.

### Choosing mus partner
Mus is a pretty popular Spanish card game (more info (here)), especially among the collective of unemployed Bonn students (more info here). Every semester we organize a tournament for deciding who will held the honors of being the king of mus. However, choosing a partner is always difficult, especially on your first semester. There is many people that you decide to take a strategy: you will play each day during the training sessions in the canteen with a different person, and at the end of each match you will decide if you want to partner with them or not. How do you know which is the right time to partner someone?

At first this seems like a tough question. There is a compromise between being wrong in choosing really quick and leaving potentially good partners that would have come later and being wrong in choosing really late and rejecting good partners hoping that something better would have come. However, maths come to rescue, telling you that you must systematically reject the first N/e players, and then partner with the following one that is better than all of the first N/e players.

(Formulas and computation)

(foot note dates. Popular explanations of this fact use dating strategies instead, but let's not talk about that)

## Geometry

### Balancing a table
You're having dinner with some friends at a living room, but something is clearly bothering you. There's something about the table that is off... It's the balance, only three of the four legs are in contact with the ground.

Turns out that this can be solved just with a simple rotation. In fact, if you start rotating the table (say, clockwise), you will find a point where it is balance before reaching the $180^\circ$ rotation. This fact that may seem surprising at first, relies on a very simple (but powerful) result in analysis, i.e. Bolzano's theorem, which states that if a continuous function goes from positive to negative, then there is some point in the middle which is zero. Let's see it in action:

Fix three legs of the table touching the ground, and consider the distance of the other one to the ground (as a positive value). Then, we can consider that distance, say $d(\alpha)$ as a function of the angle $\alpha$ we are rotating the table. As we rotate this distance changes continuously (under the assumption that the floor is smooth). This is the point where we need the type of abstraction mathematicians love to do when dealing with problems, allowing, in this case, negative values for the distance $d(\alpha)$. If we perform a $180 ^\circ$ rotation with the three same legs always touching the ground, we will end up with a symmetric position, where $d(180) = -d(0)$ we have the same distance from the fourth leg to the ground, but with different sign. An now here's the magic: we can apply Bolzano's theorem, and show that there is an angle $\beta$ in the middle where $d(\beta) = 0$ where the table is balanced.

If we think about it, the abstraction of allowing negative values does not make any sense in the physical world, but it is just a mathematical idea for using powerful tools. Could we have proved the same result without that abstraction? Yes, of course. Would it have been more difficult and less clean? Absolutely.

### Eating a pizza slice
Depending on the consistency of the dough and quantity of tomato, eating a pizza slice is sometimes rather cumbersome. Without noticing, we often tend to slightly fold the slice and eat it that way. The surprising fact is that there is a beautiful mathematical concept what we are using here: the Egregium theorem. Very simplificated, this theorem is telling you that, whenever we have two directions of curvature, then the product is invariant under a certain transformation.

In this case, it is clear that the curvature of the pizza slice when it is flat is zero, since it has no curvature on any direction. When we fold it, though, it acquires a non-zero curvature in one direction. But that is forcing that the other direction should have zero curvature, for achieving the product of curvatures equal to zero. Thus, mathematics are telling us that, (in a perfect world), if you slightly bend the slice, then it will be flat in the other direction.

This is, perhaps, one of the most common examples, yet representative on the math hiding in our daily life, and how we act in certain ways without even noticing that there is a deep reason behind.