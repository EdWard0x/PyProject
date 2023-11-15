import json
import sys
import time

import traceback

from web3 import Web3, HTTPProvider

rpc = 'https://polygon-rpc.com'
FORTA_ADDRESS = Web3.toChecksumAddress('0x9ff62d1FC52A907B6DCbA8077c2DDCA6E6a9d3e1')
FORTA_ABI = json.loads(
    '[{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"DenominatorLessOrEqualThanProd","type":"error"},{"inputs":[],"name":"FrozenSubject","type":"error"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"}],"name":"InvalidSubjectType","type":"error"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"MissingRole","type":"error"},{"inputs":[],"name":"NoActiveShares","type":"error"},{"inputs":[],"name":"NoInactiveShares","type":"error"},{"inputs":[],"name":"SlashingOver90Percent","type":"error"},{"inputs":[],"name":"StakeInactiveOrSubjectNotFound","type":"error"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"UnsupportedInterface","type":"error"},{"inputs":[],"name":"WithdrawalNotReady","type":"error"},{"inputs":[],"name":"WithdrawalSharesNotTransferible","type":"error"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"ZeroAddress","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newAddressManager","type":"address"}],"name":"AccessManagerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newWithdrawalDelay","type":"uint256"}],"name":"DelaySet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"by","type":"address"},{"indexed":false,"internalType":"bool","name":"isFrozen","type":"bool"}],"name":"Froze","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"}],"name":"MaxStakeReached","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Released","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Rewarded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"router","type":"address"}],"name":"RouterUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"by","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Slashed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"StakeDeposited","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newManager","type":"address"}],"name":"StakeParamsManagerSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokensSwept","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newTreasury","type":"address"}],"name":"TreasurySet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WithdrawalExecuted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint8","name":"subjectType","type":"uint8"},{"indexed":true,"internalType":"uint256","name":"subject","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint64","name":"deadline","type":"uint64"}],"name":"WithdrawalInitiated","type":"event"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"}],"name":"activeStakeFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"address","name":"account","type":"address"}],"name":"availableReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"uint256","name":"stakeValue","type":"uint256"}],"name":"deposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"exists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"bool","name":"frozen","type":"bool"}],"name":"freeze","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"address","name":"account","type":"address"}],"name":"inactiveSharesOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"}],"name":"inactiveStakeFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"__manager","type":"address"},{"internalType":"address","name":"__router","type":"address"},{"internalType":"contract IERC20","name":"__stakedToken","type":"address"},{"internalType":"uint64","name":"__withdrawalDelay","type":"uint64"},{"internalType":"address","name":"__treasury","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"uint256","name":"sharesValue","type":"uint256"}],"name":"initiateWithdrawal","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"}],"name":"isFrozen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"relayPermit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"address","name":"account","type":"address"}],"name":"releaseReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"reward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newManager","type":"address"}],"name":"setAccessManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint64","name":"newDelay","type":"uint64"}],"name":"setDelay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"ensRegistry","type":"address"},{"internalType":"string","name":"ensName","type":"string"}],"name":"setName","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newRouter","type":"address"}],"name":"setRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IStakeController","name":"newStakingParameters","type":"address"}],"name":"setStakingParametersManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newTreasury","type":"address"}],"name":"setTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newUri","type":"string"}],"name":"setURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"address","name":"account","type":"address"}],"name":"sharesOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"},{"internalType":"uint256","name":"stakeValue","type":"uint256"}],"name":"slash","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stakedToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"},{"internalType":"address","name":"recipient","type":"address"}],"name":"sweep","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalActiveStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"}],"name":"totalInactiveShares","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalInactiveStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"}],"name":"totalShares","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"subjectType","type":"uint8"},{"internalType":"uint256","name":"subject","type":"uint256"}],"name":"withdraw","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]')

web3 = Web3(HTTPProvider(rpc))
token_contract = web3.eth.contract(address=FORTA_ADDRESS, abi=FORTA_ABI)


def get_file_addr():
    matic_addr_info = []
    try:
        with open("wallet.txt", "r") as f:
            while True:
                matic_addr = {}
                lines = f.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                line_list = lines.split(' ')
                matic_addr['name'] = line_list[0]
                matic_addr['address'] = line_list[1]
                matic_addr['private_key'] = line_list[2].strip('\n')

                matic_addr_info.append(matic_addr)

    except:
        traceback.print_exc()

    return matic_addr_info


def get_amount(address):
    balance = web3.fromWei(token_contract.functions.balanceOf(address).call(), "ether")
    # print(balance)
    return balance


def transfer_forta(token_contract, from_address, private_key, target_address, amount):
    gas_price = web3.eth.gasPrice
    # block = web3.eth.block_number
    # gas_limit = block.gasLimit
    params = {
        "from": from_address,
        "value": 0,
        'gasPrice': gas_price,
        "gas": 1200000,
        "nonce": web3.eth.getTransactionCount(from_address),
        'chainId': 137
    }
    func = token_contract.functions.transfer(target_address, web3.toWei(amount, "ether"))
    tx = func.buildTransaction(params)
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("please use the following format:\n")
        print("python3 gather_forta.py address \n")

    else:
        print("==================================================")
        print("==     To Address:", sys.argv[1])

        wallets = get_file_addr()

        print("==     Wallet Count:", len(wallets), '\n')
        print("==================================================\n")

        i = 0

        total_forta = 0

        max = 0
        min = 1000
        not_deploy = 0

        for wallet in wallets:
            try:

                amount = get_amount(wallet['address'])

                print(i, wallet['name'], wallet['address'], amount)

                wallet['amount'] = amount

                total_forta = total_forta + amount

                if amount > max and amount < 300:
                    max = amount

                if amount < min:
                    min = amount

                if int(amount) == 0:
                    not_deploy = not_deploy + 1

                i = i + 1
            except:
                traceback.print_exc()
                i = i + 1

            # time.sleep(3)

        print("\nTotal_forta=", total_forta, 'max=', int(max), 'min=', int(min), 'not_deploy=', not_deploy, '\n')

        while True:
            in_content = input("Are you sure the transfer Forta (Y/N)：")
            if in_content == "Y":
                print("confirmed!....")

                break
            elif in_content == "N":
                print("exit！")
                exit(0)
            else:
                print("Wrong Input, please repeat！")

        i = 0

        for wallet in wallets:
            try:

                if wallet['amount'] == 0 or wallet['address'] == sys.argv[1]:
                    print(i, wallet['name'], wallet['address'], 'amount=', amount, '---no need transfer')
                else:
                    print(i, wallet['name'], wallet['address'], amount)

                    print("start transfer to ", sys.argv[1], 'amount=', wallet['amount'])

                    tx = transfer_forta(token_contract, wallet['address'], wallet['private_key'], sys.argv[1],
                                        wallet['amount'])

                    print('tx=', tx)

                print('\n')

                i = i + 1
            except Exception as e:
                print(str(e))
                i = i + 1

            time.sleep(3)
