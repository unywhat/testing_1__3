import click
import subprocess
from pathlib import Path
import os


@click.group()
def cli() -> None:
    pass


def is_hex_enabled() -> bool:
    if os.path.exists('.hex'):
        return True
    else:
        return False


@cli.command()
@click.argument("name")
def create(name: str) -> None:
    if is_hex_enabled():
        subprocess.run(["git", "init"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", "\"init\""], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["gh", "repo", "create", name, "--public", "--source=.", "--remote=origin", "--push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        click.echo("use 'hex init'")


@cli.command()
def init() -> None:
    Path.touch('.hex')
    click.echo("initialized hex")