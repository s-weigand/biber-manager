"""Console script for biber."""
import typer

app = typer.Typer()


@app.command()
def main(args=None) -> int:
    """Console script for biber.

    Parameters
    ----------
    args : list, optional
        Commandlineargs, by default None

    Returns
    -------
    int
        Returncode
    """
    typer.echo("Replace this message by putting your code into " "biber_manager.cli.main")
    typer.echo("See click documentation at https://typer.tiangolo.com/")
    return 0


if __name__ == "__main__":
    app()
