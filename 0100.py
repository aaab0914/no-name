# Create a programming glossary
glossary = {
    'variable':'A named storage location in memory that hold a value.',
    'function':'A block of organized, reusable code that performa a single action.',
    'list':'A collection of items in a particular order, mutable and allows duplicate member.',
    'loop':'A programming structure what repeat a sequence of instructions until a specific condition is met.'
    }

# Print each word and its meaning with neat formatting
print("Progamming Glossary:")
print("=" * 50)

for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f" {meaning}")
    
    
