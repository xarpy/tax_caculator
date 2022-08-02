import json
import os
from pathlib import Path

import click
import pytest
from IPython import embed

from app import execute

BASE_DIR = Path(__file__).resolve().parent


class DefaultToStdin(click.Argument):
    """Click class conversion configuration"""

    def __init__(self, *args, **kwargs):
        kwargs["nargs"] = -1
        super().__init__(*args, **kwargs)

    def process_value(self, ctx, value):
        try:
            result = []
            for v in value:
                result.append(json.loads(v))
            return result
        except Exception:
            raise click.BadParameter(value)


@click.group()
def cli():
    pass


@click.command("calculate", short_help="Command to execute the system")
@click.argument("capital_gain", cls=DefaultToStdin)
def compile_command(capital_gain):
    click.echo(execute(capital_gain))


@click.command("runtest", short_help="Command to execute tests")
@click.option(
    "--list",
    is_flag=True,
    default=False,
    help="Obtain module tests list",
)
@click.option(
    "--node",
    "-n",
    help="Inform the module name and the function you want to run the tests",
)
def test_command(list, node):
    folder_path = os.path.join(BASE_DIR, "tests")
    if not os.path.exists(folder_path):
        print("There is no folder named tests anywhere!")
    if list:
        pytest.main(["--co"])
    if node:
        pytest.main(["-v", f"{folder_path}/{node}"])
    else:
        pytest.main(["-vv", "--cov=."])


@click.command("shell", short_help="Command to execute ipython shell")
def shell_command():
    embed(colors="neutral")


cli.add_command(compile_command)
cli.add_command(shell_command)
cli.add_command(test_command)

if __name__ == "__main__":
    cli()
