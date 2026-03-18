word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]


categories = {
    "animals": {
        "easy": [
            "cat", "dog", "cow", "bat", "ant", "fox", "hen", "bee", "rat", "goat",
            "lion", "frog", "bear", "deer", "duck"
        ],
        "medium": [
            "tiger", "rabbit", "monkey", "zebra", "pigeon", "donkey", "parrot",
            "giraffe", "leopard", "penguin", "dolphin", "hamster", "peacock", "ostrich", "buffalo"
        ],
        "hard": [
            "elephant", "crocodile", "chimpanzee", "kangaroo", "alligator",
            "rhinoceros", "hippopotamus", "porcupine", "woodpecker", "orangutan",
            "chameleon", "hedgehog", "armadillo", "salamander", "grasshopper"
        ]
    },

    "fruits": {
        "easy": [
            "fig", "kiwi", "pear", "plum", "lime", "apple", "grape", "mango", "guava", "peach",
            "melon", "lemon", "berry", "olive", "dates"
        ],
        "medium": [
            "orange", "banana", "papaya", "apricot", "avocado", "coconut", "lychee",
            "mulberry", "jackfruit", "custard", "pomelo", "durian", "raisin", "carrot", "tomato"
        ],
        "hard": [
            "pineapple", "watermelon", "pomegranate", "strawberry", "dragonfruit",
            "blackberry", "cranberry", "passionfruit", "raspberry", "gooseberry",
            "tangerine", "persimmon", "starfruit", "longan", "elderberry"
        ]
    },

    "countries": {
        "easy": [
            "india", "china", "japan", "nepal", "chile", "spain", "italy", "qatar", "egypt", "kenya",
            "laos", "sudan", "yemen", "ghana", "syria"
        ],
        "medium": [
            "canada", "brazil", "germany", "france", "mexico", "sweden", "norway",
            "turkey", "poland", "ireland", "ukraine", "thailand", "romania", "finland", "denmark"
        ],
        "hard": [
            "australia", "argentina", "kazakhstan", "portugal", "madagascar",
            "azerbaijan", "uzbekistan", "switzerland", "philippines", "mozambique",
            "luxembourg", "mauritania", "kyrgyzstan", "turkmenistan", "afghanistan"
        ]
    },

    "programming": {
        "easy": [
            "loop", "list", "code", "file", "bug", "data", "text", "type", "math", "byte",
            "node", "task", "input", "print", "logic"
        ],
        "medium": [
            "string", "python", "object", "method", "class", "binary", "compile",
            "syntax", "module", "thread", "server", "client", "return", "import", "debug"
        ],
        "hard": [
            "algorithm", "recursion", "dictionary", "inheritance", "polymorphism",
            "encapsulation", "abstraction", "framework", "middleware", "multithreading",
            "serialization", "authentication", "dependency", "optimization", "constructor"
        ]
    },

    "colors": {
        "easy": [
            "red", "blue", "pink", "gray", "black", "white", "green", "brown", "gold", "cyan",
            "navy", "lime", "teal", "beige", "pearl"
        ],
        "medium": [
            "yellow", "purple", "orange", "violet", "indigo", "silver", "maroon",
            "magenta", "scarlet", "turquoise", "lavender", "crimson", "mustard", "bronze", "peach"
        ],
        "hard": [
            "chartreuse", "ultramarine", "aquamarine", "vermilion", "fuchsia",
            "periwinkle", "burgundy", "cerulean", "sepia", "amethyst",
            "saffron", "mahogany", "aubergine", "carmine", "celadon"
        ]
    },

    "sports": {
        "easy": [
            "golf", "judo", "chess", "rugby", "tennis", "boxing", "karate", "hockey", "soccer", "skating",
            "rowing", "cycling", "archery", "bowling", "running"
        ],
        "medium": [
            "cricket", "baseball", "wrestling", "badminton", "swimming", "volleyball",
            "shooting", "handball", "fencing", "surfing", "snooker", "gymnastics", "kabaddi", "taekwondo", "triathlon"
        ],
        "hard": [
            "powerlifting", "snowboarding", "bodybuilding", "windsurfing", "equestrian",
            "synchronized", "weightlifting", "skateboarding", "mountaineering", "motorsports",
            "paragliding", "decathlon", "freestyle", "bobsleigh", "biathlon"
        ]
    },

    "vehicles": {
        "easy": [
            "car", "bus", "van", "bike", "jeep", "taxi", "train", "truck", "ship", "boat",
            "scooter", "metro", "cycle", "wagon", "canoe"
        ],
        "medium": [
            "tractor", "bicycle", "airplane", "submarine", "helicopter", "bulldozer",
            "ambulance", "rickshaw", "tramway", "glider", "minibus", "freighter", "sailboat", "jetski", "ferry"
        ],
        "hard": [
            "motorcycle", "locomotive", "spacecraft", "hovercraft", "excavator",
            "fighterjet", "snowmobile", "fireengine", "warship", "zeppelin",
            "speedboat", "monorail", "seaplane", "autogyro", "limousine"
        ]
    },

    "school": {
        "easy": [
            "book", "pen", "desk", "bag", "exam", "quiz", "note", "chalk", "board", "class",
            "scale", "paper", "table", "chair", "teach"
        ],
        "medium": [
            "marker", "eraser", "lesson", "pencil", "subject", "project", "science",
            "library", "college", "uniform", "drawing", "grammar", "student", "chapter", "physics"
        ],
        "hard": [
            "assignment", "attendance", "laboratory", "mathematics", "dictionary",
            "curriculum", "blackboard", "geography", "scholarship", "examination",
            "headmaster", "notebook", "principal", "chemistry", "certificate"
        ]
    },

    "film_terms": {
        "easy": [
            "hero", "scene", "actor", "drama", "comedy", "fight", "story", "music", "dance", "queen",
            "crown", "voice", "frame", "title", "image"
        ],
        "medium": [
            "villain", "theater", "trailer", "romance", "fantasy", "horror", "costume",
            "director", "dialogue", "stuntman", "episode", "screenplay", "camera", "editing", "release"
        ],
        "hard": [
            "cinematography", "documentary", "blockbuster", "screenwriter", "franchise",
            "soundtrack", "production", "animation", "biographical", "independent",
            "filmmaking", "masterpiece", "adaptation", "characterization", "premiere"
        ]
    },

    "space": {
        "easy": [
            "moon", "mars", "star", "sun", "orbit", "comet", "earth", "venus", "alien", "eclipse",
            "rocket", "planet", "galaxy", "meteor", "cosmos"
        ],
        "medium": [
            "saturn", "jupiter", "uranus", "neptune", "asteroid", "gravity", "telescope",
            "solstice", "capsule", "shuttle", "crater", "nebula", "vacuum", "launch", "module"
        ],
        "hard": [
            "constellation", "astronaut", "observatory", "interstellar", "supernova",
            "spacecraft", "cosmology", "blackhole", "exoplanet", "satellite",
            "quasar", "wormhole", "lightyear", "trajectory", "microgravity"
        ]
    },

    "jobs": {
        "easy": [
            "chef", "nurse", "pilot", "farmer", "actor", "judge", "clerk", "guard", "painter", "driver",
            "tailor", "doctor", "lawyer", "singer", "writer"
        ],
        "medium": [
            "teacher", "dentist", "plumber", "cashier", "manager", "soldier", "engineer",
            "designer", "journalist", "mechanic", "pharmacist", "carpenter", "electrician", "scientist", "firefighter"
        ],
        "hard": [
            "photographer", "archaeologist", "entrepreneur", "veterinarian", "psychiatrist",
            "statistician", "nutritionist", "researcher", "technician", "accountant",
            "politician", "biologist", "astronomer", "administrator", "consultant"
        ]
    }
}