def individual_serial(account) ->dict:
    return {
        "account_number": account["account_number"],
        "user_id": account["user_id"],
        "balance":  account["balance"],
        "account_type": account["account_type"],
        "status": account["status"],
        "initial_deposit": account["initial_deposit"]
    }
def list_serial(accounts)->list:
    return[individual_serial(accounts) for account in accounts]

