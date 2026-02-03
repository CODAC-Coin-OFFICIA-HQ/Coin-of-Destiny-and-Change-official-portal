import os
import shutil
import datetime

# --- CODAC COIN SYSTEM CLEANUP PROTOCOL ---
# Purpose: Archive old/backup files to secure the Final Production Environment.
# Governance: Data Privacy & Asset Protection

# 1. Setup Archive Directory
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
archive_dir = f"CODAC_ARCHIVE_{timestamp}"

if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)
    print(f"✅ Created Safe Archive Vault: {archive_dir}")

# 2. Define the STRICT LIST of Production Files (The "White List")
# These are the files from your Master List that we KEEP in the main folder.
PRODUCTION_ASSETS = [
    "app.py",
    "codac_secrets.py", 
    "secrets.py",
    "graduation_engine_smart.py",
    "global_viral_engine.py",
    "merchant_spending_logic.py",
    "task_race_engine.py", # If exists
    "mother_tree.db", 
    "CODAC_MASTER_LEDGER.pdf",
    "CODAC_CENTRAL_BANKING_PLAN.pdf",
    "homepage.html",
    "dashboard.html",
    "business.html",
    "cycle2_rewards.html",
    "cdc_logo.jpg",
    "templates", # Folder
    "static", # Folder
    "database", # Folder
    "system_cleanup_protocol.py",
    ".gitignore",
    "requirements.txt"
]

# 3. Execution Logic
files_moved = 0
current_files = os.listdir('.')

print("🔒 Starting System Isolation...")

for filename in current_files:
    # Skip the archive dir itself and directories (unless we want to move specific folders)
    if filename == archive_dir:
        continue
    
    # If it's a folder (like __pycache__ or old backups), check if it's in whitelist
    if os.path.isdir(filename):
        if filename not in PRODUCTION_ASSETS:
            # We skip moving folders for safety in this step, focusing on loose files
            pass 
        continue

    # If the file is NOT in the Production White List, move it.
    if filename not in PRODUCTION_ASSETS:
        try:
            source = filename
            destination = os.path.join(archive_dir, filename)
            shutil.move(source, destination)
            print(f"📦 Archived: {filename}")
            files_moved += 1
        except Exception as e:
            print(f"⚠️ Could not archive {filename}: {e}")

print("-" * 30)
print(f"✅ Cleanup Complete. {files_moved} files moved to {archive_dir}.")
print("🚀 The Main Directory is now ready for the Final Run.")
