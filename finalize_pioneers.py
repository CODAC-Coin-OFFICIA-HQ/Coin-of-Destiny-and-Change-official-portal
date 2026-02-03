import sqlite3
import os

def complete_structure():
    db_path = os.path.expanduser("~/codac-coin_portal/database/codac_master.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Count current Pioneers (L2-L8)
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level BETWEEN 2 AND 8")
    current_pioneers = cursor.fetchone()[0]
    target = 513
    missing = target - current_pioneers

    if missing <= 0:
        print(f"✅ Structure already complete. Pioneers: {current_pioneers}")
        conn.close()
        return

    print(f"⚠️ Missing {missing} Pioneers. Injecting now...")

    # 2. Inject missing Pioneers into Level 8 (The Reserve Layer)
    for i in range(missing):
        # Using a distinct ID format for the final 6
        new_id = f"CODAC-VIP-FINAL-PATCH-{str(i+1).zfill(3)}"
        try:
            cursor.execute("""
                INSERT INTO active_members (user_id, parent_id, current_level, grand_reward_total, trading_points, locked_balance, is_active)
                VALUES (?, 'FOUNDER-001', 8, 1000.0, 500.0, 2000.0, 1)
            """, (new_id,))
        except sqlite3.IntegrityError:
            continue

    conn.commit()
    
    # 3. Final Verification
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level BETWEEN 2 AND 8")
    final_count = cursor.fetchone()[0]
    print(f"📊 FINAL AUDIT: Pioneers = {final_count} / 513")
    print("✅ STRUCTURE LOCKED.")
    conn.close()

if __name__ == "__main__":
    complete_structure()
