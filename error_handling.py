# Error Handling Lab: Handling file errors gracefully

def get_filename_and_read():
    filename = input("Please enter the filename you want to read: ")
    
    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            print("\nFile Content:")
            print(content)  # Print the content of the file
            
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found. Please check again.")
    except IOError:
        print(f"Error: Unable to read the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
get_filename_and_read()
