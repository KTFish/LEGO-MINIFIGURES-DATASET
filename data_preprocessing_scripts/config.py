# Paths
RAW_DATASET_PATH = "./only_lego_dataset"  # Path to images scraped form Internet splitted into categories used on the website

DESTINATION_PATH = "./preprocessed_dataset"  # Path to dataset with cropped and scaled images splitted into 3 classes (yellow, skin, other)
TRAIN_DATASET_PATH = f"{DESTINATION_PATH}/train"
TEST_DATASET_PATH = f"{DESTINATION_PATH}/test"

# Number of images in dataset
NUM_IMAGES_RAW = 14999


# Shape of images
CROP_WIDTH, CROP_HEIGHT = 310, 310  # Shape after cropping
FINAL_WIDTH, FINAL_HEIGHT = (
    28,
    28,
)  # Shape after resizing (for faster training, this will be feed into the network)

# Segregating the data
# Classes in the baseline CNN classifier:
# - yellow - figures with yellow faces, traditional lego minifigures. Some outliers with non-yellow faces will also occur.
# - skin color - figures with natural skin, mostly minifigures from films
# - other - duplo, random stuff that do not look like lego minifugures
# ! Warning: In categoies outliers can be found. In OTHER there are few normal lego minifigures, in SKIN are some figures that do not look like traditional lego minifigures (like Star Wars droids)
# ! This outliers aren't for now autimatically detected!

# Category names (needed for directory creation)
CATEGORY_NAMES = ["YELLOW", "SKIN", "OTHER"]

# List with categories belonging to the super-cateogry
YELLOW = [
    "vikings",
    "western",
    "world-racers" "universe",
    "ultra-agents",
    "train",
    "time-cruisers",
    "town",
    "the-lego-movie",
    "the-lego-ninjago-movie",
    "studios",
    "sports",
    "speed-champions",
    "space",
    "power-miners",
    "school-supplies",
    "promotional",
    "rock-raiders",
    "racers",
    "pharaoh-s-quest",
    "pirates",
    "monster-fighters",
    "monkie-kid",
    "legoland",
    "legoland-parks",
    "master-builder-academy",
    "minecraft",
    "lego-brand",
    "lego-ideas",
    "legends-of-chima",
    "bricklink-designer-program",
    "island-xtreme-stunts",
    "homemaker",
    "holiday-event",
    "hidden-side",
    "freestyle",
    "first-lego-league",
    "space",
    "speed-champions",
    "town",
    "educational-dacta",
    "dino",
    "dino-attack",
    "discovery",
    "collectible-minifigures",
    "adventurers",
    "agents",
    "alpha-team",
    "aquazone",
    "atlantis",
    "building-bigger-thinking",
    "castle",
    "nexo-knights",
    "ninja",
    "ninjago",
]
SKIN = [
    "the-lone-ranger",
    "the-hobbit-and-the-lord-of-the",
    "the-incredibles",
    "teenage-mutant-ninja-turtles",
    "super-heroes",
    "star-wars",
    "stranger-things",
    "speed-racer",
    "spider-man",
    "scooby-doo",
    "queer-eye",
    "prince-of-persia",
    "pirates-of-the-caribbean",
    "overwatch",
    "horizon",
    "back-to-the-future",
    "jurassic-world",
    "ghostbusters",
    "fusion",
    "friends-tv-series",
    "avatar",
    "avatar-the-last-airbender",
    "batman-i",
    "harry-potter",
    "indiana-jones",
    "dimensions",
]
OTHER = [
    "vidiyo",
    "unikitty!",
    "trolls-world-tour",
    "toy-story",
    "the-powerpuff-girls",
    "the-simpsons",
    "the-angry-birds-movie",
    "technic",
    "super-mario",
    "spongebob-squarepants",
    "sonic-the-hedgehog",
    "scala",
    "quatro",
    "primo",
    "minions-the-rise-of-gru",
    "hero-factory",
    "games",
    "gabby-s-dollhouse",
    "friends",
    "for-juniors",
    "fabuland",
    "exo-force",
    "disney",
    "disney's-mickey-mouse",
    "disney-s-mickey-mouse",
    "dreamzzz",
    "duplo",
    "dc-super-hero-girls",
    "basic",
    "belville",
    "bionicle",
    "elves",
    "cars",
    "clikits",
]

# Paths
RAW_DATASET_PATH = "./dataset"  # Path to images scraped form Internet splitted into categories used on the website
DESTINATION_PATH = "./preprocessed_dataset"  # Path to dataset with cropped and scaled images splitted into 3 classes (yellow, skin, other)

# Number of images in dataset
NUM_IMAGES_RAW = 14999

PREPROCESSED_CATEGORIES = []


# Shape of images
CROP_WIDTH, CROP_HEIGHT = 310, 310  # Shape after cropping
FINAL_WIDTH, FINAL_HEIGHT = (
    28,
    28,
)  # Shape after resizing (for faster training, this will be feed into the network)

# Segregating the data
# Classes in the baseline CNN classifier:
# - yellow - figures with yellow faces, traditional lego minifigures. Some outliers with non-yellow faces will also occur.
# - skin color - figures with natural skin, mostly minifigures from films
# - other - duplo, random stuff that do not look like lego minifugures
# ! Warning: In categoies outliers can be found. In OTHER there are few normal lego minifigures, in SKIN are some figures that do not look like traditional lego minifigures (like Star Wars droids)
# ! This outliers aren't for now autimatically detected!

# Category names (needed for directory creation)
CATEGORY_NAMES = ["YELLOW", "SKIN", "OTHER"]

# List with categories belonging to the super-cateogry
YELLOW = [
    "vikings",
    "western",
    "world-racers" "universe",
    "ultra-agents",
    "train",
    "time-cruisers",
    "town",
    "the-lego-movie",
    "the-lego-ninjago-movie",
    "studios",
    "sports",
    "speed-champions",
    "space",
    "power-miners",
    "school-supplies",
    "promotional",
    "rock-raiders",
    "racers",
    "pharaoh-s-quest",
    "pirates",
    "monster-fighters",
    "monkie-kid",
    "legoland",
    "legoland-parks",
    "master-builder-academy",
    "minecraft",
    "lego-brand",
    "lego-ideas",
    "legends-of-chima",
    "bricklink-designer-program",
    "island-xtreme-stunts",
    "homemaker",
    "holiday-event",
    "hidden-side",
    "freestyle",
    "first-lego-league",
    "space",
    "speed-champions",
    "town",
    "educational-dacta",
    "dino",
    "dino-attack",
    "discovery",
    "collectible-minifigures",
    "adventurers",
    "agents",
    "alpha-team",
    "aquazone",
    "atlantis",
    "building-bigger-thinking",
    "castle",
    "nexo-knights",
    "ninja",
    "ninjago",
]
SKIN = [
    "the-lone-ranger",
    "the-hobbit-and-the-lord-of-the",
    "the-incredibles",
    "teenage-mutant-ninja-turtles",
    "super-heroes",
    "star-wars",
    "stranger-things",
    "speed-racer",
    "spider-man",
    "scooby-doo",
    "queer-eye",
    "prince-of-persia",
    "pirates-of-the-caribbean",
    "overwatch",
    "horizon",
    "back-to-the-future",
    "jurassic-world",
    "ghostbusters",
    "fusion",
    "friends-tv-series",
    "avatar",
    "avatar-the-last-airbender",
    "batman-i",
    "harry-potter",
    "indiana-jones",
    "dimensions",
]
OTHER = [
    "vidiyo",
    "unikitty!",
    "trolls-world-tour",
    "toy-story",
    "the-powerpuff-girls",
    "the-simpsons",
    "the-angry-birds-movie",
    "technic",
    "super-mario",
    "spongebob-squarepants",
    "sonic-the-hedgehog",
    "scala",
    "quatro",
    "primo",
    "minions-the-rise-of-gru",
    "hero-factory",
    "games",
    "gabby-s-dollhouse",
    "friends",
    "for-juniors",
    "fabuland",
    "exo-force",
    "disney",
    "disney's-mickey-mouse",
    "disney-s-mickey-mouse",
    "dreamzzz",
    "duplo",
    "dc-super-hero-girls",
    "basic",
    "belville",
    "bionicle",
    "elves",
    "cars",
    "clikits",
]
