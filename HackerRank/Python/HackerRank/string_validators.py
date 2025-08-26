if __name__ == '__main__':
    s = input()
    
    is_alphanumeric = any(c.isalnum() for c in s)
    is_alphabetic = any(c.isalpha() for c in s)  
    is_digits = any(c.isdigit() for c in s)
    is_lower = any(c.islower() for c in s)
    is_upper = any(c.isupper() for c in s)
    
    print(is_alphanumeric)
    print(is_alphabetic)
    print(is_digits)
    print(is_lower)
    print(is_upper) 
    