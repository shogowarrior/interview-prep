package design.banking;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.concurrent.ConcurrentHashMap;

class BankingService {
    private final Map<String, Account> accounts = new ConcurrentHashMap<>();
    private final PriorityQueue<Account> topKAccounts = new PriorityQueue<>((a, b) -> Double.compare(a.balance, b.balance));
    private final int topK;

    public BankingService(int topK) {
        this.topK = topK;
    }

    public Account createAccount(String id) {
        return accounts.computeIfAbsent(id, Account::new);
    }

    public void deposit(String id, double amount) {
        Account account = createAccount(id);
        account.deposit(amount);
        updateTopK(account);
    }

    public boolean transfer(String fromId, String toId, double amount) {
        Account from = createAccount(fromId);
        Account to = createAccount(toId);
        boolean success = from.transferTo(to, amount);
        if (success) {
            updateTopK(from);
            updateTopK(to);
        }
        return success;
    }

    private void updateTopK(Account acc) {
        synchronized (topKAccounts) {
            topKAccounts.remove(acc);
            topKAccounts.add(acc);
            if (topKAccounts.size() > topK) {
                topKAccounts.poll();
            }
        }
    }

    public List<Account> getTopKAccounts() {
        synchronized (topKAccounts) {
            return new ArrayList<>(topKAccounts);
        }
    }
}