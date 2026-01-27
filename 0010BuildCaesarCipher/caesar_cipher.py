def caesar(shift: int, text: str, encrypted: bool = True) -> str:
    """
    Applies the Caesar Cipher to encrypt or decrypt a given text.

    The Caesar Cipher shifts each alphabetical character in the text
    by a fixed number of positions in the alphabet.

    Parameters:
    shift (int): Number of positions to shift (must be between 1 and 25).
    text (str): The input text to encrypt or decrypt.
    encrypted (bool):
        - True  -> encrypt the text
        - False -> decrypt the text

    Returns:
    str: The transformed (encrypted or decrypted) text.
         If shift is invalid, an error message is returned.
    """
    # The English alphabet used as the reference for shifting
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Validate shift value (Caesar Cipher only allows 1–25)
    if shift < 1 or shift > 25:
        return f"The shift {shift} must be between 1 and 25"

    # If decrypting, reverse the shift direction
    if not encrypted:
        shift = - shift

    # Create the shifted alphabet based on the shift value
    # Example (shift = 3):
    # abcdefghijklmnopqrstuvwxyz -> defghijklmnopqrstuvwxyzabc
    shifted_alphabet = alphabet[shift:] + alphabet[: shift]

    # Create a translation table that maps:
    # - lowercase letters
    # - uppercase letters
    shifted_alphabet_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    # Translate the input text using the translation table
    return text.translate(shifted_alphabet_table)


def encrypt(shift: int, text: str) -> str:
    """
    Encrypts the given text using the Caesar Cipher.

    Parameters:
    shift (int): Number of positions to shift.
    text (str): Plain text to encrypt.

    Returns:
    str: En
    """

    # Call the main Caesar function in encryption mode
    return caesar(shift, text)

def decrypt(shift: int, text: str) -> str:
    """
    Decrypts a Caesar Cipher encrypted text.

    Parameters:
    shift (int): Number of positions to shift.
    text (str): Encrypted text to decrypt.

    Returns:
    str: Decrypted (original) text.
    """
    # Call the main Caesar function in decryption mode
    return caesar(shift, text, encrypted=False)


#test cases
if __name__ == "__main__":
    # Test Case 1: Basic encryption
    shift = 5
    text = "hi"
    encrypted_text = encrypt(shift, text)
    print("Encrypted:", encrypted_text)  # Expected: mn

    # Test Case 2: Basic decryption
    decrypted_text = decrypt(shift, encrypted_text)
    print("Decrypted:", decrypted_text)  # Expected: hi


    # Test Case 3: Preserve uppercase letters
    text = "Hello"
    print("Encrypted:", encrypt(3, text))  # Expected: Khoor

    # Test Case 4: Non-alphabet characters should remain unchanged
    text = "Hello, World!"
    print("Encrypted:", encrypt(3, text))  # Expected: Khoor, Zruog!

    # Test Case 5: Invalid shift value
    print(encrypt(30, "test"))  # Expected: error message