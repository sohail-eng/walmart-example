# walmart-example

A Python project to scrape seller offers from Walmart product pages using Playwright and Chrome DevTools Protocol. The script collects offer data for specified Walmart URLs and saves the results in both JSON and HJSON formats for easy analysis and human-friendly editing.

---

## Setup Instructions

### 1. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Running Chrome for Playwright

To allow Playwright to connect and extract cookies, you need to run Chrome with remote debugging enabled. Use the following command:

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-playwright --profile-directory="Default"
```

- This will open a Chrome window with a fresh user profile.
- Sign in to Chrome if needed.
- Manually visit walmart.com and log in if you want to scrape data as an authenticated user.

---

## How the Main Script Works

- The script in `main.py`:
  - Defines a list of Walmart product URLs (`urls_to_scrape`).
  - Uses Playwright to extract cookies from the first URL.
  - Scrapes all seller offers for each URL using those cookies.
  - Saves the results to both `records.json` (standard JSON) and `records.hjson` (human-friendly HJSON).

### To Test with Your Own URLs

1. Edit the `urls_to_scrape` list in `main.py` and add or replace product URLs.
2. Run the script:

```bash
python main.py
```

3. After execution, you’ll find:
   - `records.json` (machine-friendly)
   - `records.hjson` (human-friendly, supports comments, easier to edit)
