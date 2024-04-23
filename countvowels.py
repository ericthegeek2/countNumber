def count_vowels(sentence):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count

# Test the function
sentence = "This is a sample sentence"
result = count_vowels(sentence)
print("Number of vowels:", result)  # Output: Number of vowels: 8
