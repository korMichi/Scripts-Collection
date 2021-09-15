# Functions to caclculate hydrophobicity (Eisenberg score) and polarity of amino acid sequence

hydrophobicity = {"A": 0.62, "C": 0.29, "D": -0.9, "E": -0.74, "F": 1.19, "G": 0.48, 
                  "H": -0.4, "I": 1.38, "K": -1.5, "L": 1.06, "M": 0.64, "N": -0.78, 
                  "P": 0.12, "Q": -0.85, "R": -2.53, "S": -0.18, "T": -0.05, "V": 1.08, 
                  "W": 0.81, "Y": 0.26}

polarity = {"A": 0, "R": 1, "N": 0, "D": -1, "C": 0, "G": 0, "Q": 0, "E": -1,
            "H": 1, "I": 0, "L": 0, "K": 1, "M": 0, "F": 0, "P": 0, "S": 0,
            "T": 0, "W": 0, "Y": 0, "V": 0}

def hydrophobicity_calculator(sequence):
    ''' Requirements: hydrophobicity dictionary
        Input: protein Sequence as string
        Output: hydrophobicity score
        Function: calculates hydrophobicity score (Eisenberg)
    '''
    hydrophobicity_score = 0
    for aminoAcid in sequence:
        hydrophobicity_score += hydrophobicity[aminoAcid]
    return hydrophobicity_score

def polarity_calculator(sequence):
    ''' Requirements: polarity dictionary
        Input: protein sequence as string
        Output: polarity score
        Function: calculates polarity score
    '''
    polarity_score = 0
    for aminoAcid in sequence:
        polarity_score += polarity[aminoAcid]
    return polarity_score

input_sequence = "ACVDD"
score = hydrophobicity_calculator(input_sequence)
pol_score = polarity_calculator(input_sequence)
print(score, pol_score)