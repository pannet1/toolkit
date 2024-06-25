from time import sleep
import subprocess

try:
    import pendulum as pdlm
except ModuleNotFoundError:
    print("pendulum module not found. Installing it")
    __import__("os").system("pip install pendulum")
    sleep(5)
    import pendulum as pdlm


def is_time_past(time_str: str) -> bool:
    """
    Args:
        time_str: HH:MM:SS or HH:MM
    Returns:
        True if time is past
    """
    tz = "Asia/Kolkata"
    given_time = pdlm.parse(time_str, tz=tz)
    current_time = pdlm.now(tz=tz)
    return current_time > given_time


def dt_to_str(str_time: str, time_format="YYYY-MM-DD HH:mm") -> str:
    """
    Args:
        str_time: HH:MM:SS or HH:MM
        time_format: pendulum string time format
    Returns:
        current time with the given time string
    """
    hour = minute = second = 0
    current_time = pdlm.now()
    if len(str_time) > 2:
        lst = str_time.split(":")
        if len(lst) == 3:
            hour = int(lst[0])
            minute = int(lst[1])
            second = int(lst[2])
        elif len(lst) == 2:
            hour = int(lst[0])
            minute = int(lst[1])
        elif len(lst) == 1:
            hour = int(lst[0])
        if len(lst) > 0:
            if hour > 0:
                current_time = current_time.replace(hour=hour)
            if minute > 0:
                current_time = current_time.replace(minute=minute)
            if second > 0:
                current_time = current_time.replace(second=second)
    return current_time.format(time_format)


def blink() -> None:
    sleep(round(pdlm.now().microsecond / 1000000, 2))


def timer(sec=1) -> None:
    """
    Args:
        sec: second(s) to sleep
    """
    sleep(sec)


def kill_tmux():
    try:
        subprocess.run(["tmux", "kill-session"], check=True)
    except subprocess.CalledProcessError as e:
        raise e


if __name__ == "__main__":
    print(dt_to_str("9:0"))
