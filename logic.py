#   Author: Hans van Lierop
#   Date: 2025-08-22

from machine import Pin
import utime # Relies on an RTC instead of OS time

menu_options = {
    "1": {
        "long": "find baud rate", 
        "short": "baud"
    }
}

def print_menu() -> None:
    """
    Prints the modes for the logic analyzer.
    """
    print("---Logic analyzer modes---")
    for mode_n, desc in menu_options.items():
        print(f"{mode_n}:  {desc["long"]}")


def get_input() -> str:
    """
    Gets a valid mode setting from the user.
    """
    try:
        print_menu()
        mode_n = input("Choose a mode: ")
        print()
        mode = menu_options[mode_n]["short"]
    except KeyError:
        print("invalid mode\n")
        mode = get_input()

    return mode

def handle_mode(mode) -> None:
    """
    Handles calling of functionality based on mode.
    """
    if mode == "baud":
        pins = {
            "GND": "GND",
            "GP0": "target pin"
        }
        idle_value = 1 # Can add logic depending on protocol (UART is 1, I2C is 0, etc.)
        baud_listen(idle_value)
    else:
        print("mode not found\n")

def baud_listen(idle_value: int):
    """
    Tracks edge gap durations of timing diagram.
    """
    n_samples = 10 # Number of edge samples to take

    target_pin = Pin(0, Pin.IN, idle_value) # Inputs to GP0
    
    print("Waiting for idle...")
    # Check for idle state
    while target_pin.value() == 0:
        utime.sleep_us(10)
    
    print("Idle detected. Waiting for edge...")
    # Wait for edge
    while target_pin.value() == idle_value:
        pass

    print("Edge detected. Collecting samples...")
    # Start time
    start_time = utime.ticks_us()
    edge_gap_durations = []
    level_value = ~idle_value
    # Collect edge samples
    for _ in range(n_samples+1):
        # Detect change in level
        while target_pin.value() == level_value:
            utime.sleep_us(100)
            pass
        # Next edge
        end_time = utime.ticks_us()
        # Append the gap duration
        edge_gap_durations.append(utime.ticks_diff(end_time, start_time))
        # Old end is the new start
        start_time = end_time
        level_value = ~level_value

    print(edge_gap_durations)

def baud_calculate(edge_gap_durations) -> int:
    """
    Calculates baud rate by finding the greatest common factor of edge gaps.
    """
    pass
    #calculated_baud_rate = 1 / bit_duration_gcf / 1_000_000 # Get baud rate per second

    common_rates = (19200)


    #return baud_rate

def main() -> int:
    try:
        mode = get_input()
        print(f"Mode: {mode}\n")
        handle_mode(mode)
    except KeyboardInterrupt:
        return 0

    return 0

main()