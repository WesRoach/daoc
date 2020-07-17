import pytest


@pytest.fixture(scope="session")
def parsed_item():
    return {
        "magical_bonuses": {
            "dexterity": "10",
            "constitution": "9",
            "quickness": "1",
            "slash": "5",
            "parry": "2",
            "all_melee_weapon_skills": "1",
        },
        "item_name": "Edgebender Arcanium Exceptional Moon Claw",
        "total_utility": "43.333",
        "single_skill_utility": "38.333",
    }



@pytest.fixture(scope="session")
def parsed_log():
    return {
        "items": [
            {
                "magical_bonuses": {
                    "strength": "11",
                    "quickness": "10",
                    "hits": "28",
                    "cold": "4",
                    "crush": "1",
                    "slash": "1",
                    "thrust": "3",
                    "shields": "1",
                    "all_melee_weapon_skills": "2",
                },
                "item_name": "Slapping Supreme Ring",
                "total_utility": "64",
                "single_skill_utility": "54",
            },
            {
                "magical_bonuses": {
                    "strength": "30",
                    "body": "9",
                    "thrust": "8",
                },
                "item_name": "Tuscarian Ring of Might",
                "total_utility": "54",
            },
            {
                "magical_bonuses": {
                    "dexterity": "13",
                    "quickness": "13",
                    "crush": "1",
                    "energy": "5",
                    "heat": "5",
                    "all_melee_weapon_skills": "1",
                    "all_archery_skills": "1",
                },
                "item_name": "Adroit Supreme Necklace",
                "total_utility": "54.333",
                "single_skill_utility": "49.333",
            },
        ]
    }
