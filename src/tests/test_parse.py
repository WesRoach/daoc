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


# def test_parse_item(parsed_item, txt=chatlog_single_item_txt):
#     itemized_log = itemize_log(txt)
#     res = parse_item(itemized_log["items"][0])

#     assert res == parsed_item


def test_process_log(parsed_log, log=chatlog_three_items_txt):
    res = process_log(log)

    assert res == parsed_log
