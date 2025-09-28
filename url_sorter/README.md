# URL Shortener 🔗

This is a **Python-based URL shortener** with a **MySQL database** backend.
It lets users **sign up, sign in, shorten URLs, retrieve original URLs, and track analytics** (click count, last clicked, IP, user agent).

---

## Features

* **User Authentication**

  * Sign up with username, email, and password.
  * Sign in with credentials.
* **Short URL Generation**

  * Generates unique alphanumeric short codes.
* **Analytics Tracking**

  * Logs each click with:

    * IP address
    * User agent
    * Timestamp
  * Shows total clicks and last clicked time per URL.
* **CLI Options**

  * Add a new URL.
  * Open a short URL.
  * View analytics after each access.

---

## How It Works

1. **User signs up or signs in.**
2. **Add URL** → Generates a short code and stores it in DB.
3. **Open URL** → Retrieves original URL, logs analytics, and shows stats.
4. **Analytics** → Displays total clicks and last clicked timestamp.

---

## Database Schema

### 1. `users` table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

### 2. `urls` table

```sql
CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    original_url TEXT NOT NULL,
    short_code VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 3. `analytics` table

```sql
CREATE TABLE analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url_id INT NOT NULL,
    ip_address VARCHAR(50),
    user_agent VARCHAR(255),
    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (url_id) REFERENCES urls(id)
);

✍️ **Author:** Harshvardhan Sanadhya
