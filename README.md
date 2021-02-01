# TranspositionCipherBruteForce
Transposition Cipher BruteForce. Python script that finds the correct key (with given keylength/blocklength) by bruteforcing every key and checking if the output text is english.

The decrypt function in transpositionBruteForce.py takes a row input that defaults to False. The default read in for the transpositon cipher is thus column, but can also be used for row. defaults to row output, you can change this in the code.

The keys is not always correct when comparing it to JcrypTool even though the text gets decrypted

Can also change the dictionary.txt to support other languages.

## USE
Copy the text in to encrypted.txt and save.
Run the script transpositionBruteForce.py and give the keylength to search for. It will stop when the detected english level is above a threshold of 20% and ask if its correct.

If successfully decrypting the ciphertext the plaintext will be stored in decrypted.txt. If not it will give you the key with the highest percentage of english.

## The code are based on
* http://inventwithpython.com/hacking
* http://www.crypto-it.net/eng/simple/columnar-transposition.html
