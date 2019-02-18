"""
@version 1.2.0
"""

# TODO: Add mallcious nodes.
# TODO: Add light clients.

from simulator import agent, environment, virtual_network
from arguments import argparser

import json
import os
from time import sleep
import random
import numpy as np
from pprint import pprint


# define
IP = "http://127.0.0.1"
SEED = 950327

# random seed
random.seed(SEED)
np.random.seed(SEED)


def check_agents_avail(agents):
    for agent in agents:
        try:
            agent.get_address()
        except:
            return False

    return True


def check_master_avail(master):
    try:
        return master.get_peers()
    except:
        return []


if __name__ == '__main__':
    args = argparser()

    try:
        agents = [agent.Agent(args, IP, args.https + i, args.p2ps + i) for i in range(args.nodes)]
        env = environment.Env(args)
        vnet = virtual_network.Vnet(args, agents)

        # pprint(vnet.virtual_connections)
        with open('table.json', 'w') as f:
            json.dump(vnet.virtual_connections, f)

        # TODO: Visualization of virtual and real network with propagation delay.
        # Use table.json

        while not check_agents_avail(agents):
            pass

        master = virtual_network.Master(args, IP, args.master_http, args.master_p2p, agents)

        while not len(check_master_avail(master)) == args.nodes:
            pass

        step = 0
        while True:
            # TODO: Replace 'while' loop to multi-processing.
            # Current implementation doesn't make multiple queries.
            who_ = random.randrange(0, len(agents))

            # How frequently?
            delay_ = random.random() * 10

            print("step: {}, agent: {}, delay: {}".format(step, who_, delay_))

            agents[who_].mine_block()

            step += 1
            sleep(delay_)

        # TODO: How many steps?
        # What means 'step'? What means 'episode'?

        """analysis"""
        # 각 에이전트의 블록 생성 비율, 채택 비율
        # tps (마스터노드를 통과하는 초당 블록의 갯수)
        # 포크 발생 비율

        # TODO: Offer the dashboard with tensorboardX.
        # Tracking master node

    finally:
        os.system("killall npm")
