# Web Crawler

## 1. Initial Synchronous Design

### Architecture

- Single-threaded.
- Fetch URLs one at a time.
- Parse page → Extract links → Crawl each link sequentially.

**_Pros:_**

- Simple to write and reason about.
- No concurrency bugs.

**_Cons:_**

- Very slow – waits for I/O.
- No parallelism.
- Blocks entire thread for each network call.

## 2. Introducing Concurrency with Threads

### Enhancement

- Use ExecutorService to crawl multiple pages concurrently.
- Thread-per-task model.

**_Pros:_**

- Uses multiple threads → Faster crawling.
- Exploits parallelism.

**_Cons:_**

- Limited scalability (too many threads = high memory & context switching).
- Still blocking I/O (each thread blocks during ```fetch```).

## 3. Asynchronous + Non-blocking I/O (Async I/O with CompletableFuture)

### Strategy

- Use CompletableFuture or Java's HttpClient with sendAsync.
- Avoids blocking threads during I/O.
- Suitable for massive scale.

**_Pros:_**

- Highly scalable (thousands of concurrent requests).
- No thread-per-request overhead.
- Ideal for I/O-bound tasks like web crawling.

**_Cons:_**

- More complex error handling and flow control.
- Harder to limit depth/rate (needs careful orchestration).

## Concurrency Considerations

| Concern                            | How to Address                                                         |
| ---------------------------------- | ---------------------------------------------------------------------- |
| **Duplicate URLs**                 | Use thread-safe `Set<String>` (e.g., `ConcurrentHashMap.newKeySet()`). |
| **Depth Control**                  | Pass depth param and reject if exceeds max.                            |
| **Rate Limiting**                  | Use `Semaphore` or external rate-limiter like `Bucket4j`.              |
| **Graceful Shutdown**              | Track active tasks and wait for completion.                            |
| **Politeness (robots.txt, delay)** | Respect robots.txt; add delay before hitting same domain.              |

## Scalability Trade-offs

| Approach                             | Threads                | Blocking | Scalability | Complexity |
| ------------------------------------ | ---------------------- | -------- | ----------- | ---------- |
| Synchronous                          | 1                      | Yes      | Very low    | Low        |
| Thread Pool                          | Limited (e.g., 10-100) | Yes      | Medium      | Medium     |
| Async (CompletableFuture / Reactive) | Few                    | No       | High        | High       |

## Regex ```extractLinks```

```java
"(?i)<(?:a|link)[^>]+href\\s*=\\s*['\"]([^'\"]+)['\"]"
```

| Part           | Meaning                                                                                      |
|----------------|----------------------------------------------------------------------------------------------|
| `(?i)`         | Case-insensitive matching (so `<A>` or `<a>` both match).                                    |
| `<`            | Matches the literal `<` character (start of an HTML tag).                                    |
| `(?:a\|link)`  | Non-capturing group: matches either `a` or `link` (so `<a>` or `<link>` tags).              |
| `[^>]+`        | One or more characters that are not `>` (stays inside the tag, matches attributes before href).|
| `href`         | Matches the literal string `href`.                                                           |
| `\s*=\s*`      | Matches `=` with optional whitespace around it.                                              |
| `['"]`         | Matches a single or double quote (start of the href value).                                  |
| `([^'"]+)`     | Capturing group: matches the actual URL (any chars except quotes).                           |
| `['"]`         | Matches the closing quote (single or double).                                                |
