# GitHub Green Graph Generator 🟢

Automatically keep your GitHub contribution graph 100% green with past backfilled commits and automated daily commits via GitHub Actions.

## Features
- **Past Backfill**: Fill all grey squares in the past 365 days with commit activity.
- **Future Auto-Commit**: Continuous daily commits via GitHub Actions (no local computer required).
- **Varied Intensity**: Random commit counts per day (2–7 commits) for visual contrast (light green to dark green).

## Setup Instructions

### 1. Create a Repository on GitHub
1. Go to [GitHub - Create New Repository](https://github.com/new).
2. Name it `github-green-graph` (or any name you prefer).
3. Set visibility to **Public** (so contribution activity appears on your profile).
4. Do NOT check "Initialize this repository with a README".
5. Click **Create repository**.

### 2. Connect Local Repository & Push
Run the following commands in your terminal:

```bash
cd /Users/rahil/Developer/github-green-graph
git remote add origin https://github.com/thecodex110/github-green-graph.git
git push -u origin main --force
```

### 3. Ensure Workflow Permissions
1. Go to your repo on GitHub: `https://github.com/thecodex110/github-green-graph/settings/actions`
2. Scroll to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

---
*Created automatically by Antigravity AI Assistant.*
