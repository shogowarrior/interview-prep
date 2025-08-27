package design.filesystem;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class DistributedFileSystem {
    private List<FileStore> nodes = new CopyOnWriteArrayList<>();

    public void addNode(FileStore node) {
        nodes.add(node);
    }

    public void set(String name, String content) {
        for (FileStore node : nodes) {
            node.set(name, content); // replicate
        }
    }

    public String get(String name) {
        for (FileStore node : nodes) {
            String content = node.get(name);
            if (content != null) return content;
        }
        return null;
    }
}

