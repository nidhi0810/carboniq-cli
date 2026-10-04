import typer
from .tracker import track_command

app = typer.Typer()


@app.command()
def run(command: list[str] = typer.Argument(...)):
    print(f"Running: {' '.join(command)}")

    result, emissions = track_command(command)

    print(f"Emissions: {emissions} kg CO₂")

    if result.returncode != 0:
        print(f"Program exited with code {result.returncode}")


@app.command()
def analyze():
    print("Carbon analysis coming soon...")


@app.command()
def forecast():
    print("Carbon forecast coming soon...")


@app.command()
def history():
    print("Carbon history coming soon...")


if __name__ == "__main__":
    app()