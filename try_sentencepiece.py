import sentencepiece as spm

import io
import sys 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")  # for printing in console


"""
uv add sentencepiece

Outputs: 

['▁I', '▁', 'lo', 'v', 'e', '▁pr', 'o', 'g', 'ra', 'm', 'm', 'i', 'ng', '!']
[129, 3, 104, 109, 11, 38, 20, 90, 76, 28, 28, 31, 41, 0]
I love programming ⁇

Notes:
- If ! (exclamation mark) is not in the vocabulary, it may be replaced with an unknown token (⁇).
- If punctuation marks weren’t included in training, they get replaced. Fix: Ensure the training corpus includes various characters.
""" 

# Train a SentencePiece model
spm.SentencePieceTrainer.Train('--input=data/philosophy_wiki.txt --model_prefix=data/models/sentencepiece/philosophy --vocab_size=172')

# Load the trained model
sp = spm.SentencePieceProcessor(model_file='data/models/sentencepiece/philosophy.model')

# Tokenization
text = "I love programming!"
tokens = sp.encode(text, out_type=str)
print(tokens)  

# Token IDs
token_ids = sp.encode(text, out_type=int)
print(token_ids)  

# Detokenization
detokenized_text = sp.decode(token_ids)
print(detokenized_text)  
