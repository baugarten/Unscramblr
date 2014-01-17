# Unscramblr

Given multiple ciphertexts encdoded from the same stream cipher, decode any or all to (mostly) plaintext

## Usage

```python
import unscramblr

u = unscramblr.Unscramblr("abcdefghijklmnopqrstuvwxyz") # letters that could be in the hex string (the fewer the better)
for h in hexstrings:
  u.addHexString(h)
plaintext = u.decode(hexstringIWantToDecode)
print plaintext
```
