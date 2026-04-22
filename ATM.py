"""ATM Transaction Validator"""
def process_withdrawal(balance: int, requests: list[int]) -> None:
    """Checks balance before transaction
    Conditions:
        - Amount must be a multiple of 100
        - Amount must be positive
    Args:
        balance (int): Initial balance in the account
        requests (list[int]): List of withdrawal amounts
    """
    for amount in requests:
        if amount < 0 or amount % 100 != 0 or amount > balance:
            print("FAILED")
        else:
            balance -= amount
            print("SUCCESS")
