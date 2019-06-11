# Caesar Cipher

Jun 11 2019

## Description

- This Python program encrypts and decrypts messages based on the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).
- The Caesar cipher is a type of substitution cipher where letters are replaced with other letters from a shifted position in an alphabet set.
  - For example, the letter `'a'`, shifted by two (2) positions, would result in the letter `'c'`.

## `cipherMessage(message, key, mode)`

- To encrypt and decrypt messages, use the `cipherMessage(message, key, mode)` function.
- The `cipherMessage(message, key, mode)` accepts three parameters:
  - `message` (type: string)
    - The message parameter accepts any string object.
    - Enter the message you want encrypt or decrypt in this first parameter.
  - `key` (type: integer)
    - Select and enter your desired encryption/decryption key value.
  - `mode` (type: string)
    - There are only two (2) modes:
      - Enter `'e'` if you want to encrypt messages.
      - Enter `'d'` if you want to decrypt messages.

### Encryption Example

```python
cipherMessage('Today is beautiful!', 37, 'e')

# 3_~0BD%;D-!0.,%@.*S
```

- Remember to enter `'e'` as the mode parameter so that the `cipherMessage()` function is set properly to encrypt messages.
- When you encrypt the message string `'Today is beautiful!'`, the `cipherMessage()` function will return the encrypted string message: `'3_~0BD%;D-!0.,%@.*S'`.

### Decryption Example

```python
cipherMessage('3_~0BD%;D-!0.,%@.*S', 37, 'd')

# Today is beautiful!
```

- Remember to enter `'d'` as the mode parameter so that the `cipherMessage()` function is set properly to decrypt messages.
- When you decrypt the encrypted message string `'3_~0BD%;D-!0.,%@.*S'`, the `cipherMessage()` function will return the decrypted string message: `'Today is beautiful!'`.

## Challenges

### Decryption With Key

- Decrypt the following:
    > O zs2m45xm4u z3?-k 5-tm6q-35ooq33r5xx9-pqo29`4qp-4tu3-yq33msq?
    >
    > *(Hint: 12)*

### Decryption Without Key

- Decrypt the following:
    > u9@*w= *w7w&381A

- Explore the handy `magicOutput(message)` function!

## Future Development

- [ ] TODO: Dictionary lookup for `magicOutput()` function. Return corresponding keys in descending order of relevance.
  - [ ] <https://pypi.org/project/PyDictionary/>
  - [ ] <https://pypi.org/project/pyenchant/#description>
- [ ] TODO: Links conversion `/`.
- [ ] TODO: Error handling for edge cases.
- [ ] TODO: Front-end GUI.

## Resources

- <https://en.wikipedia.org/wiki/Caesar_cipher>
- <https://inventwithpython.com/cracking/chapter5.html>
