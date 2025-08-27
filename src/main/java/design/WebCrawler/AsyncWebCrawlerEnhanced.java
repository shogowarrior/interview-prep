package design.WebCrawler;

import java.net.URI;
import java.net.http.*;
import java.sql.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.stream.Collectors;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

public class AsyncWebCrawlerEnhanced {
    private final HttpClient client = HttpClient.newBuilder().followRedirects(HttpClient.Redirect.NORMAL).build();
    private final Set<String> visited = ConcurrentHashMap.newKeySet();
    private final Map<String, ExecutorService> domainExecutors = new ConcurrentHashMap<>();
    // private final Connection dbConnection;

    // public AsyncWebCrawlerEnhanced() throws SQLException {
        // dbConnection = DriverManager.getConnection("jdbc:sqlite:crawler.db");
        // try (Statement stmt = dbConnection.createStatement()) {
        //     stmt.execute("""
        //         CREATE TABLE IF NOT EXISTS pages (
        //             url TEXT PRIMARY KEY,
        //             title TEXT
        //         )
        //     """);
        // }
    // }

    public void crawl(String url) {
        if (!visited.add(url)) return;

        String domain = getDomain(url);
        ExecutorService executor = domainExecutors.computeIfAbsent(domain, d -> Executors.newFixedThreadPool(4));

        CompletableFuture.runAsync(() -> {
            HttpRequest request = HttpRequest.newBuilder(URI.create(url)).GET().build();
            client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
                  .thenApply(HttpResponse::body)
                  .thenAccept(body -> {
                    //   saveToDatabase(url, body);
                      List<String> links = extractLinks(url, body);
                      links.forEach(this::crawl); // Recursively crawl
                  })
                  .exceptionally(ex -> {
                      System.err.println("Failed to fetch: " + url);
                      return null;
                  });
        }, executor);
    }

    // private void saveToDatabase(String url, String html) {
    //     try {
    //         Document doc = Jsoup.parse(html);
    //         String title = doc.title();
    //         try (PreparedStatement pstmt = dbConnection.prepareStatement("INSERT OR IGNORE INTO pages (url, title) VALUES (?, ?)")) {
    //             pstmt.setString(1, url);
    //             pstmt.setString(2, title);
    //             pstmt.executeUpdate();
    //         }
    //     } catch (SQLException e) {
    //         System.err.println("DB error for: " + url);
    //     }
    // }

    private List<String> extractLinks(String baseUrl, String html) {
        try {
            Document doc = Jsoup.parse(html, baseUrl);
            Elements links = doc.select("a[href]");
            return links.stream()
                        .map(link -> link.absUrl("href"))
                        .filter(href -> href.startsWith("http"))
                        .collect(Collectors.toList());
        } catch (Exception e) {
            return List.of();
        }
    }

    private String getDomain(String url) {
        try {
            return URI.create(url).getHost();
        } catch (Exception e) {
            return "default";
        }
    }

    public void shutdown() {
        domainExecutors.values().forEach(ExecutorService::shutdown);
        // try {
        //     dbConnection.close();
        // } catch (SQLException e) {
        //     System.err.println("Failed to close DB");
        // }
    }

    public static void main(String[] args) throws Exception {
        AsyncWebCrawlerEnhanced crawler = new AsyncWebCrawlerEnhanced();
        crawler.crawl("https://example.com");

        // Let it run for a while then shut down
        Thread.sleep(15000);
        crawler.shutdown();
    }
}
