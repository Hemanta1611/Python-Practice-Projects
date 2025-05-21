# Random Password Generator | Not a Security Provider (no encryption and decription)

A secure and customizable password generator built with Python that allows users to create strong passwords based on their specific requirements.

## Features

- Generate passwords of custom length (minimum 8 characters)
- Customize password composition with options for:
  - Uppercase letters
  - Special characters
  - Numbers
  - Lowercase letters (always included)
- Ensures at least one character from each selected character type
- Random shuffling of characters for enhanced security

## Requirements

- Python 3.x
- No external dependencies required (uses built-in Python modules)

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Follow the interactive prompts:
   - Enter desired password length (minimum 8 characters)
   - Choose whether to include uppercase letters (yes/no)
   - Choose whether to include special characters (yes/no)
   - Choose whether to include numbers (yes/no)

3. The generated password will be displayed on the screen

## Example
Enter the length of the password: 12
Include uppercase letters? (yes/no): yes
Include special characters? (yes/no): yes
Include numbers? (yes/no): yes
Your password is: Kj#9mP$2nL5v


## Security Features

- Enforces minimum password length of 8 characters
- Guarantees inclusion of at least one character from each selected character type
- Randomly shuffles all characters to prevent predictable patterns
- Uses Python's secure random number generator

## Note

This password generator is designed for educational purposes and personal use. Always follow your organization's password policies when creating passwords for professional or sensitive accounts.