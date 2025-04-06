import psutil
import time


def monitor_cpu_health(threshold:int = 80):
    """
    Monitors the CPU usage of the system and alerts if it exceeds a specified threshold.
    Args:
        threshold (int, optional): The CPU usage percentage threshold to trigger an alert.
                                   Defaults to 80.
    Behavior:
        - Continuously checks the CPU usage at 1-second intervals.
        - Prints an alert message if the CPU usage exceeds the specified threshold.
        - Handles exceptions during monitoring and prevents rapid error loops by pausing for 1 second.
        - Allows graceful exit from the monitoring loop using a keyboard interrupt (Ctrl+C).
    Note:
        This function requires the `psutil` library to be installed.
    """

    print("Monitoring CPU usage...")
    try:
        while True:
            try:
                # Get CPU usage with a 1-second interval
                cpu_usage = psutil.cpu_percent(interval=1)
                if cpu_usage > threshold:
                    print(f"Alert! CPU usage exceeds threshold: {cpu_usage:.0f}%")
            except Exception as e:
                print(f"An error occurred during monitoring: {e}")
                time.sleep(1)  # Prevent rapid error loops
    except KeyboardInterrupt:
        print("\nExiting CPU monitoring program.")


if __name__ == "__main__":
    monitor_cpu_health()
