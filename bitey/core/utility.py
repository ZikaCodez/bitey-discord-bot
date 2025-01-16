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
        "BLACK": "\033[30m",
        "RESET": "\033[0m",
    }
    
    background_colors = {
        "SUCCESS": "\033[42m",
        "PROCESS": "\033[44m",
        "ERROR": "\033[41m",
        "WARNING": "\033[43m",
        "BLACK": "\033[40m",
        "RESET": "\033[0m",
    }

    bg_color = background_colors.get(type.upper(), background_colors["RESET"])
    
    color = colors.get(type.upper(), colors["RESET"])
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    print(f"{color}[{timestamp}]{colors['RESET']} {bg_color}{colors["BLACK"]}{type.upper()}{colors['RESET']}{color}: {message}{colors['RESET']}")