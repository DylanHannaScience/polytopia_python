# polytopia_score_counter/rewards.py

# Star cost for common units
UNIT_STAR_COST = {
    "warrior": 2,
    "rider": 3,
    "archer": 3,
    "defender": 3,
    "swordsman": 5,
    "catapult": 8,
    "cloak": 8,
    "knight": 8,
    "giant": 10,
}


def calculate_reward(action, **kwargs):
    if action == "train_unit":
        unit_type = kwargs.get("unit_type", None)
        return 5 * UNIT_STAR_COST.get(unit_type, 0)

    if action == "lose_unit":
        unit_type = kwargs.get("unit_type", None)
        return -5 * UNIT_STAR_COST.get(unit_type, 0)

    if action == "upgrade_city":
        city_population_gain = kwargs.get("city_population_gain", 0)
        return 50 + (5 * city_population_gain)

    if action == "place_structure":
        structure = kwargs.get("structure", None)
        if structure == "monument":
            return 400

    if action == "capture_city":
        return 100

    if action == "lose_city":
        city_population_loss = kwargs.get("city_population_loss", 0)
        return -(50 + (5 * city_population_loss))

    if action == "gain_territory":
        return 20

    if action == "lose_territory":
        return -20

    if action == "research_tech":
        tech_tier = kwargs.get("tech_tier", 1)
        return 100 * tech_tier

    if action == "discover_fog":
        return 5

    if action == "park":
        return 250

    return 0  # Default reward for neutral actions
