def customer_individual_serial(customer) ->dict:
    return {
        "user_name": customer["user_name"],
        "user_id":   customer["user_id"],
        "active_accounts": customer["active_accounts"]
    }
def customer_list_serial(customers)->list:
    return[customer_individual_serial(customers) for customer in customers]
