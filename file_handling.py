# File Read & Write Challenge

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
        
        # Example modification: convert text to uppercase
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
modify_file("input.txt", "output.txt")
