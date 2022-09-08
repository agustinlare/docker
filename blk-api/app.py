from flask import Flask
import broadlink as blk
import json, os

app = Flask(__name__)
config_file = "./blk.json"

if not os.path.isfile(config_file):
  raise SystemExit("Configuration file is missing")
else:
  with open(config_file) as f:
    config = json.load(f)

@app.route('/', methods=['GET'])
def index():
  return "e.g. /light/switch"

@app.route('/<device>/<button>', methods=['GET'])
def call_blk(device, button):
  try:
    assert device in config, "Device or button not found"
    assert button in config[device], "Button no encontrada"
    remote = blk.discover(discover_ip_address="192.168.1.193")[0]
    remote.auth()
    remote.send_data(bytes.fromhex(config[device][button]))

    return "You can close this windows now"
  except AssertionError as e:
    return {"message": str(e)}
  except Exception as e:
    raise SystemExit(str(e))

if __name__ == '__main__':
    if os.getenv('FLASK_APP'):
        app.run(host=os.environ['FLASK_RUN_HOST'], port=os.environ['FLASK_RUN_PORT'])
    else:
        app.run(debug=True, port=8881)
