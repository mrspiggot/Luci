from brownie import Luci, accounts, network, config
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_accounts():
    print(f"get_account network is {network.show_active()}")
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(f"Network is {network.show_active()}")
        print(accounts[0], len(accounts))
        return accounts[0], accounts[1], accounts[2]
    else:
        print(f"Network is {network.show_active()}")
        return accounts.add(config["wallets"]["from_key"]), accounts.add(config["wallets"]["from_key2"]), accounts.add(
            config["wallets"]["from_key3"])


def deploy_token():
    initial_supply = Web3.toWei(1_000_000, "ether")
    account, account2, account3 = get_accounts()

    my_token = Luci.deploy(account, initial_supply, {"from": account},
                                publish_source=config["networks"][network.show_active()].get("verify"))
    return my_token


def main():
    my_token = deploy_token()

    # account_0, account_1, account_2 = get_accounts()
    # get_token_balance(account_0.address)
    #
    # send_token(account_1, Web3.toWei(7_000_000, "ether"))
    # get_token_balance(account_0.address)
    # get_token_balance(account_1.address)
    # get_token_balance(account_2.address)



def get_token_balance(account_address):
    my_token = Luci[-1]
    print(
        f"The account {account_address} has balance {my_token.balanceOf(account_address)} of {my_token.symbol()} called {my_token.name()}")


def send_token(receiver_address, amount):
    my_token = Luci[-1]
    my_token.transfer(receiver_address, amount)
    get_token_balance(receiver_address)


def set_allowance(spender_address, amount):
    my_token = Luci[-1]
    my_token.increaseAllowance(spender_address, amount)

