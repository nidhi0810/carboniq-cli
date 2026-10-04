import subprocess
from codecarbon import EmissionsTracker


def track_command(command: list[str]):
    tracker = EmissionsTracker()

    tracker.start()

    result = subprocess.run(command)

    emissions = tracker.stop()

    return result, emissions