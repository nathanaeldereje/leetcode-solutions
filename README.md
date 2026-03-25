# 💻 leetcode-solutions

This repository contains my accepted LeetCode solutions.

* **Languages:** Python, Pandas, Java, C++
* **Purpose:** Improve problem-solving and coding interview skills

---

## 🔐 Extracting LeetCode Session & CSRF Tokens

This guide explains how to safely extract your `LEETCODE_SESSION` and `csrftoken` from your browser. These tokens are commonly used for automation, API access, or personal tooling.

---

## 📌 Prerequisites

* A LeetCode account
* Logged into your account in a browser (Chrome, Edge, Brave, etc.)

---

## 🚀 Step-by-Step Guide

### 1. Log into LeetCode

Go to the LeetCode website and sign in to your account.

---

### 2. Open Developer Tools

You can open Developer Tools using:

* **Windows/Linux:** `F12` or `Ctrl + Shift + I`
* **Mac:** `Cmd + Option + I`

Or:

* Right-click anywhere on the page → click **Inspect**

---

### 3. Navigate to Cookies

1. Click on the **Application** tab
2. In the left sidebar:

   * Expand **Storage**
   * Click **Cookies**
   * Select `https://leetcode.com`

---

### 4. Locate Required Tokens

In the cookies table, find the following:

| Name               | Description              |
| ------------------ | ------------------------ |
| `LEETCODE_SESSION` | Your login session token |
| `csrftoken`        | CSRF protection token    |

---

### 5. Copy Token Values

* Click on each row
* Copy the value from the **Value** column

---

## ⚡ Alternative Method (Console)

1. Go to the **Console** tab in Developer Tools
2. Run:

```javascript
document.cookie
```

3. Look for:

* `LEETCODE_SESSION=...`
* `csrftoken=...`

4. Copy their values manually

---

## ⚠️ Security Notes

* These tokens act like **authentication credentials**
* **Do NOT share them publicly**
* They expire periodically
* Logging out will invalidate them


---

## 🛑 Disclaimer

Use these tokens responsibly. Automating actions on LeetCode may violate their terms of service if abused.

---

## ✅ Summary

You can extract your session and CSRF tokens directly from browser cookies using Developer Tools, and use them together to make authenticated requests. Handle them securely at all times.

---
