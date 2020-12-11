import json
from web3 import Web3, HTTPProvider

ganacheUrl = 'HTTP://127.0.0.1:7545' 

Web3 = Web3(HTTPProvider(ganacheUrl))

Web3.eth.defaultAccount = Web3.eth.accounts[0]

deployedContract = '../build/contracts/Setter.json'

contractAddress = '0x39687ffcF30780b93eDf1dd52dca7915aE75A275'

with open(deployedContract) as file:
    contractJson = json.load(file)

    contractAbi = contractJson ['abi']

    contract = Web3.eth.contract(address = contractAddress, abi = contractAbi)

    name = contract.functions.getName().call()

    print(name)