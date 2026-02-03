import sqlite3
import os

def surgical_purge():
    db_path = os.path.expanduser("~/codac-coin_portal/database/codac_master.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("=========================================================")
    print("      ✂️  SURGICAL PURGE: REMOVING ALL VIP IDs")
    print("=========================================================")

    # 1. DELETE ALL IDs CONTAINING 'VIP'
    cursor.execute("DELETE FROM active_members WHERE user_id LIKE '%VIP%'")
    deleted_count = cursor.rowcount
    print(f" [🗑️] Removed {deleted_count} VIP accounts.")

    # 2. FINAL AUDIT OF REMAINING NODES
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level=1")
    founder = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level BETWEEN 2 AND 8")
    pioneers = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM active_members WHERE current_level=9")
    countries = cursor.fetchone()[0]

    total = founder + pioneers + countries

    print("---------------------------------------------------------")
    print(f" 📊 CLEAN DATASET AUDIT:")
    print(f"    👑 Founder:   {founder}")
    print(f"    📜 Pioneers:  {pioneers} (Official Ledger Only)")
    print(f"    🌍 Countries: {countries}")
    print(f"    ✅ TOTAL NODES: {total}")
    print("=========================================================")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    surgical_purge()
