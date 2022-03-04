
   
# Takes a file CSV file called "data.csv" and outputs each row as a numbered YAML file.
# Data in the first row of the CSV is assumed to be the column heading.

# Import the python library for parsing CSV files.
import csv

# Open our data file in read-mode.
csvfile = open('nc_quarterly_pricing_.csv', 'r')

# Save a CSV Reader object.
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Get header row and then remove it
data_headings = datareader.__next__()

sortedlist = sorted(datareader, key=lambda row: (row[1], row[2]))
# Open a new file with filename based on index number of our current row.
filename = 'nc_quarterly_pricing.yml'
new_yaml = open(filename, 'w')

# Loop through each row...
for row_index, row in enumerate(sortedlist):

	# Empty string that we will fill with YAML formatted text based on data extracted from our CSV.
	yaml_text = ""

	# Loop through each cell in this row...
	for cell_index, cell in enumerate(row):
		# Compile a line of YAML text from our headings list and the text of the current cell, followed by a linebreak.
		# Heading text is converted to lowercase. Spaces are converted to underscores and hyphens are removed.
		# In the cell text, line endings are replaced with commas.

		clean_key = data_headings[cell_index].lower().replace(' ', '_').replace('-', '').replace('/', '')
		clean_value = cell.replace('\n', ',').replace(":", "-")

		if cell_index == 0:
			cell_text = "- " + clean_key + ": " + clean_value + "\n"
		else:
			cell_text = "  " + clean_key + ": " + clean_value + "\n"

		# Add this line of text to the current YAML string.
		if cell_text.strip() != ":":
			yaml_text += cell_text

	new_yaml.write(yaml_text)

	# Newline after record
	new_yaml.write("\n")

# We're done! Close the CSV file.
new_yaml.close()
csvfile.close()
