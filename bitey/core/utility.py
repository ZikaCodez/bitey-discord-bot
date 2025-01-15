import random
import datetime

def generate_id():
    return random.randint(1000, 9999)

def send_log(type, message):
    colors = {
        "INFO": "\033[94m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "SUCCESS": "\033[92m",
        "RESTART": "\033[0m",
    }
    
    background_colors = {
        "INFO": "\033[44m",
        "WARNING": "\033[43m",
        "ERROR": "\033[41m",
        "SUCCESS": "\033[42m",
        "RESTART": "\033[0m",
    }

    bg_color = background_colors.get(type.upper(), background_colors["RESTART"])
    
    color = colors.get(type.upper(), colors["RESTART"])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{color}[{timestamp}] {bg_color}{type.upper()}{colors['RESTART']}: {message}{colors['RESTART']}")