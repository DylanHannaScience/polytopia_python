# polytopia_score_counter/actions.py

# List of valid actions for reference
ACTIONS = [
    "train_unit",
    "lose_unit",
    "upgrade_city",
    "place_structure",
    "capture_city",
    "lose_city",
    "gain_territory",
    "lose_territory",
    "research_tech",
    "discover_fog",
    "park",
]

_2D_ACTIONS = [
    {"action": "train_unit", "unit_type": "archer"},
    {"action": "lose_unit", "unit_type": "warrior"},
    {"action": "upgrade_city", "city_population_gain": 3},
    {"action": "place_structure", "structure": "monument"},
    {"action": "capture_city", "city_population_gain": 1},
    {"action": "lose_city", "city_population_loss": 2},
    {"action": "gain_territory"},
    {"action": "lose_territory"},
    {"action": "research_tech", "tech_tier": 1},
    {"action": "research_tech", "tech_tier": 2},
    {"action": "research_tech", "tech_tier": 3},
    {"action": "discover_fog"},
    {"action": "park"},
]
