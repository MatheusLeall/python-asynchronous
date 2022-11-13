from src.projects.bank_example import Account, create_accounts, get_two_accounts, transfer


class TestAccountClass:
    def test_should_create_account_with_no_balance(self):
        account = Account()

        assert isinstance(account, Account)
        assert account.amount == 0

    def test_should_create_an_account_with_amount(self):
        account_with_amount = Account(amount=1000)

        expected_ammount = account_with_amount.amount

        assert isinstance(account_with_amount, Account)
        assert account_with_amount.amount == expected_ammount


class TestUnitFunctions:
    def test_should_transfer_amount_between_accounts(self):
        c1 = Account(amount=1000)
        c2 = Account()
        quantity_to_transfer = 500

        transfer(c1, c2, quantity_to_transfer)

        assert c1.amount == quantity_to_transfer
        assert c2.amount == quantity_to_transfer

    def test_should_create_accounts(self):
        accounts = create_accounts()

        assert accounts is not None
        assert [isinstance(account, Account) for account in accounts]

    def test_should_get_two_accounts(self):
        accounts = create_accounts()

        c1, c2 = get_two_accounts(accounts=accounts)

        assert isinstance(c1, Account) and isinstance(c2, Account)
        assert c1.amount > 0 and c2.amount > 0
        assert c1.amount != c2.amount
