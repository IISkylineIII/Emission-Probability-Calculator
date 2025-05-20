# Emission-Probability-Calculator

Calculates the probability of an emitted string given a hidden state path and an emission probability matrix in a Hidden Markov Model (HMM).

# Usage
```
def compute_emission_probability(emitted_string, alphabet, hidden_path, states, emission_matrix):
    # Converts emission matrix into a dictionary for easier access
    emission = {}
    for i, state in enumerate(states):
        emission[state] = {}
        for j, symbol in enumerate(alphabet):
            emission[state][symbol] = emission_matrix[i][j]

    # Calculate the emission probability by multiplying corresponding emissions
    probability = 1.0
    for symbol, state in zip(emitted_string, hidden_path):
        probability *= emission[state][symbol]

    return probability

``` 
# Output 
4.05156406075e-38

# Applications
* Calculating emission probabilities in Hidden Markov Models.
* Useful in bioinformatics, speech recognition, and other sequence analysis tasks.

# License
This project is licensed under the MIT License.
