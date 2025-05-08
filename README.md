# News-Aggregator-for-Real-Client

# Argo: Web Presence Aggregator for QBG

## 📌 Executive Summary

**Argo** is a Python-based local web aggregation system developed for the **Qur’anic Botanic Garden (QBG)**. Its goal is to automate the process of collecting, storing, and cataloging online content such as news articles, social media posts, and event mentions related to QBG.

The system allows QBG to:
- Discover relevant content from the web.
- Archive this content via PDFs or snapshots.
- Store it in a searchable local database.
- Use this data for generating reports and analyzing influence.

---

## 🌿 Community Partner: QBG

QBG is a unique initiative backed by UNESCO and launched under the patronage of Her Highness Sheikha Moza. It aims to cultivate and document every plant species mentioned in the Holy Qur’an and Hadith.

**Key Points:**
- 60 documented plants, including 26 from the Qur’an.
- Located near Education City, Qatar.
- Engages in sustainability and environmental outreach.
- Lacks a dedicated IT department; technology is managed by a small team.

---

## 🖥️ Technology Infrastructure

- All systems run on **Windows**.
- QBG is connected to the **Qatar Foundation** internal network.
- No dedicated IT department; technical responsibilities handled by staff.
- A single dedicated machine is used to run the Argo application.

---

## ❗ Problem Analysis

QBG currently gathers web mentions manually, which includes:
- Searching Google.
- Copying and pasting links into spreadsheets.
- Archiving articles manually.

### Issues:
- Time-consuming and inefficient.
- High chance of human error and missing data.
- Expired links lead to data loss.
- Inability to generate quick, accurate reports for stakeholders.

Argo solves this by automating the data discovery, storage, and analysis process.

---

## 🔍 Rejected Alternatives

### 1. Java Application
- Lacks API support.
- High development complexity.
- Team lacks experience.

### 2. Marketing Firm
- Not cost-effective given QBG’s limited budget.
- Current online presence doesn’t justify outsourcing.

### 3. Open Source Solutions
- Too broad or too complex.
- Do not meet QBG’s specific requirements.

### 4. Web Application
- Not allowed due to internal policy and network security.
- QBG needs a local, offline-first tool.

---

## ✅ Chosen Solution

A **Python desktop application** was selected because:
- It supports the APIs required (Twitter, YouTube, web scraping, PDF generation).
- It is easy to maintain and extend.
- It leverages the team's existing skills.
- It avoids web hosting or infrastructure costs.
- It is secure and runs locally.

---

## 🛠️ Features

### Must-Have
- ✅ Local database to catalog QBG-related content.
- ✅ Store active links to online sources.
- ✅ Save web posts as PDFs or snapshots.
- ✅ Search database by date or time.
- ✅ Web scraping and API integration for automated discovery.

### Should-Have
- 🔄 Event categorization and tagging.
- 🔍 Search by event or tag.
- 📄 Preserve original visual formatting.
- 🚫 Duplicate detection.
- 📘 Installation guide and user manual.

### Could-Have
- 🔐 Login credentials.
- 🏷️ Manual tag addition.
- 📊 Event statistics.
- 📁 Save search results in exportable folders.

### Won’t-Have (Out of Scope)
- 📽️ Flash/YouTube downloading.
- 📈 Visual analytics dashboards.
- 🌐 Intranet/multi-device deployment.
- 📻 TV/radio content support.
- 🔒 Facebook/Snapchat/private social networks integration.

---

## 📋 Functional Requirements

- The system shall search the web for QBG-related content.
- It shall detect and highlight new posts not yet in the database.
- It shall allow the user to save snapshots or PDFs.
- It shall support tag- and time-based filtering.
- It shall display the number of posts related to events or tags.
- It shall ensure no duplicate entries are stored.

---

## 🚧 Limitations and Risks

- **API Rate Limits:** Can restrict data retrieval from services like Twitter or YouTube.
- **Expired Links:** Content may disappear over time without snapshots.
- **Manual Tagging:** Tagging still requires human input for accuracy.
- **No Live Syncing:** The system must be run manually or on a schedule.

---

## 🧩 System Modules

- **Scraper Module:** Fetches relevant posts via APIs and keyword searches.
- **Snapshot Module:** Saves HTML snapshots or PDFs of discovered content.
- **Database Module:** Stores and indexes content locally with metadata.
- **Search Interface:** Enables filtering by tag, date, and keyword.
- **Statistics Module:** Summarizes post frequency by category (future enhancement).

---

## 🧠 Future Improvements

- Add a better graphical user interface (GUI).
- Build a statistics dashboard.
- Integrate basic Natural Language Processing for smarter tagging.
- Add OCR for image-based content.

---

## 👥 Credits

**Community Partner:** QBG  
**Development Team:** Team Argo
