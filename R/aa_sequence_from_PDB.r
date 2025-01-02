# In a CSV of missense variant sequencing data, the protein position is extracted for ABO variants and arranged by 
# log10P and beta scores. The most significant protein position is extracted and the PDB IDs are fetched from Uniprot.
# Position counts are obtained from Uniprot to find the position with the highest number of counts across all PDB IDs.

library(dplyr)
library(protti)
library(bio3d)

# read in the fie containg sequencing data and extract "protein position"
missense_variants <- read.table("missense_variants.txt")
protein_positions <- missense_variants$protein_position

# Column named "Prot_pheno" is filtered to only include ABO variants and arranged by log10P and BETA scores in other columns
abo_variants <- missense_variants %>% filter(Prot_pheno == "ABO")
abo_positions <- unique(abo_variants$protein_position)
sig_abo_variant <- abo_variants %>% arrange(desc(LOG10P + abs(BETA))) %>% slice(1)
sig_abo_variants <- abo_variants %>% arrange(desc(LOG10P + abs(BETA)))
protein_position <- sig_abo_variant$protein_position

# fetch data from Uniprot for ABO gene, id = P16442 and create a list of all PDB IDs
structure_data <- fetch_uniprot(uniprot_id = "P16442")
pdb_ids <- structure_data$xref_pdb
pdb_ids <- unlist(strsplit(structure_data$xref_pdb, ";"))
#for (i in seq_along(structure_data$xref_pdb)) {
#     # Split the pdb_id string into individual IDs
#     pdb_ids <- unlist(strsplit(structure_data$xref_pdb[i], ";"))
# }

# Extract protein positions from PDB IDs and count how many times each position occurs across all PDB IDs
pdb_structures <- fetch_pdb_structure(pdb_ids)
position_counts <- sapply(pdb_structures, function(structure) {
     sum(structure$auth_seq_id == protein_position)
 })

# Get the amino acid sequence from structure data in PDB IDs
get_amino_acid_sequence <- function(structure) {
  sequence <- structure %>% filter(label_comp_id != "HOH") %>% select(label_seq_id, label_comp_id) %>% unique()
  sequence <- sequence[order(sequence$label_seq_id), ]
  return(paste(sequence$label_comp_id, collapse = ""))
}
structure <- pdb_structures[[pdb_id]]
amino_acid_sequence <- get_amino_acid_sequence(structure)
cat("Amino acid sequence for PDB ID", pdb_id, ":\n", amino_acid_sequence, "\n")

