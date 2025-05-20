def compute_emission_probability(emitted_string, alphabet, hidden_path, states, emission_matrix):
    emission = {}
    for i, state in enumerate(states):
        emission[state] = {}
        for j, symbol in enumerate(alphabet):
            emission[state][symbol] = emission_matrix[i][j]

    # Calculate the emission probability
    probability = 1.0
    for symbol, state in zip(emitted_string, hidden_path):
        probability *= emission[state][symbol]

    return probability

emitted_string = "yzzxyzzzzzyyzzzyyzxyzxzzyyyzxzxyzxyxzxyxxyxxxzxzxy"
alphabet = ["x", "y", "z"]
hidden_path = "ABBBBBBBAABABABBBBABBABBAABBBBABAABBAABBABAABBAABA"
states = ["A", "B"]
emission_matrix = [
    [0.06, 0.893, 0.047],
    [0.579, 0.25, 0.171]
]

probability = compute_emission_probability(emitted_string, alphabet, hidden_path, states, emission_matrix)
print(f"{probability:.11e}")
