# Error Handling Lab

def read_user_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            print("\n File Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found! Please check the filename and try again.")
    except PermissionError:
        print("Permission denied! You don’t have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
read_user_file()
