import os
from Crypto.Cipher import AES

# Define the length of the random number in bytes
length = 8

# Define the counter value for the AES-CTR generator
# This can be any value, as long as it is incremented with each use of the generator
counter = 0

# Define the number of digits in the final random number
num_digits = 16

# Define the format string for the final random number
# This will create a 16-digit number with leading zeros
format_string = '{:0' + str(num_digits) + 'd}'

# Generate a random key and nonce for the AES-CTR generator
key = os.urandom(16)
nonce = os.urandom(8)

# Define the AES-CTR generator function
def aes_ctr(key, nonce, counter):
    # Create an AES cipher object in CTR mode
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce, initial_value=counter)

    # Generate the random bytes using the AES-CTR generator
    output = cipher.encrypt(bytes([0x00] * length))

    # Convert the output to an integer
    value = int.from_bytes(output, byteorder='big')

    # Return the value formatted as a 16-digit number
    return format_string.format(value)

# Generate a random 16-digit number using AES-CTR
random_number = aes_ctr(key, nonce, counter)

print(random_number)
