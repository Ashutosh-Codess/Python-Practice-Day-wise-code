#Mobile Battery Drain Simulator
def battery_drain(drain_per_minute: int) -> int:
    battery: int = 100
    minutes: int = 0
    while battery > 0:
        battery -= drain_per_minute
        minutes += 1
    return minutes