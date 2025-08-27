package design.banking;

class Transaction {
    public final String from;
    public final String to;
    public final double amount;
    public final long timestamp;
    public final String type;

    public Transaction(String from, String to, double amount, String type) {
        this.from = from;
        this.to = to;
        this.amount = amount;
        this.timestamp = System.currentTimeMillis();
        this.type = type;
    }
}