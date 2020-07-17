from pathlib import Path

from src.parse import itemize_log, parse_itemized_log, parse_item, process_log

__file_path = Path(__file__).parent.absolute()

with open(__file_path / "chatlog_single_item.log", "r") as f:
    chatlog_single_item_txt = f.readlines()

with open(__file_path / "chatlog_three_items.log", "r") as f:
    chatlog_three_items_txt = f.readlines()


def test_itemize_log(txt=chatlog_single_item_txt):
    assert itemize_log(chatlog_three_items_txt) is not None


def test_parse_itemized_log(txt=chatlog_single_item_txt):
    itemized_log = itemize_log(txt)
    parsed_itemized_log = parse_itemized_log(itemized_log)
    assert parsed_itemized_log is not None


def test_parse_item(txt=chatlog_single_item_txt):
    itemized_log = itemize_log(txt)
    res = parse_item(itemized_log["items"][0])
    exp = {
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

    assert res == exp


def test_process_log(log=chatlog_three_items_txt):
    res = process_log(log)
    exp = {
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

    assert res == exp
