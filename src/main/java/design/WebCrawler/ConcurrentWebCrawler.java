package design.WebCrawler;

import java.io.IOException;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import static design.WebCrawler.CrawlerUtils.extractLinks;
import static design.WebCrawler.CrawlerUtils.fetch;


public class ConcurrentWebCrawler {
    private final ExecutorService executor = Executors.newFixedThreadPool(10);
    private final Set<String> visited = ConcurrentHashMap.newKeySet();

    public void crawl(String url) {
        if (visited.contains(url)) return;
        visited.add(url);

        System.out.println("Crawling: " + url);
        executor.submit(() -> {
            try {
                String content = fetch(url);
                for (String link : extractLinks(url, content)) {
                    crawl(link); // submit new tasks recursively
                }
            } catch (IOException | InterruptedException e) {
                System.err.println("Failed to fetch: " + url);
            }
        });
    }

    public void shutdown() throws InterruptedException {
        executor.awaitTermination(5, TimeUnit.SECONDS);
        executor.shutdown();
    }

    public static void main(String[] args) throws InterruptedException {
        ConcurrentWebCrawler crawler = new ConcurrentWebCrawler();
        crawler.crawl("https://google.com");
        crawler.shutdown();
    }

}
