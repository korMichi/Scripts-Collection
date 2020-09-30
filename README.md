# Collection of Scripts

1) **rename_sequences.py**  -> renames files to names found in an excel file
2) **files_puller.py** -> extracts all files from subdirectories
3) **file_extractor.py** -> extracts files from a named excel list
4) **trimmed_sequences.py** -> using crowelabs pipeline to extract trimmed sequences from IGBlast

## Bash commands 
1) **Tab to FASTA** -> awk '{print ">"$1"\n"$2}' example.txt > example.fasta 
2) **IGBLAST commandline** -> igblastn -germline_db_V *PATH_TO_DATABASE* -germline_db_D *PATH_TO_DATABASE* -germline_db_J *PATH_TO_DATABASE* -auxiliary_data *PATH_TO_AUXILIARY_DATA* -organism human -outfmt 19  -extend_align5end -query input.fasta > output.txt