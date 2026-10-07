def collect_emissions_data(emissions_data):
    return {
        "actual_emissions": {
            "co2_kg": emissions_data.emissions,
            "energy_kwh": emissions_data.energy_consumed,
            "emissions_rate": emissions_data.emissions_rate,
        },
        "energy": {
            "cpu_kwh": emissions_data.cpu_energy,
            "gpu_kwh": emissions_data.gpu_energy,
            "ram_kwh": emissions_data.ram_energy,
        },
        "power": {
            "cpu_watts": emissions_data.cpu_power,
            "gpu_watts": emissions_data.gpu_power,
            "ram_watts": emissions_data.ram_power,
        },
        "workload": {
            "duration_seconds": emissions_data.duration,
        },
        "machine": {
            "cpu": emissions_data.cpu_model,
            "gpu": emissions_data.gpu_model,
            "cpu_count": emissions_data.cpu_count,
            "gpu_count": emissions_data.gpu_count,
            "ram_total_gb": emissions_data.ram_total_size,
        },
        "location": {
            "country": emissions_data.country_name,
            "country_code": emissions_data.country_iso_code,
            "region": emissions_data.region,
            "latitude": emissions_data.latitude,
            "longitude": emissions_data.longitude,
        },
        "utilization": {
            "cpu_percent": emissions_data.cpu_utilization_percent,
            "gpu_percent": emissions_data.gpu_utilization_percent,
            "ram_percent": emissions_data.ram_utilization_percent,
            "ram_used_gb": emissions_data.ram_used_gb,
        },
        "environment": {
            "water_liters": emissions_data.water_consumed,
            "pue": emissions_data.pue,
            "wue": emissions_data.wue,
        },
    }