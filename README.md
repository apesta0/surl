# 🔗 SURL (Shortened Uniform Resource Locator)

A simple URL shortener built using Python with minimal dependencies.  
It converts long URLs into short codes and stores them in a local SQLite database.

---

## 🚀 Features

- Shorten long URLs into 6-character codes
- Expand short codes back to original URLs
- Local SQLite database storage
- No external dependencies (only Python standard library)
- Collision-safe code generation

---

## ⚙️ How It Works

### Shorten URL
- Generates a random 6-character code
- Stores mapping in SQLite database

### Expand URL
- Looks up the short code
- Returns original URL if found

---

## ▶️ How to Run

### 1. Clone or download project
```bash
git clone git clone https://github.com/apesta0/surl.git   
cd surl
```

### 2. Run The App

```bash
python3 main.py
```

## 🧪 Example Usage

```bash
--- URL Shortener ---
1. Shorten URL
2. Expand URL
3. Exit

Choose: 1
Enter URL: https://example.com/very/long/link
Short code: Ab92xZ

Choose: 2
Enter short code: Ab92xZ
Original URL: https://example.com/very/long/link
```

