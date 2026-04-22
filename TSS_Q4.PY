#Traffic Signal Simulator
def traffic_signal(time: int) -> str:
    t = (time - 1) % 90 + 1  
    for limit, color in {(30, "GREEN"), (60, "YELLOW"), (90, "RED")}:
        if t <= limit:
            return color
