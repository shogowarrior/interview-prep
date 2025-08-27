package design.banking;

import java.util.Collections;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/api")
class BankingController {
    private final BankingService bankingService = new BankingService(5);
    private final Scheduler scheduler = new Scheduler();

    @PostMapping("/account/{id}/deposit")
    public ResponseEntity<String> deposit(@PathVariable String id, @RequestParam double amount) {
        try {
            bankingService.deposit(id, amount);
            return ResponseEntity.ok("Deposited " + amount + " into account " + id);
        } catch (IllegalArgumentException e) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, e.getMessage());
        }
    }

    @PostMapping("/transfer")
    public ResponseEntity<String> transfer(@RequestParam String from, @RequestParam String to, @RequestParam double amount) {
        if (!bankingService.transfer(from, to, amount)) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Transfer failed");
        }
        return ResponseEntity.ok("Transfer successful");
    }

    @PostMapping("/schedule-transfer")
    public ResponseEntity<String> scheduleTransfer(@RequestParam String from, @RequestParam String to, @RequestParam double amount, @RequestParam long delayMs) {
        scheduler.scheduleTransfer(bankingService, from, to, amount, delayMs);
        return ResponseEntity.ok("Scheduled transfer");
    }

    @GetMapping("/logs")
    public List<String> getLogs(
        @RequestParam(name = "page", defaultValue = "0") int page,
        @RequestParam(name = "size", defaultValue = "10") int size) {
        return paginate(scheduler.getLogs(), page, size);
    }

    @GetMapping("/top-accounts")
    public List<Account> getTopAccounts(
        @RequestParam(name = "page", defaultValue = "0") int page,
        @RequestParam(name = "size", defaultValue = "10") int size) {
        return paginate(bankingService.getTopKAccounts(), page, size);
    }


    @PostMapping("/merge")
    public ResponseEntity<String> mergeAccounts(@RequestParam String from, @RequestParam String to) {
        AccountMerger.merge(bankingService, from, to);
        return ResponseEntity.ok("Merged account " + from + " into " + to);
    }

    private <T> List<T> paginate(List<T> list, int page, int size) {
        int fromIndex = page * size;
        if (fromIndex >= list.size()) return Collections.emptyList();
        return list.subList(fromIndex, Math.min(fromIndex + size, list.size()));
    }
}