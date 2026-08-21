#!/usr/bin/env python3
import subprocess
import random
from datetime import datetime, timedelta
import os
import sys

def make_commit(date_str, count):
    """Make a commit with specified author and committer date."""
    for i in range(count):
        hour = random.randint(9, 21)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        timestamp = f"{date_str} {hour:02d}:{minute:02d}:{second:02d}"
        
        with open("commit_log.txt", "a") as f:
            f.write(f"Contribution on {timestamp} - commit #{i+1}\n")
            
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = timestamp
        env["GIT_COMMITTER_DATE"] = timestamp
        
        subprocess.run(["git", "add", "commit_log.txt"], check=True, env=env, stdout=subprocess.DEVNULL)
        subprocess.run(
            ["git", "commit", "-m", f"feat: daily contribution {timestamp}"],
            check=True,
            env=env,
            stdout=subprocess.DEVNULL
        )

def main():
    days = 365
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            pass
            
    print(f"Generating green graph contributions for the past {days} days...")
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    current_date = start_date
    total_commits = 0
    
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        commits_today = random.randint(2, 7)
        make_commit(date_str, commits_today)
        total_commits += commits_today
        current_date += timedelta(days=1)
        
    print(f"Success! Generated {total_commits} commits across {days} days.")

if __name__ == "__main__":
    main()
