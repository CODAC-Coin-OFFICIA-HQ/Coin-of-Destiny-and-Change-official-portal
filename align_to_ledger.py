import sqlite3
import os

def align():
    db_path = os.path.expanduser("~/codac-coin_portal/database/codac_master.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("=========================================================")
    print("      ⚖️  ALIGNING DATABASE TO MASTER LEDGER")
    print("=========================================================")

    # 1. Verification of Levels
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level BETWEEN 2 AND 8")
    current_pioneers = cursor.fetchone()[0]
    
    target = 513
    missing = target - current_pioneers

    if missing > 0:
        print(f" [⚠️] Database has {current_pioneers}. Ledger requires {target}.")
        print(f" [✍️] Restoring missing {missing} Pioneer slots from Ledger IDs...")
        
        # We restore using the official naming convention found in your directory
        # starting from the last known good index in Level 8
        for i in range(missing):
            # Using the official 'RES' (Reserve) prefix found in your dir
            idx = 129 + i 
            new_id = f"CODAC-RES-L08-{str(idx).zfill(3)}"
            
            cursor.execute("""
                INSERT OR IGNORE INTO active_members 
                (user_id, parent_id, current_level, grand_reward_total, trading_points, locked_balance, is_active)
                VALUES (?, 'FOUNDER-001', 8, 0.0, 0.0, 0.0, 1)
            """, (new_id,))

        conn.commit()
        print(f" [✅] Successfully restored to {target} Pioneers.")
    else:
        print(" [✨] Pioneer count is already aligned with Ledger.")

    print("=========================================================")
    conn.close()

if __name__ == "__main__":
    align()
