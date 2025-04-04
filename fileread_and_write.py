# File Read & Write Challenge: Reading and writing to files

def read_and_write_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            content = file.read()  # Read the entire content of the file
            
        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"File has been read, modified, and saved as {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError:
        print(f"Error: Unable to read/write the file.")
        

# Example usage
input_file = 'test.txt'  # Replace with your input file name
output_file = 'modified_test.txt'  # Replace with your desired output file name

read_and_write_file(input_file, output_file)
