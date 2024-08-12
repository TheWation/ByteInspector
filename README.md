# ByteInspector

The Non-Printable Character Checker is a Python-based tool designed to identify non-printable characters in base64-encoded strings and regular strings. It decodes base64 strings, converts the resulting bytes to hexadecimal, and checks each character for non-printability. The tool can handle both base64-encoded and regular string inputs. 

## Features

- Detects non-printable characters in base64-encoded strings
- Identifies non-printable characters in regular strings
- Provides clear output indicating the type of input (base64 or string) and the non-printable characters found
- Supports Python 3.x

## Usage
Run the script using Python:

```bash
python non_printable_checker.py
```

When prompted, enter a base64-encoded string or a regular string:

```text
[?] Enter a base64-encoded string or a regular string: gASVNQAAAAAAAACMAm50lIwGc3lzdGVtlJOUjB1jdXJsIGh0dHBzOi8vd2ViaG9vay5zaXRlLy4uLpSFlFKULg==
```

The script will analyze the input and display the results:

```text
[+] Non-printable characters found in base64: 80, 04, 95, 00, 00, 00, 00, 00, 00, 00, 8c, 02, 94, 8c, 06, 94, 93, 94, 8c, 1d, 94, 85, 94, 94
```

If non-printable characters are found, they will be listed in the output.

## Contributing
Contributions to the Non-Printable Character Checker are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the project's GitHub repository.

## License
This project is licensed under the MIT License.