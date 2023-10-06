import os
import re


# Corner case, colorFromRGB() needs a temporary transformation
def replace_colorFromRGB_commas(text):
    def replacer(match):
        return match.group(0).replace(',', '|')
    return re.sub(r'colorFromRGB\([^)]+\)', replacer, text)

# Modifying the code flattener to accept a file name as an argument
def flatten_code_from_file(file_path):
    """
    Flatten code from a file and return it as a string.
    
    Args:
    - file_path (str): The path to the file containing the code to flatten.
    
    Returns:
    - str: The flattened code as a string.
    """
    # Initialize variables for the final refinement
    flattened_code = []
    token = ''
    open_brackets = 0
    open_parentheses = 0
    
    # Read the code from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Iterate through each character in the code
    for char in code:
        # Count open and close brackets
        if char in ['{', '[']:
            open_brackets += 1
        elif char in ['}', ']']:
            open_brackets -= 1
        elif char == '(':
            open_parentheses += 1
        elif char == ')':
            open_parentheses -= 1

        # Add characters to current token
        if char != '\n' or open_parentheses > 0:  # Preserve newlines within parentheses
            token += char

        # Commit token to flattened code when a line ends or a bracket closes
        if (char == '\n' and open_parentheses == 0) or (open_brackets == 0 and char in ['}', ']']):
            if token.strip():
                # Replace multiple spaces with a single space for readability
                token = ' '.join(token.split())
                flattened_code.append(token.strip())
            token = ''
    
    # Combine the flattened code lines
    flattened_code_str = '\n'.join(flattened_code)
    return flattened_code_str


def search_and_flatten_in_tree(root_dir, target_strings, file_extension=".kt"):
    """
    Search for target strings in all .kt files within a directory tree, flatten the code and display matching lines.

    Args:
    - root_dir (str): The root directory of the tree to search.
    - target_strings (list): List of target strings to search for.
    - file_extension (str): File extension to consider. Default is ".kt".

    Returns:
    - None: Prints out the matching lines in the code.
    """
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                flattened_code = flatten_code_from_file(file_path)
                
                # Search for target strings in flattened code
                for line in flattened_code.split('\n'):
                    # Replace commas within colorFromRGB() with '|' to deal with later parsing
                    line = replace_colorFromRGB_commas(line)

                    if any(target_string in line for target_string in target_strings):
                        if line.strip().startswith(("//", "/*", "*", "*/", "import", "else", "private fun")): 	# Skip lines that start with comments, imports, else statements, function decs
                            continue

                        print(f"{line}")
#                        print(f"File: {file_path}\nLine: {line}\n")

def main():
    root_dir = "e:/dev/github/unciv/core/src/com/unciv"  # Replace with your actual path
    target_strings = ["getUiBackground", "getUIColor", "BorderedTable"]
    search_and_flatten_in_tree(root_dir, target_strings)


main()

#flattened_code = flatten_code_from_file("E:/Downloads/Popup.kt")
#print(f"{flattened_code}\n")


