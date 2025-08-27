package design.banking;

import java.util.Collections;

import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;

@SpringBootApplication
public class BankingApplication {
    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(BankingApplication.class);
        app.setDefaultProperties(Collections.singletonMap("server.port", "8081"));
        app.run(args);
    }
}

class AccountMerger {
    public static void merge(BankingService service, String fromId, String intoId) {
        Account from = service.createAccount(fromId);
        Account into = service.createAccount(intoId);
        into.deposit(from.balance);
        from.balance = 0;
        into.transactions.addAll(from.transactions);
    }
}

class MemoryManager {
    private final int maxTransactionsPerAccount;

    public MemoryManager(int maxTransactionsPerAccount) {
        this.maxTransactionsPerAccount = maxTransactionsPerAccount;
    }

    public void enforce(Account acc) {
        synchronized (acc) {
            int excess = acc.transactions.size() - maxTransactionsPerAccount;
            if (excess > 0) {
                acc.transactions.subList(0, excess).clear();
            }
        }
    }
}
