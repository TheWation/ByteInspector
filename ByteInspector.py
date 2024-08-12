import base64

def is_non_printable(char):
    """Check if a character is non-printable."""
    return char < 0x20 or char > 0x7E

def check_non_printable_chars(input_string):
    """Check for non-printable characters in the input string or base64-encoded string."""
    try:
        # Attempt to decode the input as base64
        decoded_bytes = base64.b64decode(input_string, validate=True)
        hex_string = decoded_bytes.hex()
        source_type = "base64"
    except (base64.binascii.Error, ValueError):
        # If decoding fails, treat the input as a regular string
        decoded_bytes = input_string.encode('utf-8')
        hex_string = decoded_bytes.hex()
        source_type = "string"

    # Check for non-printable characters
    non_printable_chars = []
    for i in range(0, len(hex_string), 2):
        char_hex = hex_string[i:i+2]
        if char_hex == '00' or is_non_printable(int(char_hex, 16)):
            non_printable_chars.append(char_hex)

    return non_printable_chars, source_type

# Example usage
input_string = input("[?] Enter a base64-encoded string or a regular string: ")
result, source_type = check_non_printable_chars(input_string)

if result:
    print(f"[+] Non-printable characters found in {source_type}: {', '.join(result)}")
else:
    print(f"[-] No non-printable characters found in {source_type}.")