# 🚀 LLM Cost Tracker

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![CLI](https://img.shields.io/badge/interface-CLI-green)
![License](https://img.shields.io/badge/license-MIT-orange)

A pip-installable Python CLI tool to track, log, and analyze LLM token usage and cost.

## ✨ Features

- 📊 Track LLM token usage and cost
- 🧾 Store usage logs in JSON format
- 📅 View daily usage reports (`--today`)
- 🚨 Set cost limits and get alerts (`--limit`)
- 📤 Export usage data to CSV (`--export`)
- ⚡ Simple and fast CLI interface

## 💡 Use Cases

- Monitor OpenAI / LLM API spending
- Track usage across projects or teams
- Prevent unexpected API costs
- Analyze usage trends over time
  
## Installation

```bash
pip install -e .
## 🚀 Usage

### Track usage
```bash
llm-tracker --tokens 2000
Generate Report
llm-tracker --report
📊 Example Output
Cost: $0.004000

----- LLM Usage Report -----
Total Requests: 3
Total Tokens Used: 7000
Total Cost: $0.014000

👨‍💻 Author
Purnima Singh
