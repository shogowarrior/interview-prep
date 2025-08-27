package design;

import java.util.*;

public class StackTraceReconstruction {

    public static List<List<String>> reconstructStackTrace(List<String> events) {
        Deque<String> stack = new ArrayDeque<>();
        List<List<String>> snapshots = new ArrayList<>();

        for (String event : events) {
            String[] parts = event.split(" ");
            String action = parts[0];
            String function = parts[1];

            if (action.equals("call")) {
                stack.push(function);
            } else if (action.equals("return")) {
                // Take a snapshot before popping
                List<String> snapshot = new ArrayList<>(stack);
                Collections.reverse(snapshot);  // Convert from top-to-bottom order
                snapshots.add(snapshot);

                // Check if the function matches the top of the stack
                if (stack.isEmpty() || !stack.peek().equals(function)) {
                    String ret = (stack.isEmpty() ? "empty" : stack.peek());
                    throw new IllegalStateException("Mismatched return: expected " + ret + ", got " + function);
                }
                stack.pop();
            } else {
                throw new IllegalArgumentException("Unknown action: " + action);
            }
        }

        return snapshots;
    }

    public static void main(String[] args) {
        List<String> events = Arrays.asList(
            "call A",
            "call B",
            "call C",
            "return C",
            "return B",
            "call D",
            "return D",
            "return A"
        );

        List<List<String>> stackTraces = reconstructStackTrace(events);

        for (int i = 0; i < stackTraces.size(); i++) {
            System.out.println("Before return " + (i + 1) + ": " + stackTraces.get(i));
        }
    }
}
