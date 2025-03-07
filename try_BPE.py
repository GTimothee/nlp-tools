from tokenizers import Tokenizer, models, trainers, pre_tokenizers

"""
uv add tokenizers

Output:
['I', 'lo', 'v', 'e', 'philosophy']
"""

# Initialize BPE Tokenizer
tokenizer = Tokenizer(models.BPE())

# Pre-tokenizer (splits text into words)
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Train on a sample dataset
trainer = trainers.BpeTrainer(vocab_size=172, special_tokens=["<unk>", "<s>", "</s>"])
tokenizer.train(["data/philosophy_wiki.txt"], trainer)

# Save the trained tokenizer
tokenizer.save("data/models/bpe/bpe_tokenizer.json")

# Load and use the tokenizer
tokenizer.from_file("data/models/bpe/bpe_tokenizer.json")
output = tokenizer.encode("I love philosophy!")
print(output.tokens) 