import sys
import math
from collections import Counter

def entropy(text):
    # Wahrscheinlichkeit der jeweiligen Zeichen
    probabilities = [float(count) / len(text) for count in Counter(text).values()]

    # tatsächliche Entropie
    h_actual = -sum(p * math.log2(p) for p in probabilities)

    # maximale Entropie
    h_max = math.log2(len(set(text)))

    return h_max, h_actual

if __name__ == "__main__":
    # Fehlerbehandlung
    if len(sys.argv) < 2:
        print("\nFehler: Kein Text eingegeben. Tool in Konsole mit python entropy.py \"Text\" aufrufen.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("\nFehler: Zu viele Argumente eingegeben. Tool in Konsole mit python entropy.py \"Text\" aufrufen.")
        sys.exit(1)
    
    text = sys.argv[1]

    h_max, h_actual = entropy(text)

    print(f"\nH\u2098\u2090\u2093 = {h_max}")
    print(f"\nH = {h_actual}")