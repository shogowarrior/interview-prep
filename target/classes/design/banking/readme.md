# 📃 Banking System

A multi-tiered in-memory banking system built with Java and Spring Boot. This system supports basic account operations, analytics, scheduled actions, logging, and memory-budgeting, all exposed via RESTful APIs.

---

## ✅ Features

* Deposit & transfer money between accounts
* Top-K richest accounts analytics
* Scheduled transfers with async logging
* Account merging
* In-memory data store (can be persisted)
* Memory control with max transactions/account
* REST API with error handling and pagination

---

## 📅 Tech Stack

* Java 17+
* Spring Boot
* ConcurrentHashMap & synchronized structures for thread safety

---

## 📆 REST API Endpoints

### ⭐ Account Operations

| Method | Endpoint                               | Description    |
| ------ | -------------------------------------- | -------------- |
| POST   | `/api/account/{id}/deposit?amount=100` | Deposit funds  |
| POST   | `/api/transfer?from=A&to=B&amount=50`  | Transfer funds |

### 📊 Analytics & Logs

| Method | Endpoint                           | Description              |
| ------ | ---------------------------------- | ------------------------ |
| GET    | `/api/top-accounts?page=0&size=10` | Paginated top-K accounts |
| GET    | `/api/logs?page=0&size=10`         | Paginated scheduler logs |

### ⏳ Scheduling

| Method | Endpoint                                                     | Description                       |
| ------ | ------------------------------------------------------------ | --------------------------------- |
| POST   | `/api/schedule-transfer?from=A&to=B&amount=30&delayMs=10000` | Schedule transfer with delay (ms) |

### ♻️ Account Management

| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| POST   | `/api/merge?from=A&to=B` | Merge account A into B |

---

## 📂 Pagination

Paginated endpoints accept `page` (0-based) and `size` query parameters:

```http
GET /api/top-accounts?page=1&size=5
```

---

## ⚠️ Error Handling

Standard Spring `ResponseStatusException` is used to throw `400 Bad Request` on:

* Invalid deposit/transfer amounts
* Transfer failure due to insufficient funds

---

## 📁 Memory & Compute

* Account transactions are pruned via `MemoryManager`
* Scheduler executes delayed transfers using thread pool
* `ConcurrentHashMap` ensures thread-safe operations

---

## 💼 Future Extensions

* Persistent DB integration (JPA or NoSQL)
* Authentication & authorization
* UI frontend with monitoring dashboard
* Event-based architecture for high scalability

---

## 📄 License

MIT License. Built for learning and architectural practice.
