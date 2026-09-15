# 📰 News Headline Aggregator

An automated DevOps-based news aggregation pipeline that extracts
latest news headlines, transforms the data using Pandas, and loads
the results into MySQL.

The complete pipeline is orchestrated using Prefect and integrated
with Jenkins for CI/CD automation.

---

## 🏗️ Architecture

GNews API
    ↓
Python Requests
    ↓
Pandas Transformation
    ↓
MySQL
    ↓
Prefect
    ↓
Jenkins CI/CD
    ↓
GitHub

---

## 🚀 Project Workflow

1. Developer pushes code to GitHub.
2. GitHub webhook triggers Jenkins.
3. Jenkins checks out the source code.
4. Jenkins creates a Python virtual environment.
5. Project dependencies are installed.
6. Pytest executes automated tests.
7. Python source files are validated.
8. Jenkins triggers the Prefect deployment.
9. Prefect Worker executes the pipeline.
10. News headlines are fetched from GNews API.
11. Pandas transforms and cleans the data.
12. Data is loaded into MySQL.
13. URL hashing prevents duplicate headlines.
14. Prefect reports the final flow status.
15. Jenkins waits until the Prefect flow completes.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Requests | API data extraction |
| Pandas | Data transformation |
| MySQL | Data storage |
| Prefect | Workflow orchestration |
| Jenkins | CI/CD automation |
| Git | Version control |
| GitHub | Source code management |
| Pytest | Automated testing |
| Linux | Server environment |
| AWS EC2 | Infrastructure |

---

## 📂 Project Structure

```text
news-headline-aggregator/
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── flow.py
│
├── tests/
│   └── test_pipeline.py
│
├── .env
├── .gitignore
├── .prefectignore
├── prefect.yaml
├── requirements.txt
├── Jenkinsfile
└── README.md
