import broadlink as blk
import logging, time, json
import sys, os

def get_device(device_ip):
    if blk.hello(host=device_ip) == None:
        logging.critical('Device not found')
        raise SystemExit('The device with ip ' + device_ip + ' could not be establish a connection.')
    remote = blk.discover(discover_ip_address=device_ip)[0]
    remote.auth()
    return remote

def get_config(ir_config_file):
    if os.path.exists(ir_config_file):
        with open(ir_config_file, 'r') as f:
            return json.load(f)

sys.argv.pop(0)
logging.getLogger().setLevel(logging.INFO)

ir_config_file = './cfg/ir.json'
config = get_config(ir_config_file)

if len(sys.argv) != 4:
    logging.critical(sys.argv)
    raise SystemExit("Not enough arguments. Should be: \"python3 blk.py device function appliance button\".")

dev = sys.argv[0] # 192.168.1.192
func = sys.argv[1] # Accion
appl = sys.argv[2] # Appliance
btn = sys.argv[3] # Btn

if func == 'learn':
    remote = get_device(dev)
    remote.enter_learning()
    logging.info('Press the button... led must be white right now')
    time.sleep(5)
    ir_packet = remote.check_data()
    ir_hex = ir_packet.hex()

    if appl in config.keys():
        config[appl].update({btn: ir_hex})
    else:
        config.update({appl:{btn:ir_hex}})

    json_object = json.dumps(config, indent = 2)
    with open(ir_config_file, 'w') as outfile:
        outfile.write(json_object)

elif func == 'send':
    get_device(dev).send_data(bytes.fromhex(config[appl][btn]))

else:
    raise SystemExit("dafac you want?")