from src.loki import fill_template, guess_location, slots_from_item


def itemize_log(log_text):
    """
    Returns dict containing sections of the log, organized into categories.

    Returns:
    {
        "items": [],
    }
    """
    # stored stores finished items from buffer
    stored = {"items": []}

    logging = False
    for line in log_text:
        if logging is False:
            # buffer will store interested sections of the log as we're
            # rolling through the log
            buffer = []

        if "<Begin Info:" in line:
            logging = True

        if logging is True:
            buffer.append(line)

        if "<End Info>" in line:
            logging = False
            stored["items"].append(buffer)

    return stored


def parse_itemized_log(itemized_log):
    """
    Given itemized log - return dict of categories.
    """
    # parsed items will parse values from each stored["items"][:] into kv dict
    parsed = {"items": []}
    for item in itemized_log["items"]:
        parsed["items"].append(parse_item(item))

    return parsed


def parse_item(item):
    """
    Given list of text from log - return dict of item kv pairs.
    """
    item_buffer = {"magical_bonuses": {}}
    processing_bonuses = False
    for line in item:
        if len(line) <= 13:
            processing_bonuses = False
            continue
        if "<Begin Info:" in line:
            item_buffer["item_name"] = line[24:-2]
            continue
        if "Total Utility" in line:
            item_buffer["total_utility"] = line[26:-1]
            continue
        if "Single Skill Utility" in line:
            item_buffer["single_skill_utility"] = line[33:-1]
            continue
        if "Magical Bonuses" in line:
            processing_bonuses = True
            continue

        if processing_bonuses and len(line) > 13:
            idx_stat_start = line.find("|") + 2
            idx_stat_end = line.find("+") - 2
            idx_bonus_start = line.find("+") + 1
            bonus_length = line[idx_bonus_start:].find(" ")

            stat = line[idx_stat_start:idx_stat_end].lower().replace(" ", "_")
            bonus = line[idx_bonus_start : idx_bonus_start + bonus_length]

            item_buffer["magical_bonuses"][stat] = bonus
            continue
        else:
            processing_bonuses = False

        if "<End Info>" in line:
            break

    return item_buffer


def convert_log_attributes(processed_log):
    # Handle "items" from log
    for item in processed_log["items"]:
        # Updated total_utility and single_skill_utility to int
        for k, v in item.items():
            if k in ("total_utility", "single_skill_utility"):
                item[k] = float(v)
        # update stat bonuses to int
        for stat, bonus in item["magical_bonuses"].items():
            item["magical_bonuses"][stat] = int(bonus)

    return processed_log


def process_log(log_text):
    """
    Return parsed log.
    """
    return convert_log_attributes(parse_itemized_log(itemize_log(log_text)))


def generate_file_name(item_name, iter):
    return item_name.replace(" ", "_") + "." + str(iter).zfill(2) + ".xml"


def log_items_to_loki(processed_log, realm, out_path):
    for item in processed_log["items"]:

        # some item names are duplicative - iterate of item name exists
        item_name = item["item_name"]
        item_name_iter = 1
        file_name = generate_file_name(item_name, item_name_iter)
        file_path = out_path / file_name

        while file_path.exists():
            item_name_iter += 1
            file_name = generate_file_name(item_name, item_name_iter)
            file_path = out_path / file_name

        item_template = fill_template(
            Location=guess_location(item_name),
            Realm=realm,
            ItemName=item_name,
            slots=slots_from_item(item),
        )

        file_path.write_text(item_template)
