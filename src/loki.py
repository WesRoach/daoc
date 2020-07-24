from collections import namedtuple
from typing import List

TypeEffectTuple = namedtuple("TypeEffectTuple", ["Type", "Effect"])

# TODO: Add other parsed bonuses
parsed_bonus_to_effect_dict = {
    "strength": TypeEffectTuple("Stat", "Strength"),
    "dexterity": TypeEffectTuple("Stat", "Dexterity"),
    "constitution": TypeEffectTuple("Stat", "Constitution"),
    "quickness": TypeEffectTuple("Stat", "Quickness"),
    "piety": TypeEffectTuple("Stat", "Piety"),
    "charisma": TypeEffectTuple("Stat", "Charisma"),
    "hits": TypeEffectTuple("Stat", "Hits"),
    "power": TypeEffectTuple("Stat", "Power"),
    "crush": TypeEffectTuple("Resist", "Crush Resist"),
    "slash": TypeEffectTuple("Resist", "Slash Resist"),
    "thrust": TypeEffectTuple("Resist", "Thrust Resist"),
    "body": TypeEffectTuple("Resist", "Body Resist"),
    "spirit": TypeEffectTuple("Resist", "Spirit Resist"),
    "energy": TypeEffectTuple("Resist", "Energy Resist"),
    "matter": TypeEffectTuple("Resist", "Matter Resist"),
    "heat": TypeEffectTuple("Resist", "Heat Resist"),
    "cold": TypeEffectTuple("Resist", "Cold Resist"),
    "parry": TypeEffectTuple("Skill", "Parry"),
    "stealth": TypeEffectTuple("Skill", "Stealth"),
    "shields": TypeEffectTuple("Skill", "Shield"),
    "all_melee_weapon_skills": TypeEffectTuple(
        "Skill", "All Melee Skill Bonus"
    ),
    "all_dual_wielding_skills": TypeEffectTuple(
        "Skill", "All Dual Wield Skill Bonus"
    ),
    "all_archery_skills": TypeEffectTuple("Skill", "Archery Skill Bonus"),
}


class Slot:
    """
    Class defining an item Slot.

    An item Slot consists of:
        Type: (Stat, Resist, Skill, Cap Increase, Other Bonus, PvE)
        Effect: (Strength, Body Resist, Left Axe, ...)
        Amount: 1-Inf
    """

    def __init__(
        self,
        Remakes: int = 0,
        Effect: str = "",
        Qua: int = 99,
        Amount: int = 0,
        Done: int = 0,
        Time: int = 0,
        Type: str = "Unused",
    ):
        self.Remakes = Remakes
        self.Effect = Effect
        self.Qua = Qua
        self.Amount = Amount
        self.Done = Done
        self.Time = Time
        self.Type = Type


def parsed_bonus_to_slot(bonus, value):
    # bonus == "quickness" => (Type="Stat", Effect="Quickness")
    # value == 13 => (Amount=13)
    # Qua == 99 => (Qua=99)
    return Slot(
        Effect=parsed_bonus_to_effect_dict[bonus].Effect,
        Type=parsed_bonus_to_effect_dict[bonus].Type,
        Amount=value,
    )


def slots_from_item(item) -> List[Slot]:
    """
    Splits "magical_bonuses" from item into Slots

    Returns:
        list[Slot]
    """
    slots = [Slot() for x in range(0, 10)]

    for idx, bonus in enumerate(item["magical_bonuses"]):
        slots[idx] = Slot(
            Effect=parsed_bonus_to_effect_dict[bonus].Effect,
            Type=parsed_bonus_to_effect_dict[bonus].Type,
            Amount=item["magical_bonuses"][bonus],
        )

    return slots


item_locations = [
    "Head",
    "Hands",
    "Feet",
    "Chest",
    "Arms",
    "Legs",
    "Right Hand",
    "Left Hand",
    "2 Handed",
    "Neck",
    "Cloak",
    "Jewel",
    "Belt",
    "Right Ring",
    "Left Ring",
    "Right Wrist",
    "Left Wrist",
]

location_alias = [
    ("Head", "helm"),
    ("Hands", "gauntlets"),
    ("Feet", "boots"),
    ("Chest", "chest"),
    ("Chest", "hauberk"),
    ("Arms", "greaves"),
    ("Legs", "legs"),
    ("Right Hand", "greave"),
    ("Right Hand", "claw"),
    ("Neck", "neck"),
    ("Neck", "choker"),
    ("Neck", "medallion"),
    ("Cloak", "cloak"),
    ("Cloak", "mantle"),
    ("Jewel", "gem"),
    ("Jewel", "jewel"),
    ("Belt", "belt"),
    ("Right Ring", "ring"),
    ("Right Wrist", "bracer"),
    ("Right Wrist", "bracelet"),
    ("Right Wrist", "wrap"),
]


def guess_location(item_name: str):
    lower_name = item_name.lower()
    # Try to guess by name what Location the item is equipped in
    for alias in location_alias:
        if alias[1] in lower_name:
            return alias[0]
    try:
        return input(f"Location of {item_name}:\n" f"{item_locations}: ")
    except Exception:
        return ""


def fill_template(Location, Realm, ItemName, slots):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<SCItem>
    <ActiveState>drop</ActiveState>
    <Location>{Location}</Location>
    <Realm>{Realm}</Realm>
    <ItemName>{ItemName}</ItemName>
    <AFDPS>0.0</AFDPS>
    <Bonus>35</Bonus>
    <ItemQuality>100</ItemQuality>
    <Equipped>1</Equipped>
    <Level>51</Level>
    <OFFHAND>no</OFFHAND>
    <SOURCE>artifact</SOURCE>
    <DBSOURCE>LOKI</DBSOURCE>
    <CLASSRESTRICTIONS>
        <CLASS>All</CLASS>
    </CLASSRESTRICTIONS>
    <DROPITEM>
        <SLOT Number="0">
            <Remakes>0</Remakes>
            <Effect>{slots[0].Effect}</Effect>
            <Qua>{slots[0].Qua}</Qua>
            <Amount type="str">{slots[0].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[0].Type}</Type>
        </SLOT>
        <SLOT Number="1">
            <Remakes>0</Remakes>
            <Effect>{slots[1].Effect}</Effect>
            <Qua>{slots[1].Qua}</Qua>
            <Amount type="str">{slots[1].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[1].Type}</Type>
        </SLOT>
        <SLOT Number="2">
            <Remakes>0</Remakes>
            <Effect>{slots[2].Effect}</Effect>
            <Qua>{slots[2].Qua}</Qua>
            <Amount type="str">{slots[2].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[2].Type}</Type>
        </SLOT>
        <SLOT Number="3">
            <Remakes>0</Remakes>
            <Effect>{slots[3].Effect}</Effect>
            <Qua>{slots[3].Qua}</Qua>
            <Amount type="str">{slots[3].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[3].Type}</Type>
        </SLOT>
        <SLOT Number="4">
            <Remakes>0</Remakes>
            <Effect>{slots[4].Effect}</Effect>
            <Qua>{slots[4].Qua}</Qua>
            <Amount type="str">{slots[4].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[4].Type}</Type>
        </SLOT>
        <SLOT Number="5">
            <Remakes>0</Remakes>
            <Effect>{slots[5].Effect}</Effect>
            <Qua>{slots[5].Qua}</Qua>
            <Amount type="str">{slots[5].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[5].Type}</Type>
        </SLOT>
        <SLOT Number="6">
            <Remakes>0</Remakes>
            <Effect>{slots[6].Effect}</Effect>
            <Qua>{slots[6].Qua}</Qua>
            <Amount type="str">{slots[6].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[6].Type}</Type>
        </SLOT>
        <SLOT Number="7">
            <Remakes>0</Remakes>
            <Effect>{slots[7].Effect}</Effect>
            <Qua>{slots[7].Qua}</Qua>
            <Amount type="str">{slots[7].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[7].Type}</Type>
        </SLOT>
        <SLOT Number="8">
            <Remakes>0</Remakes>
            <Effect>{slots[8].Effect}</Effect>
            <Qua>{slots[8].Qua}</Qua>
            <Amount type="str">{slots[8].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[8].Type}</Type>
        </SLOT>
        <SLOT Number="9">
            <Remakes>0</Remakes>
            <Effect>{slots[9].Effect}</Effect>
            <Qua>{slots[9].Qua}</Qua>
            <Amount type="str">{slots[9].Amount}</Amount>
            <Done>0</Done>
            <Time>0</Time>
            <Type>{slots[9].Type}</Type>
        </SLOT>
    </DROPITEM>
</SCItem>
"""


# Unused atm
__base_dict = {
    "ActiveState": "drop",
    "Location": "Neck",
    "Realm": "Midgard",
    "ItemName": "Beaded Resisting Stones Test",
    "AFDPS": 0.0,
    "Bonus": 35,
    "ItemQuality": 100,
    "Equipped": 1,
    "Level": 51,
    "OFFHAND": "no",
    "SOURCE": "drop",
    "DBSOURCE": "LOKI",
    "CLASSRESTRICTIONS": {"CLASS": "All"},
    "ISUNIQUE": 0,
    "ORACLE_IGNORE": 0,
    "USER_VALUE": 0,
    "VARIANT": "",
    "ASSOCIATE": "",
    "EQUIPLIST": {"SLOT NAME": "Neck"},
    "DROPITEM": [
        {
            "Remakes": 0,
            "Effect": "Body Resist",
            "Qua": 99,
            "Amount": "10",
            "Done": 0,
            "Time": 0,
            "Type": "Resist",
        },
    ],
}

# Unused atm
# {Type: Effect}
# type_effect_dict["Stat"] >> {"Strength", ...}
__type_effect_dict = {
    "Stat": {
        "Strength",
        "Constitution",
        "Dexterity",
        "Quickness",
        "Intelligence",
        "Piety",
        "Charisma",
        "Empathy",
        "Hits",
        "Power",
        "Acuity",
    },
    "Resist": {
        "Body Resist",
        "Cold Resist",
        "Heat Resist",
        "Energy Resist",
        "Matter Resist",
        "Spirit Resist",
        "Crush Resist",
        "Thrust Resist",
        "Slash Resist",
    },
    "Skill": {
        "Augmentation",
        "Axe",
        "Battlesongs",
        "Beastcraft",
        "Bone Army",
        "Cave Magic",
        "Composite Bow",
        "Critical Strike",
        "Cursing",
        "Darkness",
        "Envenom",
        "Hammer",
        "Hand to Hand",
        "Hexing",
        "Left Axe",
        "Mending",
        "Odin's Will",
        "Pacification",
        "Parry",
        "Runecarving",
        "Savagery",
        "Shield",
        "Spear",
        "Staff",
        "Stealth",
        "Stormcalling",
        "Summoning",
        "Suppression",
        "Sword",
        "Thrown",
        "Witchcraft",
        "ALL magic skills",
        "ALL melee weapon skills",
        "ALL dual wielding skills",
        "ALL archery skills",
    },
    "Cap Increase": {
        "Strength",
        "Constitution",
        "Dexterity",
        "Quickness",
        "Intelligence",
        "Piety",
        "Charisma",
        "Empathy",
        "Hits",
        "Power",
        "Acuity",
    },
    "Other Bonus": {
        "Armour Factor",
        "Power Pool",
        "Debuff Effectiveness",
        "Buff Effectiveness",
        "Healing Effectiveness",
        "Spell Duration",
        "Casting Speed",
        "Spell Range",
        "Spell Damage",
        "Archery Damage",
        "Archery Range",
        "Archery Speed",
        "Style Damage",
        "Melee Damage",
        "Melee Combat Speed",
        "Fatigue",
        "Resist Pierce",
        "Death XP Loss",
        "Arrow Recovery",
    },
    "PvE": {
        "Bladeturn Reinforcement",
        "Spell Power Cost",
        "Blocking",
        "Defensive Bonus",
        "Evade",
        "Negative Effect Duration",
        "Parry",
        "Piece Ablative",
        "Reactionary Style Damage",
        "Style Cost Reduction",
        "To-Hit Bonus",
        "Concentration",
    },
    "Unused": {""},
}
