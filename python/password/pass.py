import numpy as np

def mypassword():
    num_length = np.random.randint(1, 10)  # Random length for numeric digits
    num = np.random.randint(0, 10, num_length)  # Generate numeric digits

    upper = np.random.randint(97, 123, 10)  # Generate random lowercase ASCII codes
    lower = np.random.randint(65, 91, 10)   # Generate random uppercase ASCII codes
    li = []
    li.extend(upper)
    li.extend(lower)

    password = []

    for _ in range(1, 5):  # Use underscore for unused loop variables
        password.append(chr(np.random.choice(li)))

    password.insert(np.random.randint(0, len(password)), str(np.random.choice(num)))  # Insert random number
    np.random.shuffle(password)  # Shuffle the password characters for randomness
    return ''.join(password)  # Convert the list of characters to a string and return

print(mypassword())
