package design.banking;

import java.util.ArrayList;
import java.util.List;

class Account {
    public final String id;
    public double balance;
    public final List<Transaction> transactions = new ArrayList<>();

    public Account(String id) {
        this.id = id;
        this.balance = 0.0;
    }

    public synchronized void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("Amount must be positive");
        balance += amount;
        transactions.add(new Transaction(id, id, amount, "DEPOSIT"));
    }

    public synchronized boolean transferTo(Account to, double amount) {
        if (amount <= 0) return false;
        if (balance >= amount) {
            balance -= amount;
            to.deposit(amount);
            transactions.add(new Transaction(id, to.id, amount, "TRANSFER"));
            return true;
        }
        return false;
    }
}
