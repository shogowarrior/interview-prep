package design.WebCrawler;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Set;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

import static design.WebCrawler.CrawlerUtils.extractLinks;

public class AsyncWebCrawler {
    private final HttpClient client = HttpClient.newHttpClient();
    private final Set<String> visited = ConcurrentHashMap.newKeySet();
    private final AtomicInteger activeTasks = new AtomicInteger(0);
    private CountDownLatch doneSignal;

    public void crawl(String url) {
        if (!visited.add(url)) return;
        activeTasks.incrementAndGet();

        System.out.println("Crawling: " + url);
        client.sendAsync(HttpRequest.newBuilder(URI.create(url)).GET().build(), HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .thenApply(content -> extractLinks(url, content))
              .thenAccept(links -> links.forEach(link -> crawl(link)))
              .exceptionally(ex -> {
                  System.err.println("Failed to fetch: " + url);
                  return null;
              })
              .whenComplete((result, throwable) -> {
                  if (activeTasks.decrementAndGet() == 0 && doneSignal != null) {
                      doneSignal.countDown();
                  }
              });
    }

    public void crawlAndWait(String url) throws InterruptedException {
        doneSignal = new CountDownLatch(1);
        crawl(url);
        doneSignal.await();
    }

    public static void main(String[] args) throws InterruptedException {
        AsyncWebCrawler crawler = new AsyncWebCrawler();
        crawler.crawlAndWait("https://google.com");
    }
}
