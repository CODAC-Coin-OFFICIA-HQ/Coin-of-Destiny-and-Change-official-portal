import sqlite3
import os

class SmartGraduationEngine:
    def __init__(self):
        # Dummy path for simulation if DB is busy, creates a file if missing
        self.db_path = "codac_test.db"

    def calculate_required_usdt(self, current_level):
        base = 18888.0
        if current_level == 1: return base
        elif 2 <= current_level <= 17: return base + ((current_level - 1) * 10000.0)
        elif current_level == 18: return 0.0 # Hayahay
        return 999999.0
