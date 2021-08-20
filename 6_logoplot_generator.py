from weblogo import *
from os import listdir
from PIL import Image
from io import BytesIO

for file in listdir("CDR3_MSA"): 			# MS alignment files in directory
    if "fasta" in file: 				# must be fasta format
        seq_file = open("CDR3_MSA/" + file)	
        seqs = read_seq_data(seq_file)		
        logodata = LogoData.from_seqs(seqs)	
        logooptions = LogoOptions()		# All OPTIONS go here as logooptions.
        logooptions.title = str(file)
        logoformat = LogoFormat(logodata, logooptions)
        png = png_print_formatter(logodata, logoformat)	# generates plot from data and format
        byte_file = BytesIO(png)				# plot in bytes therefore conversion
        img = Image.open(byte_file).convert("RGBA")
        file_name = str(file)[:-6] + ".png"
        img.save(file_name)

'''
creator_text – Embedded as comment in figures.
logo_title – Creates title for the sequence logo
logo_label – An optional figure label, added to the top left (e.g. ‘(a)’).
unit_name – See std_units for options. (Default ‘bits’)
yaxis_label – Defaults to unit_name
xaxis_label – Add a label to the x-axis, or hide x-axis altogether.
fineprint – Defaults to WebLogo name and version
show_yaxis – Display entropy scale along y-axis (default: True)
show_xaxis – Display sequence numbers along x-axis (default: True)
show_ends – Display label at the ends of the sequence (default: False)
show_fineprint – Toggle display of the WebLogo version information in the lower right corner. Optional, but we appreciate the acknowledgment.
show_errorbars – Draw errorbars (default: False)
show_boxes – Draw boxes around stack characters (default: True)
debug – Draw extra graphics debugging information.
rotate_numbers – Draw xaxis numbers with vertical orientation?
scale_width – boolean, scale width of characters proportional to ungaps
pad_right – Make a single line logo the same width as multiline logos (default: False)
stacks_per_line – Maximum number of logo stacks per logo line. (Default: 40)
yaxis_tic_interval – Distance between ticmarks on y-axis(default: 1.0)
yaxis_minor_tic_ratio – Distance between minor tic ratio
yaxis_scale – Sets height of the y-axis in designated units
xaxis_tic_interval – Distance between ticmarks on x-axis(default: 1.0)
number_interval – Distance between ticmarks (default: 1.0)
shrink_fraction – Proportional shrinkage of characters if show_boxes is true.
errorbar_fraction – Sets error bars display proportion
errorbar_width_fraction – Sets error bars display
errorbar_gray – Sets error bars’ gray scale percentage (default .75)
resolution – Dots per inch (default: 96). Used for bitmapped output formats
default_color – Symbol color if not otherwise specified
color_scheme – A custom color scheme can be specified using CSS2 (Cascading Style Sheet) syntax. E.g. ‘red’, ‘#F00’, ‘#FF0000’, ‘rgb(255, 0, 0)’, ‘rgb(100%, 0%, 0%)’ or ‘hsl(0, 100%, 50%)’ for the color red.
stack_width – Scale the visible stack width by the fraction of symbols in the column (I.e. columns with many gaps of unknowns are narrow.) (Default: yes)
stack_aspect_ratio – Ratio of stack height to width (default: 5)
logo_margin – Default: 2 pts
stroke_width – Default: 0.5 pts
tic_length – Default: 5 pts
stack_margin – Default: 0.5 pts
small_fontsize – Small text font size in points
fontsize – Regular text font size in points
title_fontsize – Title text font size in points
number_fontsize – Font size for axis-numbers, in points.
text_font – Select font for labels
logo_font – Select font for Logo
title_font – Select font for Logo’s title
first_index – Index of first position in sequence data
logo_start – Lower bound of sequence to display
logo_end – Upper bound of sequence to display
'''