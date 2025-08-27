package design.filesystem;

import java.util.concurrent.ConcurrentHashMap;

public class FileStore {
    private ConcurrentHashMap<String, FileObject> files = new ConcurrentHashMap<>();

    public void set(String name, String content) {
        files.put(name, new FileObject(name, content));
    }

    public String get(String name) {
        FileObject file = files.get(name);
        return (file != null) ? file.getContent() : null;
    }

    public FileObject getFile(String name) {
        return files.get(name);
    }

    public ConcurrentHashMap<String, FileObject> getAllFiles() {
        return files;
    }
}


