package design.WebCrawler;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.io.IOException;

import static design.WebCrawler.CrawlerUtils.extractLinks;
import static design.WebCrawler.CrawlerUtils.fetch;

public class SyncWebCrawler {

    private final Set<String> visited = ConcurrentHashMap.newKeySet();

    public void crawl(String url) {
        if (visited.contains(url)) return;
        visited.add(url);
        
        System.out.println("Crawling: " + url);
        try {
            String content = fetch(url);
            for (String link : extractLinks(url, content)) {
                crawl(link);
            }
        } catch (IOException | InterruptedException e) {
            System.err.println("Failed to fetch: " + url);
        }
    }

    public static void main(String[] args) {
        SyncWebCrawler crawler = new SyncWebCrawler();
        crawler.crawl("https://bbc.com");
    }
}
