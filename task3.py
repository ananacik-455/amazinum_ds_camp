side = ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H']
p_h = [0.1, 0.2, 0.4, 0.8, 0.9]
P_a_H = [0.2] * 5 # P(A{1, 2, 3, 4, 5} | H)
H = sum([m * p for m, p in zip(P_a_H, p_h)])
result = []

for s in side:
    if s == 'H':
        # If coin flip on 'H', we will have: P(A | H) = P(A) * P(H | A) / P(H)
        for i in range(len(p_h)):
          P_a_H[i] *= p_h[i] / H
    else:
        # If coin flip on 'T', we will have: P(A | T) = P(A) * P(T | A)       / P(T)      OR
        #                                    P(A | H) = P(A) * (1 - P(H | A)) / (1 - P(H))
        for i in range(len(p_h)):
            P_a_H[i] *= (1 - p_h[i]) / (1 - H)
    # For better experience I show coin side ('H' or 'T') and new probability of picking every coin (Their sum must be 1)
    # print(f"{s}: {P_a_H}, [{sum(P_a_H)}]")
    H = sum([m * p for m, p in zip(P_a_H, p_h)])
    result.append(round(H, 2))

print(result)




