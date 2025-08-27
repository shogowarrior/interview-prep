package design.filesystem;

import java.io.*;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class FileStoreBackup {

    public static void backup(FileStore store, String filePath) throws IOException {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(filePath))) {
            out.writeObject(store.getAllFiles());
        }
    }

    @SuppressWarnings("unchecked")
    public static FileStore restore(String filePath) throws IOException, ClassNotFoundException {
        FileStore store = new FileStore();
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(filePath))) {
            ConcurrentHashMap<String, FileObject> files = (ConcurrentHashMap<String, FileObject>) in.readObject();
            for (Map.Entry<String, FileObject> entry : files.entrySet()) {
                store.set(entry.getKey(), entry.getValue().getContent());
            }
        }
        return store;
    }
}
