def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

read_file("test.txt")

def write_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
            print("Text written to {file_path}")
    except Exception as e:
        print("an error occured: {e}")

file_path = 'example.txt'
text = 'hello, this is a sample text'
write_file(file_path, text)        
