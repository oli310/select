import re
import sys
import getopt

# Parse command-line arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:w:s:", ["help", "input=", "output=", "word=", "select="])
except getopt.GetoptError:
    print(f"Usage: {sys.argv[0]} --input <input_file> --output <output_file> --word <word> --select <char>")
    sys.exit(2)

input_file = ""
output_file = ""
word = ""
select_char = ""

for opt, arg in opts:
    if opt in ("-h", "--help"):
        print(f"Usage: {sys.argv[0]} --input <input_file> --output <output_file> --word <word> --select <char>")
        sys.exit()
    elif opt in ("-i", "--input"):
        input_file = arg
    elif opt in ("-o", "--output"):
        output_file = arg
    elif opt in ("-w", "--word"):
        word = arg
    elif opt in ("-s", "--select"):
        select_char = arg

# Check if the required arguments are present
if not input_file or not output_file or not word or not select_char:
    print(f"Usage: {sys.argv[0]} --input <input_file> --output <output_file> --word <word> --select <char>")
    sys.exit(2)

# Read the input from the input file
with open(input_file, 'r') as file:
    long_string = file.read()

# Find words with the select character in front of them using regular expression
result = re.findall(f'\\{select_char}\\w+', long_string)

# Add the word in front of the selected words
result_with_word = [f"{word}{w}" for w in result]

# Write the result to the output file
with open(output_file, 'w') as file:
    file.write('\n'.join(result_with_word))
    file.write('\n')
