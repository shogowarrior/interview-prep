package design.banking;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

class Scheduler {
    private final ScheduledExecutorService executor = Executors.newScheduledThreadPool(2);
    private final List<String> logs = Collections.synchronizedList(new ArrayList<>());

    public void scheduleTransfer(BankingService service, String fromId, String toId, double amount, long delayMs) {
        executor.schedule(() -> {
            boolean success = service.transfer(fromId, toId, amount);
            logs.add("Scheduled transfer: " + fromId + " -> " + toId + " $" + amount + " Success: " + success);
        }, delayMs, TimeUnit.MILLISECONDS);
        logs.add("Scheduled transfer in " + delayMs + "ms: " + fromId + " -> " + toId);
    }

    public List<String> getLogs() {
        return new ArrayList<>(logs);
    }

    public void shutdown() {
        executor.shutdown();
    }
}