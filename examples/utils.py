import hashlib

twoe1984 = 2 ** 1984
emojis = (
    ('\U0001f609', 'WINKING_FACE'),
    ('\U0001f60d', 'SMILING_FACE_WITH_HEART_EYES'),
    ('\U0001f61b', 'FACE_WITH_TONGUE'),
    ('\U0001f62d', 'LOUDLY_CRYING_FACE'),
    ('\U0001f631', 'FACE_SCREAMING_IN_FEAR'),
    ('\U0001f621', 'POUTING_FACE'),
    ('\U0001f60e', 'SMILING_FACE_WITH_SUNGLASSES'),
    ('\U0001f634', 'SLEEPING_FACE'),
    ('\U0001f635', 'DIZZY_FACE'),
    ('\U0001f608', 'SMILING_FACE_WITH_HORNS'),
    ('\U0001f62c', 'GRIMACING_FACE'),
    ('\U0001f607', 'SMILING_FACE_WITH_HALO'),
    ('\U0001f60f', 'SMIRKING_FACE'),
    ('\U0001f46e', 'POLICE_OFFICER'),
    ('\U0001f477', 'CONSTRUCTION_WORKER'),
    ('\U0001f482', 'GUARD'),
    ('\U0001f476', 'BABY'),
    ('\U0001f468', 'MAN'),
    ('\U0001f469', 'WOMAN'),
    ('\U0001f474', 'OLD_MAN'),
    ('\U0001f475', 'OLD_WOMAN'),
    ('\U0001f63b', 'SMILING_CAT_FACE_WITH_HEART_EYES'),
    ('\U0001f63d', 'KISSING_CAT_FACE'),
    ('\U0001f640', 'WEARY_CAT_FACE'),
    ('\U0001f47a', 'GOBLIN'),
    ('\U0001f648', 'SEE_NO_EVIL_MONKEY'),
    ('\U0001f649', 'HEAR_NO_EVIL_MONKEY'),
    ('\U0001f64a', 'SPEAK_NO_EVIL_MONKEY'),
    ('\U0001f480', 'SKULL'),
    ('\U0001f47d', 'ALIEN'),
    ('\U0001f4a9', 'PILE_OF_POO'),
    ('\U0001f525', 'FIRE'),
    ('\U0001f4a5', 'COLLISION'),
    ('\U0001f4a4', 'ZZZ'),
    ('\U0001f442', 'EAR'),
    ('\U0001f440', 'EYES'),
    ('\U0001f443', 'NOSE'),
    ('\U0001f445', 'TONGUE'),
    ('\U0001f444', 'MOUTH'),
    ('\U0001f44d', 'THUMBS_UP'),
    ('\U0001f44e', 'THUMBS_DOWN'),
    ('\U0001f44c', 'OK_HAND'),
    ('\U0001f44a', 'ONCOMING_FIST'),
    ('\u270c', 'VICTORY_HAND'),
    ('\u270b', 'RAISED_HAND'),
    ('\U0001f450', 'OPEN_HANDS'),
    ('\U0001f446', 'BACKHAND_INDEX_POINTING_UP'),
    ('\U0001f447', 'BACKHAND_INDEX_POINTING_DOWN'),
    ('\U0001f449', 'BACKHAND_INDEX_POINTING_RIGHT'),
    ('\U0001f448', 'BACKHAND_INDEX_POINTING_LEFT'),
    ('\U0001f64f', 'FOLDED_HANDS'),
    ('\U0001f44f', 'CLAPPING_HANDS'),
    ('\U0001f4aa', 'FLEXED_BICEPS'),
    ('\U0001f6b6', 'PERSON_WALKING'),
    ('\U0001f3c3', 'PERSON_RUNNING'),
    ('\U0001f483', 'WOMAN_DANCING'),
    ('\U0001f46b', 'MAN_AND_WOMAN_HOLDING_HANDS'),
    ('\U0001f46a', 'FAMILY'),
    ('\U0001f46c', 'TWO_MEN_HOLDING_HANDS'),
    ('\U0001f46d', 'TWO_WOMEN_HOLDING_HANDS'),
    ('\U0001f485', 'NAIL_POLISH'),
    ('\U0001f3a9', 'TOP_HAT'),
    ('\U0001f451', 'CROWN'),
    ('\U0001f452', 'WOMAN_S_HAT'),
    ('\U0001f45f', 'RUNNING_SHOE'),
    ('\U0001f45e', 'MAN_S_SHOE'),
    ('\U0001f460', 'HIGH_HEELED_SHOE'),
    ('\U0001f455', 'T_SHIRT'),
    ('\U0001f457', 'DRESS'),
    ('\U0001f456', 'JEANS'),
    ('\U0001f459', 'BIKINI'),
    ('\U0001f45c', 'HANDBAG'),
    ('\U0001f453', 'GLASSES'),
    ('\U0001f380', 'RIBBON'),
    ('\U0001f484', 'LIPSTICK'),
    ('\U0001f49b', 'YELLOW_HEART'),
    ('\U0001f499', 'BLUE_HEART'),
    ('\U0001f49c', 'PURPLE_HEART'),
    ('\U0001f49a', 'GREEN_HEART'),
    ('\U0001f48d', 'RING'),
    ('\U0001f48e', 'GEM_STONE'),
    ('\U0001f436', 'DOG_FACE'),
    ('\U0001f43a', 'WOLF_FACE'),
    ('\U0001f431', 'CAT_FACE'),
    ('\U0001f42d', 'MOUSE_FACE'),
    ('\U0001f439', 'HAMSTER_FACE'),
    ('\U0001f430', 'RABBIT_FACE'),
    ('\U0001f438', 'FROG_FACE'),
    ('\U0001f42f', 'TIGER_FACE'),
    ('\U0001f428', 'KOALA'),
    ('\U0001f43b', 'BEAR_FACE'),
    ('\U0001f437', 'PIG_FACE'),
    ('\U0001f42e', 'COW_FACE'),
    ('\U0001f417', 'BOAR'),
    ('\U0001f434', 'HORSE_FACE'),
    ('\U0001f411', 'EWE'),
    ('\U0001f418', 'ELEPHANT'),
    ('\U0001f43c', 'PANDA_FACE'),
    ('\U0001f427', 'PENGUIN'),
    ('\U0001f425', 'FRONT_FACING_BABY_CHICK'),
    ('\U0001f414', 'CHICKEN'),
    ('\U0001f40d', 'SNAKE'),
    ('\U0001f422', 'TURTLE'),
    ('\U0001f41b', 'BUG'),
    ('\U0001f41d', 'HONEYBEE'),
    ('\U0001f41c', 'ANT'),
    ('\U0001f41e', 'LADY_BEETLE'),
    ('\U0001f40c', 'SNAIL'),
    ('\U0001f419', 'OCTOPUS'),
    ('\U0001f41a', 'SPIRAL_SHELL'),
    ('\U0001f41f', 'FISH'),
    ('\U0001f42c', 'DOLPHIN'),
    ('\U0001f40b', 'WHALE'),
    ('\U0001f410', 'GOAT'),
    ('\U0001f40a', 'CROCODILE'),
    ('\U0001f42b', 'TWO_HUMP_CAMEL'),
    ('\U0001f340', 'FOUR_LEAF_CLOVER'),
    ('\U0001f339', 'ROSE'),
    ('\U0001f33b', 'SUNFLOWER'),
    ('\U0001f341', 'MAPLE_LEAF'),
    ('\U0001f33e', 'SHEAF_OF_RICE'),
    ('\U0001f344', 'MUSHROOM'),
    ('\U0001f335', 'CACTUS'),
    ('\U0001f334', 'PALM_TREE'),
    ('\U0001f333', 'DECIDUOUS_TREE'),
    ('\U0001f31e', 'SUN_WITH_FACE'),
    ('\U0001f31a', 'NEW_MOON_FACE'),
    ('\U0001f319', 'CRESCENT_MOON'),
    ('\U0001f30e', 'GLOBE_SHOWING_AMERICAS'),
    ('\U0001f30b', 'VOLCANO'),
    ('\u26a1', 'HIGH_VOLTAGE'),
    ('\u2614', 'UMBRELLA_WITH_RAIN_DROPS'),
    ('\u2744', 'SNOWFLAKE'),
    ('\u26c4', 'SNOWMAN_WITHOUT_SNOW'),
    ('\U0001f300', 'CYCLONE'),
    ('\U0001f308', 'RAINBOW'),
    ('\U0001f30a', 'WATER_WAVE'),
    ('\U0001f393', 'GRADUATION_CAP'),
    ('\U0001f386', 'FIREWORKS'),
    ('\U0001f383', 'JACK_O_LANTERN'),
    ('\U0001f47b', 'GHOST'),
    ('\U0001f385', 'SANTA_CLAUS'),
    ('\U0001f384', 'CHRISTMAS_TREE'),
    ('\U0001f381', 'WRAPPED_GIFT'),
    ('\U0001f388', 'BALLOON'),
    ('\U0001f52e', 'CRYSTAL_BALL'),
    ('\U0001f3a5', 'MOVIE_CAMERA'),
    ('\U0001f4f7', 'CAMERA'),
    ('\U0001f4bf', 'OPTICAL_DISK'),
    ('\U0001f4bb', 'LAPTOP_COMPUTER'),
    ('\u260e', 'TELEPHONE'),
    ('\U0001f4e1', 'SATELLITE_ANTENNA'),
    ('\U0001f4fa', 'TELEVISION'),
    ('\U0001f4fb', 'RADIO'),
    ('\U0001f509', 'SPEAKER_MEDIUM_VOLUME'),
    ('\U0001f514', 'BELL'),
    ('\u23f3', 'HOURGLASS_NOT_DONE'),
    ('\u23f0', 'ALARM_CLOCK'),
    ('\u231a', 'WATCH'),
    ('\U0001f512', 'LOCKED'),
    ('\U0001f511', 'KEY'),
    ('\U0001f50e', 'MAGNIFYING_GLASS_TILTED_RIGHT'),
    ('\U0001f4a1', 'LIGHT_BULB'),
    ('\U0001f526', 'FLASHLIGHT'),
    ('\U0001f50c', 'ELECTRIC_PLUG'),
    ('\U0001f50b', 'BATTERY'),
    ('\U0001f6bf', 'SHOWER'),
    ('\U0001f6bd', 'TOILET'),
    ('\U0001f527', 'WRENCH'),
    ('\U0001f528', 'HAMMER'),
    ('\U0001f6aa', 'DOOR'),
    ('\U0001f6ac', 'CIGARETTE'),
    ('\U0001f4a3', 'BOMB'),
    ('\U0001f52b', 'PISTOL'),
    ('\U0001f52a', 'KITCHEN_KNIFE'),
    ('\U0001f48a', 'PILL'),
    ('\U0001f489', 'SYRINGE'),
    ('\U0001f4b0', 'MONEY_BAG'),
    ('\U0001f4b5', 'DOLLAR_BANKNOTE'),
    ('\U0001f4b3', 'CREDIT_CARD'),
    ('\u2709', 'ENVELOPE'),
    ('\U0001f4eb', 'CLOSED_MAILBOX_WITH_RAISED_FLAG'),
    ('\U0001f4e6', 'PACKAGE'),
    ('\U0001f4c5', 'CALENDAR'),
    ('\U0001f4c1', 'FILE_FOLDER'),
    ('\u2702', 'SCISSORS'),
    ('\U0001f4cc', 'PUSHPIN'),
    ('\U0001f4ce', 'PAPERCLIP'),
    ('\u2712', 'BLACK_NIB'),
    ('\u270f', 'PENCIL'),
    ('\U0001f4d0', 'TRIANGULAR_RULER'),
    ('\U0001f4da', 'BOOKS'),
    ('\U0001f52c', 'MICROSCOPE'),
    ('\U0001f52d', 'TELESCOPE'),
    ('\U0001f3a8', 'ARTIST_PALETTE'),
    ('\U0001f3ac', 'CLAPPER_BOARD'),
    ('\U0001f3a4', 'MICROPHONE'),
    ('\U0001f3a7', 'HEADPHONE'),
    ('\U0001f3b5', 'MUSICAL_NOTE'),
    ('\U0001f3b9', 'MUSICAL_KEYBOARD'),
    ('\U0001f3bb', 'VIOLIN'),
    ('\U0001f3ba', 'TRUMPET'),
    ('\U0001f3b8', 'GUITAR'),
    ('\U0001f47e', 'ALIEN_MONSTER'),
    ('\U0001f3ae', 'VIDEO_GAME'),
    ('\U0001f0cf', 'JOKER'),
    ('\U0001f3b2', 'GAME_DIE'),
    ('\U0001f3af', 'DIRECT_HIT'),
    ('\U0001f3c8', 'AMERICAN_FOOTBALL'),
    ('\U0001f3c0', 'BASKETBALL'),
    ('\u26bd', 'SOCCER_BALL'),
    ('\u26be', 'BASEBALL'),
    ('\U0001f3be', 'TENNIS'),
    ('\U0001f3b1', 'POOL_8_BALL'),
    ('\U0001f3c9', 'RUGBY_FOOTBALL'),
    ('\U0001f3b3', 'BOWLING'),
    ('\U0001f3c1', 'CHEQUERED_FLAG'),
    ('\U0001f3c7', 'HORSE_RACING'),
    ('\U0001f3c6', 'TROPHY'),
    ('\U0001f3ca', 'PERSON_SWIMMING'),
    ('\U0001f3c4', 'PERSON_SURFING'),
    ('\u2615', 'HOT_BEVERAGE'),
    ('\U0001f37c', 'BABY_BOTTLE'),
    ('\U0001f37a', 'BEER_MUG'),
    ('\U0001f377', 'WINE_GLASS'),
    ('\U0001f374', 'FORK_AND_KNIFE'),
    ('\U0001f355', 'PIZZA'),
    ('\U0001f354', 'HAMBURGER'),
    ('\U0001f35f', 'FRENCH_FRIES'),
    ('\U0001f357', 'POULTRY_LEG'),
    ('\U0001f371', 'BENTO_BOX'),
    ('\U0001f35a', 'COOKED_RICE'),
    ('\U0001f35c', 'STEAMING_BOWL'),
    ('\U0001f361', 'DANGO'),
    ('\U0001f373', 'COOKING'),
    ('\U0001f35e', 'BREAD'),
    ('\U0001f369', 'DOUGHNUT'),
    ('\U0001f366', 'SOFT_ICE_CREAM'),
    ('\U0001f382', 'BIRTHDAY_CAKE'),
    ('\U0001f370', 'SHORTCAKE'),
    ('\U0001f36a', 'COOKIE'),
    ('\U0001f36b', 'CHOCOLATE_BAR'),
    ('\U0001f36d', 'LOLLIPOP'),
    ('\U0001f36f', 'HONEY_POT'),
    ('\U0001f34e', 'RED_APPLE'),
    ('\U0001f34f', 'GREEN_APPLE'),
    ('\U0001f34a', 'TANGERINE'),
    ('\U0001f34b', 'LEMON'),
    ('\U0001f352', 'CHERRIES'),
    ('\U0001f347', 'GRAPES'),
    ('\U0001f349', 'WATERMELON'),
    ('\U0001f353', 'STRAWBERRY'),
    ('\U0001f351', 'PEACH'),
    ('\U0001f34c', 'BANANA'),
    ('\U0001f350', 'PEAR'),
    ('\U0001f34d', 'PINEAPPLE'),
    ('\U0001f346', 'EGGPLANT'),
    ('\U0001f345', 'TOMATO'),
    ('\U0001f33d', 'EAR_OF_CORN'),
    ('\U0001f3e1', 'HOUSE_WITH_GARDEN'),
    ('\U0001f3e5', 'HOSPITAL'),
    ('\U0001f3e6', 'BANK'),
    ('\u26ea', 'CHURCH'),
    ('\U0001f3f0', 'CASTLE'),
    ('\u26fa', 'TENT'),
    ('\U0001f3ed', 'FACTORY'),
    ('\U0001f5fb', 'MOUNT_FUJI'),
    ('\U0001f5fd', 'STATUE_OF_LIBERTY'),
    ('\U0001f3a0', 'CAROUSEL_HORSE'),
    ('\U0001f3a1', 'FERRIS_WHEEL'),
    ('\u26f2', 'FOUNTAIN'),
    ('\U0001f3a2', 'ROLLER_COASTER'),
    ('\U0001f6a2', 'SHIP'),
    ('\U0001f6a4', 'SPEEDBOAT'),
    ('\u2693', 'ANCHOR'),
    ('\U0001f680', 'ROCKET'),
    ('\u2708', 'AIRPLANE'),
    ('\U0001f681', 'HELICOPTER'),
    ('\U0001f682', 'LOCOMOTIVE'),
    ('\U0001f68b', 'TRAM_CAR'),
    ('\U0001f68e', 'TROLLEYBUS'),
    ('\U0001f68c', 'BUS'),
    ('\U0001f699', 'SPORT_UTILITY_VEHICLE'),
    ('\U0001f697', 'AUTOMOBILE'),
    ('\U0001f695', 'TAXI'),
    ('\U0001f69b', 'ARTICULATED_LORRY'),
    ('\U0001f6a8', 'POLICE_CAR_LIGHT'),
    ('\U0001f694', 'ONCOMING_POLICE_CAR'),
    ('\U0001f692', 'FIRE_ENGINE'),
    ('\U0001f691', 'AMBULANCE'),
    ('\U0001f6b2', 'BICYCLE'),
    ('\U0001f6a0', 'MOUNTAIN_CABLEWAY'),
    ('\U0001f69c', 'TRACTOR'),
    ('\U0001f6a6', 'VERTICAL_TRAFFIC_LIGHT'),
    ('\u26a0', 'WARNING'),
    ('\U0001f6a7', 'CONSTRUCTION'),
    ('\u26fd', 'FUEL_PUMP'),
    ('\U0001f3b0', 'SLOT_MACHINE'),
    ('\U0001f5ff', 'MOAI'),
    ('\U0001f3aa', 'CIRCUS_TENT'),
    ('\U0001f3ad', 'PERFORMING_ARTS'),
    ('\U0001f1ef\\U0001f1f5', 'JAPAN'),
    ('\U0001f1f0\\U0001f1f7', 'SOUTH_KOREA'),
    ('\U0001f1e9\\U0001f1ea', 'GERMANY'),
    ('\U0001f1e8\\U0001f1f3', 'CHINA'),
    ('\U0001f1fa\\U0001f1f8', 'UNITED_STATES'),
    ('\U0001f1eb\\U0001f1f7', 'FRANCE'),
    ('\U0001f1ea\\U0001f1f8', 'SPAIN'),
    ('\U0001f1ee\\U0001f1f9', 'ITALY'),
    ('\U0001f1f7\\U0001f1fa', 'RUSSIA'),
    ('\U0001f1ec\\U0001f1e7', 'UNITED_KINGDOM'),
    ('1\u20e3', 'KEYCAP_ONE'),
    ('2\u20e3', 'KEYCAP_TWO'),
    ('3\u20e3', 'KEYCAP_THREE'),
    ('4\u20e3', 'KEYCAP_FOUR'),
    ('5\u20e3', 'KEYCAP_FIVE'),
    ('6\u20e3', 'KEYCAP_SIX'),
    ('7\u20e3', 'KEYCAP_SEVEN'),
    ('8\u20e3', 'KEYCAP_EIGHT'),
    ('9\u20e3', 'KEYCAP_NINE'),
    ('0\u20e3', 'KEYCAP_ZERO'),
    ('\U0001f51f', 'KEYCAP_10'),
    ('\u2757', 'EXCLAMATION_MARK'),
    ('\u2753', 'QUESTION_MARK'),
    ('\u2665', 'HEART_SUIT'),
    ('\u2666', 'DIAMOND_SUIT'),
    ('\U0001f4af', 'HUNDRED_POINTS'),
    ('\U0001f517', 'LINK'),
    ('\U0001f531', 'TRIDENT_EMBLEM'),
    ('\U0001f534', 'RED_CIRCLE'),
    ('\U0001f535', 'BLUE_CIRCLE'),
    ('\U0001f536', 'LARGE_ORANGE_DIAMOND'),
    ('\U0001f537', 'LARGE_BLUE_DIAMOND'),
)


def integer_to_bytes(integer):
    return int.to_bytes(
        integer,
        length=(integer.bit_length() + 8 - 1) // 8,  # 8 bits per byte,
        byteorder='big',
        signed=False
    )


def calc_fingerprint(key):
    return int.from_bytes(
        bytes(hashlib.sha1(key).digest()[-8:]), 'little', signed=True
    )


def check_g(g_a, p):
    if not (1 < g_a < p - 1):
        raise RuntimeError('g_a is invalid (1 < g_a < p - 1 is false)')
    if not (twoe1984 < g_a < p - twoe1984):
        raise RuntimeError('g_a is invalid (2^1984 < g_a < p - 2^1984 is false)')


def generate_visualization(part1, part2):
    visualization = []
    visualization_text = []
    vis_src = hashlib.sha256(part1 + part2).digest()
    for i in range(0, len(vis_src), 8):
        number = vis_src[i:i+8]
        number = integer_to_bytes(number[0] & 0x7f) + number[1:]
        idx = int.from_bytes(number, 'big') % len(emojis)
        visualization.append(emojis[idx][0])
        visualization_text.append(emojis[idx][1])
    print(', '.join(visualization_text))
    return visualization
