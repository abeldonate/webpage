+++
title = "Maths in daily life"
date = 2026-05-05
draft = false

[taxonomies]
categories = ["philosophy"]
+++

This post stems from the frustration of not being able to give some examples in a pub conversation when I was asked the question "but do you use maths in your daily life?".

I remember trying to think about some enlightening examples, but I wasn't as fast as I wished. This post is about those examples (a little bit late, though!).


### Law of big numbers
Estimating things might seem boring at first, but sometimes it turns out to be really useful. I am a little bit obsessed with logistics, so whenever I see a delivery truck entering the narrow streets of the old town full of restaurants and pubs, I wonder how much food it is carrying and how packed it is.

Imagine you're interested in knowing how many menus a restaurant has cooked, or how many beers a pub has sold on a single day. Of course you can take an educated guess performing a few computations, and I sometimes do so when I am on my own. However, it turns out that if you ask some people and average the result, the outcome will be surprisingly accurate. 

This phenomenon is known as the _law of big numbers_, and it is based on the fact that some people will tend to underestimate while some others will tend to overestimate, thus cancelling the errors out.

### Central limit theorem

The central limit theorem is, in my opinion, one of the most surprising results in all of statistics. In rough terms, it states that if you add up a large number of independent random contributions, the result will tend to follow a normal distribution — the familiar bell curve — regardless of the shape of the individual contributions.

Think about something as simple as the total time it takes you to get ready in the morning. Showering, making coffee, looking for your keys: each of these tasks has its own random duration. Yet their sum, your total preparation time, will trace out a bell curve shape across many days. This is why heights, measurement errors, and exam scores all tend to follow a normal distribution.

Perhaps the most striking consequence is that the bell curve appears even when the individual contributions are very far from normal. Roll a die many times and add up the results: each roll is perfectly uniform, yet the sum quickly starts to resemble a normal distribution. This universality is what makes the central limit theorem one of the cornerstones of statistics — no matter how messy the individual pieces are, the aggregate is eventually well-behaved.

### Benford's law
I am passionate about geography. I usually enjoy knowing (and estimating beforehand) the population of each city or country that I visit, or that I just talk about. But something fascinating happens when we focus our attention on the most significant digit of that number. I really encourage you to try this experiment: think about 10 cities and look up their population. Then write down just the first digit of each. 

It turns out that if you repeat this enough times, the most common digit will be 1, followed by 2, and so on up to 9. This is called Benford's law, and this logarithmic behaviour is observed in every real-world dataset. The exact distribution that one gets is 

(complete)

One of the most widely used applications of this phenomenon is in detecting tax fraud. Company invoices are regularly checked to see whether they follow Benford's law or, on the contrary, someone has been fabricating the figures.

### Choosing a mus partner
Mus is a pretty popular Spanish card game (more info here), especially among the collective of unemployed Bonn students (more info here). Every semester we organise a tournament to decide who will hold the honour of being the king of mus. However, choosing a partner is always difficult, especially in your first semester. There are many people to choose from, so you decide on a strategy: you will play each day during the training sessions in the canteen with a different person, and at the end of each match you will decide whether you want to partner with them or not. How do you know when the right time to commit to a partner is?

At first this seems like a tough question. There is a trade-off between choosing too quickly — missing potentially better partners who come later — and waiting too long, rejecting good partners in the hope that something better will come. However, maths comes to the rescue, telling you that you must systematically reject the first $N/e$ players, and then partner with the next one who is better than all of those first $N/e$ players[^1].

(Formulas and computation)



### Expected value at the railways

Near where I live there is a level crossing: a point where the road meets the railway tracks. The barrier comes down when a train is approaching, blocking the way for a few minutes. There is also an underpass not far away — a longer route, but always open. So whenever I arrive and find the barrier down, I face a small but genuine dilemma: should I wait for it to lift, or take the longer path?

This is a question of expected value — the average outcome you would get if you faced this situation many times. The longer path costs a fixed extra time, say $D$ minutes compared to the direct route. Waiting costs however long the barrier remains down from that moment — a random quantity. The rational choice is whichever of the two is smaller on average.

If we call $T$ the average duration of a closure, then, assuming a uniform distribution, arriving at a closed barrier means we can expect to wait $T/2$ minutes until it opens. Thus, if $T/2 < D$, the sensible decision is to wait; otherwise, take the underpass.

But how do we know $T$ in practice? We can simply gather data. For the first few days we always wait and note down how long the barrier was closed each time. After a while we have enough observations to compute a reliable average, which estimates $T/2$.


### Balancing a table
You're having dinner with some friends in a living room, but something is clearly bothering you. There's something about the table that is off... It's the balance: only three of the four legs are in contact with the ground.

It turns out that this can be fixed with a simple rotation. In fact, if you start rotating the table (say, clockwise), you will find a point where it is balanced before reaching the $180^\circ$ rotation. This fact that may seem surprising at first, relies on a very simple (but powerful) result in analysis, i.e. Bolzano's theorem, which states that if a continuous function goes from positive to negative, then there is some point in the middle which is zero. Let's see it in action:

Fix three legs of the table touching the ground, and consider the distance of the fourth one from the ground (as a positive value). We can then treat that distance, say $d(\alpha)$, as a function of the angle $\alpha$ through which we rotate the table. As we rotate, this distance changes continuously (under the assumption that the floor is smooth). This is the point where we need the kind of abstraction mathematicians love: allowing negative values for the distance $d(\alpha)$. If we perform a $180^\circ$ rotation with the same three legs always touching the ground, we end up in a symmetric position where $d(180) = -d(0)$ — the same distance from the fourth leg to the ground, but with the opposite sign. And now here's the magic: we can apply Bolzano's theorem to show that there is an angle $\beta$ in between where $d(\beta) = 0$, meaning the table is balanced.

If we think about it, the abstraction of allowing negative values does not make any sense in the physical world, but it is just a mathematical idea for using powerful tools. Could we have proved the same result without that abstraction? Yes, of course. Would it have been more difficult and less clean? Absolutely.

### Eating a pizza slice
Depending on the consistency of the dough and the amount of tomato, eating a pizza slice is sometimes rather cumbersome. Without noticing, we often tend to fold the slice slightly and eat it that way. The surprising fact is that there is a beautiful mathematical concept at work here: the Theorema Egregium. Broadly speaking, this theorem tells you that, whenever we have two directions of curvature, their product is invariant under bending.

In this case, it is clear that the curvature of the pizza slice when it is flat is zero, since it has no curvature on any direction. When we fold it, though, it acquires a non-zero curvature in one direction. But that forces the other direction to have zero curvature, so that the product of curvatures remains zero. Thus, mathematics tells us that, (in a perfect world), if you slightly bend the slice, then it will be flat in the other direction.

This is, perhaps, one of the most common examples, yet quite representative of the mathematics hiding in our daily life, and of how we act in certain ways without ever noticing that there is a deep reason behind it.

### Compound interest
Mindfulness is not for everyone, and it might not be for me either. However, I have recently been reading some books about improving myself in many aspects: how to learn better and faster, how to ignite curiosity and interest, and how to be a better person each day. One of the most well-known examples is the $1\%$ rule. It says that if you try to be $1\%$ better than the day before (whatever that means), then within one year you will be $38$ times better than you are right now.

This fact is based on compound interest, the same principle applied to funds with a fixed interest rate. The maths are simple: instead of adding $1\%$ linearly each day, you apply it to the quantity you already have. So you must multiply $365$ times by $1.01$. This gives
$$
 1.01^{365} \times \text{current} = 37.8 \times \text{current}
$$

[^1]: Popular explanations of this result use dating strategies instead, but let's not talk about that.