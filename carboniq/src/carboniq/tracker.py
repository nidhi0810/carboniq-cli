import subprocess
from codecarbon import EmissionsTracker


def track_command(command: list[str]):
    tracker = EmissionsTracker()

    tracker.start()

    result = subprocess.run(command)

    tracker.stop()

    return result, tracker.final_emissions_data