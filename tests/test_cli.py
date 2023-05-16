from importlib.metadata import version

from click.testing import CliRunner

from roam_research_to_sqlite import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["--version"])
    assert result.exit_code == 0
    assert (
        result.output == f"cli, version {version('roam_research_to_sqlite')}\n"
    )
