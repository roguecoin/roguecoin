import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack

nets = dict(
    feathercoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=9336,
        ADDRESS_VERSION=14,
        RPC_PORT=9337,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'feathercoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 200*100000000 >> (height + 1)//3360000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='FTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.feathercoin'), 'feathercoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.feathercoin.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.feathercoin.com/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.feathercoin.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),

    feathercoin_testnet=math.Object(
        P2P_PREFIX='daafa5ba'.decode('hex'),
        P2P_PORT=19336,
        ADDRESS_VERSION=65,
        RPC_PORT=19337,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'feathercoinaddress' in (yield bitcoind.rpc_help()) and
             (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 200*100000000 >> (height + 1)//3360000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='FTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.feathercoin'), 'feathercoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.feathercoin.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.feathercoin.com/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.feathercoin.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
phoenixcoin=math.Object(
        P2P_PREFIX='FED0D8C3'.decode('hex'),
        P2P_PORT=9555,
        ADDRESS_VERSION=56,
        RPC_PORT=9554,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'phoenixcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//1000000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=90, # s
        SYMBOL='PXC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.getcwd(), 'data') if platform.system() == 'Windows' else os.path.expanduser('~/.phoenixcoin'), 'phoenixcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.phoenixcoin.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.phoenixcoin.org/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.phoenixcoin.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.1e8,
    ),
    phoenixcoin_testnet=math.Object(
        P2P_PREFIX='FED0D8D4'.decode('hex'),
        P2P_PORT=19555,
        ADDRESS_VERSION=111,
        RPC_PORT=19554,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'phoenixcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 25*100000000 >> (height + 1)//1000000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data)),
        BLOCK_PERIOD=90, # s
        SYMBOL='PXCt',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.getcwd(), 'data') if platform.system() == 'Windows' else os.path.expanduser('~/.phoenixcoin'), 'phoenixcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.phoenixcoin.org:3080/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.phoenixcoin.org:3080/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.phoenixcoin.org:3080/tx/',
        SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.1e8,
    ),


)
for net_name, net in nets.iteritems():
    net.NAME = net_name
