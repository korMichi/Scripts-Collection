# Collection of Scripts

1) **rename_sequences.py**  -> renames files to names found in an excel file
2) **files_puller.py** -> extracts all files from subdirectories
3) **file_extractor.py** -> extracts files from a named excel list
4) **trimmed_sequences.py** -> using crowelabs pipeline to extract trimmed sequences from IGBlast

## Bash commands 
1) **Tab to FASTA** -> awk '{print ">"$1"\n"$2}' example.txt > example.fasta 