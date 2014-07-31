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
        BOOTSTRAP_ADDRS='192.168.0.10 pool.maeh.org pool2.maeh.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
phoenixcoin=math.Object(
        PARENT=networks.nets['phoenixcoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=20, # blocks
        IDENTIFIER = '50686F656E69784C'.decode('hex'), # PhoenixL
        PREFIX = '5058432D4C697665'.decode('hex'), # PXC-Live
        P2P_PORT=11555,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=11554,
        BOOTSTRAP_ADDRS='atlas.phoenixcoin.org prometheus.phoenixcoin.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-pxc',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Phoenixcoin to >= 0.6.6.0!' if v < 60600 else None,
    ),
    phoenixcoin_testnet=math.Object(
        PARENT=networks.nets['phoenixcoin_testnet'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=20, # blocks
        IDENTIFIER = '50686F656E697854'.decode('hex'), # PhoenixT
        PREFIX = '5058432D54657374'.decode('hex'), # PXC-Test
        P2P_PORT=20555,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=20554,
        BOOTSTRAP_ADDRS='phoenixcoin.org menoetius.phoenixcoin.org prometheus.phoenixcoin.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-pxct',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Phoenixcoin to >= 0.6.6.0!' if v < 60600 else None,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
