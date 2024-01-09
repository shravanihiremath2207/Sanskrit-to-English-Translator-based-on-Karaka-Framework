import os
import pydot
import spacy
from collections import defaultdict

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Function to find Karma (object) for the verb
def find_karma_for_verb(verb_token):
    karma = set()  # Use a set to store Karma entities to prevent duplicates
    for child in verb_token.children:
        if child.dep_ in ["dobj", "attr", "acomp"]:
            # Check if the token is an adjective and its head is a noun
            if child.pos_ == "ADJ" and child.head.pos_ == "NOUN":
                karma_text = child.head.text + " " + child.text
                karma.add(karma_text)
            else:
                karma_text = child.text
                karma.add(karma_text)
    return list(karma)  # Convert set back to list for consistent processing

# Function to create the mind map based on the Karaka framework for a given sentence
def create_mind_map_for_sentence(sentence, graph, verb_karma_dict):
    # Process the sentence with spaCy
    doc = nlp(sentence)

    for token in doc:
        if token.pos_ in ["VERB", "AUX"]:
            verb = token.text

            # Find Kartru (subject)
            kartru = [child.text for child in token.children if child.dep_ in ["nsubj", "csubj"]]
            compound_kartru = [child.text for child in token.children if child.dep_ in ["compound"] and child.head.dep_ in ["nsubj", "csubj"]]
            kartru.extend(compound_kartru)

            # Find Karma (object)
            karma = find_karma_for_verb(token)

            # Add nodes and edges for the verb and its associated entities
            verb_node = pydot.Node(name=verb, shape="ellipse")
            graph.add_node(verb_node)

            for entity in [kartru, karma]:
                for item in entity:
                    entity_node = pydot.Node(name=item, shape="box")
                    graph.add_node(entity_node)

                    if entity == kartru:
                        edge = pydot.Edge(entity_node, verb_node, label="Kartru")
                    elif entity == karma:
                        edge = pydot.Edge(verb_node, entity_node, label="Karma")
                    graph.add_edge(edge)

# Function to create the mind map for a paragraph
def create_mind_map_for_paragraph(paragraph, output_file):
    # Create the graph for the entire paragraph
    graph = pydot.Dot(graph_type="graph")

    # Split the paragraph into individual sentences
    sentences = [sent.text.strip() for sent in nlp(paragraph).sents]

    for sentence in sentences:
        create_mind_map_for_sentence(sentence, graph, {})

    # Save the mind map for the entire paragraph to a file
    graph.write_png(output_file)

if __name__ == "_main_":
    paragraph = "Once there was a young woman named Vidya who lived in a village. She wanted to travel and explore the world, but she couldn't speak English. So, she joined an English course in her village. Vidya learned grammar, vocabulary, and how to pronounce words. She practiced talking with her classmates and understood simple conversations. Vidya felt more confident and decided to travel alone to an English-speaking country. She visited big cities, talked to local people, and learned about different cultures. Vidya realized that learning English opened doors to new experiences and helped her connect with people all over the world. Her journey showed that with determination and learning, anything is possible. She came from the village but conquered the world with her grit."
    output_file = "karaka_mind_map.png"
    create_mind_map_for_paragraph(paragraph, output_file)

    
english_to_sanskrit_with_vibhakti={
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