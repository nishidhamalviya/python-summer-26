def read_file():
    file_path = input("Enter the filename:")
    try:
        with open(file_path,'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("error") 
    except Exception as e:
        print("an error occured")


                

def divide_numbers():
    try:
        a = float(input("Enter the first number"))
        b = float(input("Enter the second numbers")) 
        result = a/b
        print("The result when a divides b is:")

    except ZeroDivisionError:
        print("invalid")     
    except ValueError:
        print("invalid") 
    except Exception as e:      
        print("error")           