nucleotides = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    try:
        return "".join([nucleotides[v] for v in dna_strand])
    except Exception as e:
        raise ValueError("You must use a valid Nucleotides")