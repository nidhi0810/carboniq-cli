import json
import typer
from .tracker import track_command
from .carbonaware import get_forecast
from .collector import collect_emissions_data
app = typer.Typer()


@app.command()
def run(
    location: str = typer.Option(..., help="CarbonAware location"),
    command: list[str] = typer.Argument(...),
):
    print(f"Running: {' '.join(command)}")

    result, emissions_data = track_command(command)

    carboniq_data = collect_emissions_data(emissions_data)

    carbon_aware_data = get_forecast(location)

    carboniq_data["carbon_aware"] = carbon_aware_data

    print("\nCarbonIQ Data:")
    print(json.dumps(carboniq_data, indent=2))

    if result.returncode != 0:
        print(f"\nProgram exited with code {result.returncode}")


@app.command()
def analyze():
    print("Carbon analysis coming soon...")

@app.command()
def forecast(
    location: str = typer.Option(..., help="CarbonAware location"),
    window_size: int = typer.Option(30, help="Workload duration in minutes"),
):
    result = get_forecast(location, window_size)

    print(f"\nLocation: {result['location']}")
    print(f"Workload duration: {result['windowSize']} minutes")

    print("\nOptimal times:")

    for point in result["optimalDataPoints"]:
        print(
            f"  {point['timestamp']} "
            f"→ {point['value']} gCO₂/kWh"
        )

@app.command()
def history():
    print("Carbon history coming soon...")


if __name__ == "__main__":
    app()