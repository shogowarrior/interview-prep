package design.filesystem;

import java.util.List;
import java.util.stream.Collectors;

public class FileFilter {
    public static List<FileObject> filterByNamePrefix(FileStore store, String prefix) {
        return store.getAllFiles().values().stream()
                .filter(f -> f.getName().startsWith(prefix))
                .collect(Collectors.toList());
    }

    public static List<FileObject> searchContent(FileStore store, String keyword) {
        return store.getAllFiles().values().stream()
                .filter(f -> f.getContent().contains(keyword))
                .collect(Collectors.toList());
    }
}

