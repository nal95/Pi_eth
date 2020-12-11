import json
from web3 import Web3


ganache_url="HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.load([{"inputs":[],"name":"getUser","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"}],"name":"setName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"}])
address = web3.toChecksumAddress("0x69F16a80E1b64cB6A75cae81E400af321479F76A")

contract = web3.eth.contract(address = address , abi = abi)

print (contract.functions.getName().call())