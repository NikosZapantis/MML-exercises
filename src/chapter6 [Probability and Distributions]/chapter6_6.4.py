import sympy as sp

#! Using Baye's theorem [ P(Bag2 | Mango) = (P(Mango | Bag2) * P(Bag2)) / P(Mango) ]
#! Sources: [https://www.investopedia.com/terms/b/bayes-theorem.asp]

#? Probs [bag1 -> 4 mango & 2 apples  /  bag2 -> 4 mango & 4 apples]
P_heads, P_tails = 0.6, 0.4
P_mango_bag1, P_mango_bag2 = 4/6, 4/8

# Calculating with Baye's
P_mango = P_mango_bag1 * P_heads + P_mango_bag2 * P_tails
P_bag2_mango = (P_mango_bag2 * P_tails) / P_mango

# Display results
print("\n~ 6.4 Baye's theorem")
print("P(Mango | Bag1) =", round(P_mango_bag1, 3))
print("P(Mango | Bag2) =", round(P_mango_bag2, 3))
print("P(Mango) =", round(P_mango, 3))
print("P(Bag2 | Mango) =", round(P_bag2_mango, 3))
