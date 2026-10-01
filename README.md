26. Classes instances and methods — 15 points
Implement Player with __init__(name, score=0), independent name and score instance attributes, and add_points(points), which updates and returns that player's score.

27. Class attributes and shadowing
    Implement Device with a class attribute room initially set to "Lab 1" and an initializer storing each asset_tag. The given calls change the class attribute, then shadow it on one instance.

28. Encapsulation with methods — 15 points
Implement BankAccount with _balance, __init__(initial_balance=0), get_balance(), deposit(amount), and withdraw(amount). Raise ValueError for a negative initial balance, nonpositive deposits or withdrawals, and withdrawals exceeding the balance.

29. Properties and validation — 15 points
Implement Product with name, a validating price property backed by _price, and total(quantity). Reject any initial or assigned price of 0 or less with ValueError.

30. Abstraction and independent instance state — 15 points
Implement ReadingList with a separate _books list per instance, add_book(title), count(), and titles(). Reject blank or whitespace-only titles with ValueError. Return a copy from titles() so callers cannot modify the internal list.
