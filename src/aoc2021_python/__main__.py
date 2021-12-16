"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Avent of Code 2021 - Python."""


if __name__ == "__main__":
    main(prog_name="aoc2021-python")  # pragma: no cover
