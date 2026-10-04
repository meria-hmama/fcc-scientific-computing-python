class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, other_category):
        if not self.check_funds(amount):
            return False
        # withdrawal from self
        self.ledger.append({
            "amount": -amount,
            "description": f"Transfer to {other_category.name}"
        })
        # deposit to other
        other_category.ledger.append({
            "amount": amount,
            "description": f"Transfer from {self.name}"
        })
        return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        lines = []
        for item in self.ledger:
            desc = item["description"][:23]
            amount = item["amount"]
            amount_str = f"{amount:7.2f}"
            lines.append(f"{desc:<23}{amount_str}")
        body = "\n".join(lines)
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}{body}\n{total}"


def create_spend_chart(categories):
    withdrawals = []
    for cat in categories:
        total_withdrawn = sum(
            -item["amount"] for item in cat.ledger if item["amount"] < 0
        )
        withdrawals.append(total_withdrawn)

    total_spent = sum(withdrawals)

    percentages = []
    for w in withdrawals:
        if total_spent == 0:
            pct = 0
        else:
            pct = int((w / total_spent) * 100)
        percentages.append(pct)

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        label = f"{level:3d}|"
        row_parts = []
        for pct in percentages:
            if pct >= level:
                row_parts.append(" o ")
            else:
                row_parts.append("   ")
        row = label + "".join(row_parts) + " "
        lines.append(row)

    h_line = "    " + "-" * (3 * len(categories) + 1)
    lines.append(h_line)

    max_len = max(len(cat.name) for cat in categories) if categories else 0

    for i in range(max_len):
        chars = [cat.name[i] if i < len(cat.name) else " " for cat in categories]
        name_line = "     " + "  ".join(chars) + "  "
        lines.append(name_line)

    return "\n".join(lines)