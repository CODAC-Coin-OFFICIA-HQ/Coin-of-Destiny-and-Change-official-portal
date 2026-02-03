import sqlite3
import os
import time
from datetime import datetime

class TaskRaceEngine:
    def __init__(self):
        self.db_path = os.path.expanduser("~/codac-coin_portal/database/codac_master.db")
        self.PERFECT_20_LIMIT = 20 # Only Top 20 matter for the special batch

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def mark_task_complete(self, user_id, task_type):
        """
        Tasks: 'TRADING', 'YOUTUBE', 'MERCHANT'
        """
        conn = self._connect()
        cursor = conn.cursor()

        # 1. Create task tracking table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_tasks (
                user_id TEXT PRIMARY KEY,
                trading_done BOOLEAN DEFAULT 0,
                youtube_done BOOLEAN DEFAULT 0,
                merchant_done BOOLEAN DEFAULT 0,
                tasks_completed_at REAL DEFAULT NULL
            )
        """)

        # Ensure user is in table
        cursor.execute("INSERT OR IGNORE INTO user_tasks (user_id) VALUES (?)", (user_id,))

        # 2. Mark specific task
        column_map = {"TRADING": "trading_done", "YOUTUBE": "youtube_done", "MERCHANT": "merchant_done"}
        col = column_map.get(task_type)
        
        if col:
            cursor.execute(f"UPDATE user_tasks SET {col} = 1 WHERE user_id = ?", (user_id,))
            print(f" [✅] {user_id}: Completed {task_type} Task.")

        # 3. CHECK IF ALL TASKS DONE
        cursor.execute("SELECT trading_done, youtube_done, merchant_done FROM user_tasks WHERE user_id=?", (user_id,))
        row = cursor.fetchone()

        if row and all(row): # If all 3 are True
            # Check if already finished
            cursor.execute("SELECT tasks_completed_at FROM user_tasks WHERE user_id=?", (user_id,))
            if cursor.fetchone()[0] is None:
                completion_time = time.time()
                cursor.execute("UPDATE user_tasks SET tasks_completed_at = ? WHERE user_id = ?", (completion_time, user_id))
                print(f" [🏆] RACE FINISHED! {user_id} completed ALL TASKS!")

        conn.commit()
        conn.close()

    def generate_perfect_20_ranking(self):
        conn = self._connect()
        cursor = conn.cursor()

        print("\n=========================================================")
        print("      🏁 CODAC PERFECT 20 LEADERBOARD")
        print("      Criteria: Speed of Task Completion")
        print("=========================================================")

        cursor.execute("""
            SELECT user_id, tasks_completed_at
            FROM user_tasks
            WHERE tasks_completed_at IS NOT NULL
            ORDER BY tasks_completed_at ASC
            LIMIT ?
        """, (self.PERFECT_20_LIMIT,))

        rankings = cursor.fetchall()

        if not rankings:
            print(" [ℹ️] No qualifiers yet. Race is ongoing.")
        else:
            print(f" {'RANK':<5} | {'USER ID':<25} | {'TIME'}")
            print("-" * 50)
            for rank, (uid, finish_time) in enumerate(rankings, 1):
                ft_str = datetime.fromtimestamp(finish_time).strftime('%H:%M:%S')
                print(f" {rank:<5} | {uid:<25} | {ft_str}")

        conn.close()

if __name__ == "__main__":
    race = TaskRaceEngine()
    print(" [⚙️] RACE ENGINE READY. Waiting for task completions...")
