import json
import configparser
import sys

def parse_config(config_path):
    """Parse the configuration file and return a dictionary."""
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        sys.exit(1)
    
    data = {}
    for section in config.sections():
        data[section] = dict(config.items(section))
    return data

def print_parsed_data(data):
    """Print the parsed configuration data in the specified format."""
    print("Configuration File Parser Results:")
    for section, items in data.items():
        print(f"\n{section}:")
        for key, value in items.items():
            print(f"- {key}: {value}")

def save_to_json(data, output_path):
    """Save the parsed data to a JSON file."""
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving JSON data: {e}")
        sys.exit(1)