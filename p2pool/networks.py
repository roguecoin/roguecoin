from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
        feathercoin=math.Object(     
        PARENT=networks.nets['feathercoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=120, # blocks
        IDENTIFIER='4665617468657221'.decode('hex'),
        PREFIX='b131010ba6d4729a'.decode('hex'),
        P2P_PORT=19339,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='pool.maeh.org pool2.maeh.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    feathercoin_testnet=math.Object(     
        PARENT=networks.nets['feathercoin_testnet'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=120, # blocks
        IDENTIFIER='4665617468657221'.decode('hex'),
        PREFIX='b131010ba6d4729a'.decode('hex'),
        P2P_PORT=19340,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='pool.maeh.org pool2.maeh.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
