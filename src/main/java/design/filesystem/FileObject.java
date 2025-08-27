package design.filesystem;

public class FileObject {
    private String name;
    private String content;
    private long createdAt;

    public FileObject(String name, String content) {
        this.name = name;
        this.content = content;
        this.createdAt = System.currentTimeMillis();
    }

    public String getName() { return name; }
    public String getContent() { return content; }
    public long getCreatedAt() { return createdAt; }

    public void setContent(String content) {
        this.content = content;
    }
}


