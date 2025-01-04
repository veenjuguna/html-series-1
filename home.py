def greet_user(name):
    return f"Hello, {name}! Welcome to the Python world."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet_user(user_name)
    print(greeting)