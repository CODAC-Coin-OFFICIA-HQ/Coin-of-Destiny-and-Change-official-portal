import sqlite3
import os

def restore():
    db_path = os.path.expanduser("~/codac-coin_portal/database/codac_master.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Check current count
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level BETWEEN 2 AND 8")
    current = cursor.fetchone()[0]
    target = 513
    needed = target - current

    print(f"Current Pioneers: {current}")
    print(f"Restoring {needed} slots to reach 513...")

    # 2. Add missing Pioneers using the Official RES format from your file dir
    for i in range(needed):
        # We start naming from where the last one likely left off or 129+
        new_id = f"CODAC-RES-L08-{str(i+200).zfill(3)}" 
        cursor.execute("""
            INSERT OR IGNORE INTO active_members 
            (user_id, parent_id, current_level, grand_reward_total, trading_points, locked_balance, is_active)
            VALUES (?, 'FOUNDER-001', 8, 0.0, 0.0, 0.0, 1)
        """, (new_id,))

    conn.commit()
    
    # 3. Final Verification
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level BETWEEN 2 AND 8")
    p_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level = 9")
    c_count = cursor.fetchone()[0]
    
    print("========================================")
    print(f" ✅ RESTORED TOTAL: {p_count + c_count}")
    print(f" 👑 Pioneers: {p_count} / 513")
    print(f" 🌍 Countries: {c_count} / 204")
    print("========================================")
    conn.close()

if __name__ == "__main__":
    restore()
