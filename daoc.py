from pathlib import Path

import click

from src.parse import process_log, log_items_to_loki


@click.group()
def cli():
    pass


@click.group()
def parse():
    """
    Parse a chatlog.
    """
    pass


@click.command()
@click.option("chatlog_path", "--chatlog", prompt=True)
@click.option("out_path", "--out", prompt=True)
@click.option(
    "--realm",
    prompt=True,
    type=click.Choice(["Midgard", "Hibernia", "Albion"], case_sensitive=False),
)
@click.option(
    "--to",
    prompt=True,
    default="LOKI",
    show_default=True,
    type=click.Choice(["LOKI", "Korts"], case_sensitive=False),
    show_choices=True,
)
def items(chatlog_path, out_path, to, realm):
    """
    Parse chatlog items into LOKI format.
    """
    chatlog_path = Path(chatlog_path).absolute()
    out_path = Path(out_path).absolute()
    click.echo(f"Parsing: {chatlog_path.as_posix()}")
    click.echo(f"Writing items into {out_path.as_posix()}")

    processed_log = process_log(chatlog_path)

    if to.lower() == "loki":
        log_items_to_loki(processed_log, out_path)


cli.add_command(parse)
parse.add_command(items)

# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
# def cli(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo("Hello %s!" % name)
