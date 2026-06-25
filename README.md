# Extracting information from bar plots

## Requirements
For running the code - Python 3.
Libraries used in the scripts that need to be installed: 
- opencv-python
- easyocr
- XlsxWriter
- matplotlib
- numpy
  
The following libraries are only used in the script graph_statistics.py
- pandas
- dtw-python (only used in the script graph_statistics.py)

## Usage 
Run the extract_data.py script from inside the scripts directory. Example:

C:\..\some directories\..\bar_plot_extraction\scripts> python extract_data.py

## Contents
- scripts/
 - extract_data.py - extracts data from the bar plot image in img/. Saves the result to results/FigureData1.xlsx
 - graph_statistics.py - shows various information and plots that compare the extracted data to the actual data
- data/
  - virus-data-report.ods - the Microsoft Excel spreadsheet that contains the actual data, that the bar plot in img/ uses
- img/
  - figure1_no_line.png - bar plot, the image that the script runs on
- results/
  - FigureData1.xlsx - stores the result of the extract_data.py script
- statistics_figures/ - contains images of plots, produced by graph_statistics.py
  - dtw.png
  - residual.png
- .gitignore
- README.md

## Additional information
The script is only used on one image, and it needs to be in the img directory.
To use with a different image, you need to replace the current one.
If the new image has a different name:
In the beginning of the extract_data.py script, change the variable img_path to your desired image name
 
