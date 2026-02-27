transactions_list = [
    {"amt": 100, "curr": "EUR", "status": "Success"},
    {"amt": 50, "curr": "USD", "status": "Failed"},
    {"amt": 200, "curr": "USD", "status": "Success"},
    {"amt": 150, "curr": "EUR", "status": "Failed"}
]
def reconcile_ledger(transactions, rates):
    grouped_totals = {
        "Success": [],
        "Failed": []
    }
    
    for transaction in transactions:
        current_amount = transaction["amt"]
        current_currency = transaction["curr"]
        current_status = transaction["status"]
        
        conversion_rate = rates[current_currency]
        
        usd_amount = current_amount * conversion_rate
        
        if current_status == "Success":
            grouped_totals["Success"].append(usd_amount)
        elif current_status == "Failed":
            grouped_totals["Failed"].append(usd_amount)
            
    return grouped_totals


exchange_rates = {
    "EUR": 1.1,
    "USD": 1.0
}

final_result = reconcile_ledger(transactions_list, exchange_rates)

print(final_result)