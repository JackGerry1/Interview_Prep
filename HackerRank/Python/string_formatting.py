def print_formatted(number):
    # Find the width of the binary representation of the largest number
    width = len(bin(number)[2:])
    
    for n in range(1, number + 1):
        dec = str(n).rjust(width)
        octal = oct(n)[2:].rjust(width)
        hexa = hex(n)[2:].upper().rjust(width)
        binary = bin(n)[2:].rjust(width)
        
        print(dec, octal, hexa, binary)
        
    
