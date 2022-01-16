from collections import Counter
import numpy as np

label = [1, 10, 25, 6, 10, 24, 41, 10, 10]
labels = np.array(label)

# Conta o elemento que mais apareceu


def mais_votado(labels):
    votos = Counter(labels)
    # preciso, agora, apenas do valor, não da quantidade
    vencedor, _ = votos.most_common(1)[0]
    return vencedor


def majority_vote(labels):
    # presume que as etiquetas são ordenadas do mais próximo para o mais distante
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len(
        [count for count in vote_counts.values() if count == winner_count])

    if num_winners == 1:
        return winner  # vencedor único, então o devolve
    else:
        return majority_vote(labels[:-1])  # Fazemos de novo, sem o último
