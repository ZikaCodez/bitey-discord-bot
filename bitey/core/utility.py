import random
import datetime

def generate_id():
    return random.randint(1000, 9999)

def send_log(type, message):
    colors = {
        "SUCCESS": "\033[92m",
        "PROCESS": "\033[94m",
        "ERROR": "\033[91m",
        "WARNING": "\033[93m",
        "RESET": "\033[0m",
    }
    
    background_colors = {
        "SUCCESS": "\033[42m",
        "PROCESS": "\033[44m",
        "ERROR": "\033[41m",
        "WARNING": "\033[43m",
        "RESET": "\033[0m",
    }

    bg_color = background_colors.get(type.upper(), background_colors["RESET"])
    
    color = colors.get(type.upper(), colors["RESET"])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{color}[{timestamp}] {bg_color}{type.upper()}{colors['RESET']}: {message}{colors['RESET']}")