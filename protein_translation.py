"""
Translate RNA sequences into proteins.

RNA: "AUGUUUUCU" => translates to
Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>
Protein: "Methionine", "Phenylalanine", "Serine"
  NOTE: the STOP codon "UAA" terminates the translation
  and the final methionine is not translated into the
  protein sequence.

"""

codons = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU', 'UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA', 'UAG', 'UGA'],
}


def get_protein_name(name):
    for key, values in codons.items():
        if name in values:
            return key


def proteins(strand):
    split_rna = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    proteins_list = []
    for codon in split_rna:
        protein_name = get_protein_name(codon)
        if protein_name == 'STOP':
            break
        proteins_list.append(protein_name)

    return proteins_list
