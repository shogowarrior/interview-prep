package design.filesystem;

public class FileSystem {
    public static void main(String[] args) throws Exception {
        FileStore node1 = new FileStore();
        FileStore node2 = new FileStore();

        DistributedFileSystem dfs = new DistributedFileSystem();
        dfs.addNode(node1);
        dfs.addNode(node2);

        dfs.set("report.txt", "This is a distributed file.");
        System.out.println(dfs.get("report.txt"));

        FileStoreBackup.backup(node1, "backup.dat");

        FileStore restored = FileStoreBackup.restore("backup.dat");
        System.out.println(restored.get("report.txt"));
    }
}

