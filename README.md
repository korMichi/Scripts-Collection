# Collection of Scripts

1) **1_rename_sequences.py**  -> renames files to names found in an excel file
2) **2_files_puller.py** -> extracts all files from subdirectories
3) **3_file_extractor.py** -> extracts files from a named excel list
4) **4_trimmed_sequences.py** -> using crowelabs pipeline to extract trimmed sequences from IGBlast
5) **5_text_extraction.py** -> extracts patterns from overall text
6) **6_logoplot_generator.py** -> generates logoplots using multiple sequence alignment
7) **7_hydrophobicity_and_polarity.py** -> calculates hydrophobicity or/and polarity of amino acid sequence
8) **8_translation_in_excel.py** -> translates dna into protein sequence from excel file
9) **9_levensthein_distances.py** -> calculates levensthein distance from sequence data

## Bash commands 
1) **Tab to FASTA** -> awk '{print ">"$1"\n"$2}' example.txt > example.fasta 
2) **IGBLAST commandline** -> igblastn -germline_db_V *PATH_TO_DATABASE* -germline_db_D *PATH_TO_DATABASE* -germline_db_J *PATH_TO_DATABASE* -auxiliary_data *PATH_TO_AUXILIARY_DATA* -organism human -outfmt 19 --extend_align3end -extend_align5end -query input.fasta > output.txt

## IGBLAST Commands
1) igblastn -germline_db_V ~/Documents/igblast_database/igv_blast -germline_db_D ~/Documents/igblast_database/igd_blast -germline_db_J ~/Documents/igblast_database/igj_blast -auxiliary_data /usr/local/ncbi/igblast/optional_file/human_gl.aux -organism human -extend_align3end -extend_align5end -outfmt 19 -query input.fasta > output.txt
2) python /Users/kormichi/Documents/repositories/B-cell-pipeline-scripts/IgBLASTp_wrapper.py PATH_TO_FASTA_FILE
