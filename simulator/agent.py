import requests
import json
import ast
from platform import system
import os


class Agent:
    def __init__(self, args, IP, HTTP_PORT, P2P_PORT):
        self.ip_address = IP
        self.http_port = HTTP_PORT
        self.p2p_port = P2P_PORT
        self.uri = self.ip_address + ':' + str(self.http_port)

        self.start_daemon()

    def start_daemon(self):
        def is_windows():
            return True if system() == "Windows" else False

        try:
            os.chdir("./onechain")

            os.environ['HTTP_PORT'] = str(self.http_port)
            os.environ['P2P_PORT'] = str(self.p2p_port)

            if is_windows():
                os.system("nohup START /B npm start")
            else:
                os.system("nohup npm start &")

        finally:
            os.unsetenv('HTTP_PORT')
            os.unsetenv('P2P_PORT')
            os.chdir("../")

    def get_blocks(self):
        res = requests.get(self.uri + '/blocks')
        return ast.literal_eval(res.text)

    def mine_block(self, req=None):
        headers = {'Content-type': 'application/json'}
        data = {"data": req}
        res = requests.post(self.uri + '/mineBlock', headers=headers, data=json.dumps(data))
        return res.text

    # add_peers
    # block_version
    # CreateWallet
    # DeleteWallet
    # stop
