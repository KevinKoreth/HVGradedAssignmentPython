
import json
from flask import Flask, jsonify
from src.utils import parse_config, print_parsed_data, save_to_json
app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
    """Endpoint to serve the JSON configuration data."""
    try:
        with open('database.json', 'r') as f:
            config_data = json.load(f)
        return jsonify(config_data)
    except FileNotFoundError:
        return jsonify({"error": "Configuration data not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Parse configuration file
    config_data = parse_config("src/config.ini")
    
    # Display parsed data
    print_parsed_data(config_data)
    
    # Save data to JSON file
    save_to_json(config_data, 'database.json')
    
    # Start Flask server
    print("\nServer is running. Use Ctrl+C to stop.")
    app.run(debug=False)