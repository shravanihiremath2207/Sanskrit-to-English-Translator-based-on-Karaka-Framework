import string

english_to_sanskrit = {
    "Once": "एकदा",
    "there":"तत्र",
    "f":"|",
    "was": "आसीत्",
    "a": "एका",
    "young": "किशोरी",
    "woman": "स्त्री",
    "named": "नाम",
    "Vidya": "विद्या",
    "who": "या",
    "lived": "आसीत्",
   
    "village": "ग्राम",
    "She": "सा",
    "wanted": "इच्छती",
  
    "travel": "प्रयाणम्",
    "and": "च",
    "explore": "अन्वेषितुम्",
    "the": "तत्",
    "world": "जगत्",
    "but": "तथापि",
    "she": "सा",
    "couldnt": "नाशक्नोति",
    "speak": "वक्तुम्",
    "English": "अङ्ग्लभाषा",
    "So": "ततः",
    "joined": "सम्प्रविश्य",
    "an": "एकं",
    "course": "अभ्यासक्रम:",
    "her": "सा",
    "Vidya": "विद्या",
    "learned": "अधीतवती",
    "grammar": "व्याकरणम्",
    "vocabulary": "शब्दकोश",
    "and": "च",
    "how": "कथम्",
    "to": "इत्यस्मै",
    "pronounce": "उच्चारणम्",
    "words": "शब्द:",
    "She": "सा",
    "practiced": "अभ्यासत",
    "talking": "वक्तुम्",
    "with": "सह",
    "She": "सा",
    "classmates": "सहपाठिनः",
    "and": "च",
    "understood": "अवगच्छत",
    "simple": "सरला",
    "conversations": "संभाषणानि",
    "Vidya": "विद्या",
    "felt": "भवति",
    "more": "अधिकम्",
    "confident": "आत्मविश्वाससम्पन्ना",
    "and": "च",
    "decided": "निर्णीत",
    "travel": "प्रयाणम्",
    "alone": "एका",
    "an": "एकं",
    "Englishspeaking": "अङ्ग्लभाषाभाषिणीभूतां",
    "country": "देश:",
    "She": "सा",
    "visited": "आगच्छत",
    "big": "महत्तरां",
    "cities": "नगराणि",
    "talked": "वक्तुम्",
    "to": "सह",
    "local": "स्थानिक",
    "people": "जनाः",
    "and": "च",
    "learned": "अधीतवती",
    "about": "विचार्य",
    "different": "भिन्नः",
    "cultures": "संस्कृतिः",
    "Vidya": "विद्या",
    "realized": "अवगच्छत",
    "that": "या",
    "learning": "अध्ययनानि",
    "English": "अङ्ग्लभाषा",
    "opened": "उद्घाटितानि",
    "doors": "द्वाराणि",
    "to": "यात्राम्",
    "new": "नवानि",
    "experiences": "अनुभवानि",
    "and": "च",
    "helped": "सहायितवती",
    "she": "ताः",
    "connect": "सम्बद्धवती",
    "with": "सह",
    "people": "जनाः",
    "all": "सर्वत्र",
    "over": "अधिकम्",
    "the": "तत्",
    "world": "जगत्",
    "she": "सा",
    "journey": "प्रयाणः",
    "showed": "दर्शितवती",
    "that": "या",
    "with": "सह",
    "determination": "निश्चयात्मिका",
    "and": "च",
    "learning": "अध्ययनात्",
    "anything": "किमपि",
    "is": "भवति",
    "possible": "सम्भवम्",
    "She": "सा",
    "came": "आगत्य",
    "from": "ततः",
    "village.": "ग्राम",
  
    "but": "तथापि",
    "conquered": "विजयीभूता",
 
    "world": "जगत्",
    "with": "सह",
    "She": "ताः",
    "grit": "साहस"
}





# def remove_punctuation(paragraph):
#     # Create a translation table to remove punctuation characters
#     translator = str.maketrans('', '', string.punctuation)

#     # Use translate() to remove punctuation from the paragraph
#     return paragraph.translate(translator)
def replace_punctuation_with_f_and_space(paragraph):
    # Define a string containing all punctuation marks (excluding apostrophes)
    punctuation_marks = string.punctuation.replace("'", "")
    
    # Replace each punctuation mark (excluding apostrophes) with a space followed by the letter 'f'
    for punctuation in punctuation_marks:
        paragraph = paragraph.replace(punctuation, ' f')
    
    return paragraph
# Example usage
paragraph = "Once there was a young woman named Vidya who lived in a village. She wanted to travel and explore the world, but she couldnt speak English. So, she joined an English course in her village. Vidya learned grammar, vocabulary, and how to pronounce words. She practiced talking with her classmates and understood simple conversations. Vidya felt more confident and decided to travel alone to an Englishspeaking country. She visited big cities, talked to local people, and learned about different cultures. Vidya realized that learning English opened doors to new experiences and helped her connect with people all over the world. Her journey showed that with determination and learning, anything is possible. She came from the village but conquered the world with her grit."

cparagraph = replace_punctuation_with_f_and_space(paragraph)
#print(cparagraph)


# # Example usage
# paragraph =  "Once there was a young woman named Vidya who lived in a village. She wanted to travel and explore the world, but she couldn't speak English. So, she joined an English course in her village. Vidya learned grammar, vocabulary, and how to pronounce words. She practiced talking with her classmates and understood simple conversations. Vidya felt more confident and decided to travel alone to an English-speaking country. She visited big cities, talked to local people, and learned about different cultures. Vidya realized that learning English opened doors to new experiences and helped her connect with people all over the world. Her journey showed that with determination and learning, anything is possible. She came from the village but conquered the world with her grit."
# cparagraph = replace_punctuation_with_f(paragraph)
# print(cparagraph)
english_words = cparagraph.split()

# Translate each word using the dictionary
translated_words = [english_to_sanskrit.get(word, word) for word in english_words]

# Join the translated words back to form the translated paragraph
translated_paragraph = " ".join(translated_words)

# Print the translated paragraph
print(translated_paragraph)

