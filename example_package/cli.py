"""Console script for example_package."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("example-package")
    click.echo("=" * len("example-package"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
