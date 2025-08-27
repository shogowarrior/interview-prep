package design.WebCrawler;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class CrawlerUtils {

    private static final Pattern LINK_PATTERN = Pattern.compile("(?i)<(?:a|link)[^>]+href\\s*=\\s*['\"]([^'\"]+)['\"]");

    public static String resolveRelativeUrl(String baseUrl, String href) {
        try {
            URI base = URI.create(baseUrl);
            URI resolved = base.resolve(href);
            return resolved.toString();
        } catch (Exception e) {
            return null; // Malformed
        }
    }

    public static List<String> extractLinks(String baseUrl, String content) {
        List<String> links = new ArrayList<>();
        Matcher matcher = LINK_PATTERN.matcher(content);

        while (matcher.find()) {
            String href = matcher.group(1);
            String absolute = resolveRelativeUrl(baseUrl, href);
            if (absolute != null && absolute.startsWith("http")) {
                links.add(absolute);
            }
        }
        return links;
    }
    
    public static String fetchSimple(String url) throws IOException, URISyntaxException {
        return new String((new URI(url)).toURL().openStream().readAllBytes());
    }

    public static String fetch(String url) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newBuilder()
                .followRedirects(HttpClient.Redirect.NORMAL)
                .build();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
                .timeout(java.time.Duration.ofSeconds(10))
                .header("User-Agent", "Mozilla/5.0 (compatible; WebCrawler/1.0)")
                .GET()
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new IOException("HTTP error: " + response.statusCode());
        }
        return response.body();
    }

    public static CompletableFuture<String> fetchAsync(String url) {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url)).GET().build();
        return client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
                    .thenApply(HttpResponse::body);
    }

}
