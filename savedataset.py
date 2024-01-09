import pandas as pd

# Your list of dictionaries containing sentence and karakas information
data = [
    {
        "sentence": "She likes to eat apples.",
        "karakas": {
            "kartru": "She",
            "karma": "apples",
            "kriya": "likes",
            "sampradan": None,
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "He gives a book to her using a pen.",
        "karakas": {
            "kartru": "He",
            "karma": "book",
            "kriya": "gives",
            "sampradan": None,
            "apadan": "her",
            "karan": "pen"
        }
    },
    {
        "sentence": "He gave a gift to his sister on her birthday.",
        "karakas": {
            "kartru": "He",
            "karma": "gift",
            "kriya": "gave",
            "sampradan": "his sister",
            "apadan": "her birthday",
            "karan": None
        }
    },
    {
        "sentence": "She cooked a delicious meal for the family.",
        "karakas": {
            "kartru": "She",
            "karma": "meal",
            "kriya": "cooked",
            "sampradan": None,
            "apadan": "the family",
            "karan": None
        }
    },
    {
        "sentence": "The students received awards from the principal.",
        "karakas": {
            "kartru": "The students",
            "karma": "awards",
            "kriya": "received",
            "sampradan": "principal",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "They watched a movie at the theater.",
        "karakas": {
            "kartru": "They",
            "karma": "movie",
            "kriya": "watched",
            "sampradan": None,
            "apadan": "the theater",
            "karan": None
        }
    },
    {
        "sentence": "The team won the championship trophy.",
        "karakas": {
            "kartru": "The team",
            "karma": "trophy",
            "kriya": "won",
            "sampradan": None,
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "She spoke to the manager about the project.",
        "karakas": {
            "kartru": "She",
            "karma": None,
            "kriya": "spoke",
            "sampradan": "manager",
            "apadan": "the project",
            "karan": None
        }
    },
    {
        "sentence": "He fixed the broken chair with a hammer.",
        "karakas": {
            "kartru": "He",
            "karma": "chair",
            "kriya": "fixed",
            "sampradan": None,
            "apadan": None,
            "karan": "hammer"
        }
    },
    {
        "sentence": "We attended a concert at the stadium.",
        "karakas": {
            "kartru": "We",
            "karma": "concert",
            "kriya": "attended",
            "sampradan": None,
            "apadan": "the stadium",
            "karan": None
        }
    },
    {
        "sentence": "The dog chased the cat up the tree.",
        "karakas": {
            "kartru": "The dog",
            "karma": "cat",
            "kriya": "chased",
            "sampradan": "tree",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "She sang a song beautifully.",
        "karakas": {
            "kartru": "She",
            "karma": "song",
            "kriya": "sang",
            "sampradan": None,
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "They danced with joy at the party.",
        "karakas": {
            "kartru": "They",
            "karma": None,
            "kriya": "danced",
            "sampradan": "joy",
            "apadan": "the party",
            "karan": None
        }
    },
    
    {
        "sentence": "The children play in the park.",
        "karakas": {
            "kartru": "The children",
            "karma": None,
            "kriya": "play",
            "sampradan": "park",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "I read an interesting book.",
        "karakas": {
            "kartru": "I",
            "karma": "book",
            "kriya": "read",
            "sampradan": None,
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "They bought flowers for their mother.",
        "karakas": {
            "kartru": "They",
            "karma": "flowers",
            "kriya": "bought",
            "sampradan": None,
            "apadan": "their mother",
            "karan": None
        }
    },
    {
        "sentence": "He sang a beautiful song.",
        "karakas": {
            "kartru": "He",
            "karma": "song",
            "kriya": "sang",
            "sampradan": None,
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "The teacher taught the students using a whiteboard.",
        "karakas": {
            "kartru": "The teacher",
            "karma": None,
            "kriya": "taught",
            "sampradan": None,
            "apadan": None,
            "karan": "whiteboard"
        }
    },
    {
        "sentence": "She wrote a letter to her friend.",
        "karakas": {
            "kartru": "She",
            "karma": "letter",
            "kriya": "wrote",
            "sampradan": None,
            "apadan": "her friend",
            "karan": None
        }
    },
    {
        "sentence": "The cat chased the mouse.",
        "karakas": {
            "kartru": "The cat",
            "karma": "mouse",
            "kriya": "chased",
            "sampradan": None,
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "We attended the party at their house.",
        "karakas": {
            "kartru": "We",
            "karma": None,
            "kriya": "attended",
            "sampradan": "party",
            "apadan": "their house",
            "karan": None
        }
    },
    {
        "sentence": "The painter used a brush to paint the picture.",
        "karakas": {
            "kartru": "The painter",
            "karma": "picture",
            "kriya": "paint",
            "sampradan": None,
            "apadan": None,
            "karan": "brush"
        }
    },
    {
        "sentence": "They celebrated Diwali with their family.",
        "karakas": {
            "kartru": "They",
            "karma": None,
            "kriya": "celebrated",
            "sampradan": "Diwali",
            "apadan": None,
            "karan": "family"
        }
    },
    
    {
        "sentence": "They played cricket in the park.",
        "karakas": {
            "kartru": "They",
            "karma": None,
            "kriya": "played",
            "sampradan": "park",
            "apadan": None,
            "karan": "cricket"
        }
    },
    {
        "sentence": "She bought a new dress from the boutique.",
        "karakas": {
            "kartru": "She",
            "karma": "dress",
            "kriya": "bought",
            "sampradan": "boutique",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "The students are studying for the exam.",
        "karakas": {
            "kartru": "The students",
            "karma": None,
            "kriya": "studying",
            "sampradan": "exam",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "He gave a speech at the conference.",
        "karakas": {
            "kartru": "He",
            "karma": "speech",
            "kriya": "gave",
            "sampradan": "conference",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "She is reading a book in the library.",
        "karakas": {
            "kartru": "She",
            "karma": "book",
            "kriya": "reading",
            "sampradan": "library",
            "apadan": None,
            "karan": None
        }
    },
    
    {
        "sentence": "The chef cooked a delicious meal for the guests.",
        "karakas": {
            "kartru": "The chef",
            "karma": "meal",
            "kriya": "cooked",
            "sampradan": None,
            "apadan": "the guests",
            "karan": None
        }
    },
    {
        "sentence": "They celebrated their success with a party.",
        "karakas": {
            "kartru": "They",
            "karma": None,
            "kriya": "celebrated",
            "sampradan": "success",
            "apadan": "a party",
            "karan": None
        }
    },
    {
        "sentence": "He fixed the broken car using a wrench.",
        "karakas": {
            "kartru": "He",
            "karma": "car",
            "kriya": "fixed",
            "sampradan": None,
            "apadan": None,
            "karan": "wrench"
        }
    },
    {
        "sentence": "She sang a beautiful song at the concert.",
        "karakas": {
            "kartru": "She",
            "karma": "song",
            "kriya": "sang",
            "sampradan": "concert",
            "apadan": None,
            "karan": None
        }
    },
    {
        "sentence": "We traveled to the mountains for a vacation.",
        "karakas": {
            "kartru": "We",
            "karma": None,
            "kriya": "traveled",
            "sampradan": "mountains",
            "apadan": "a vacation",
            "karan": None
        }
    }
   
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a .csv file
df.to_csv('karakas.csv', index=False)
