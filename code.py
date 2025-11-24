import datetime

class BPMonitor:
    """
    A class to manage and analyze blood pressure monitoring records.
    Readings are stored as a list of dictionaries.
    """
    def __init__(self):
        # Initialize an empty list to store all BP records
        # Each record is a dictionary: {'sys': int, 'dia': int, 'date': str}
        self.records = []
        self.load_sample_data() # Load some sample data for demonstration

    def load_sample_data(self):
        """Loads some initial data to demonstrate functionality."""
        print("Loading sample blood pressure data...")
        self.records.extend([
            {'sys': 125, 'dia': 82, 'date': '2025-10-20'},
            {'sys': 118, 'dia': 75, 'date': '2025-10-21'},
            {'sys': 135, 'dia': 90, 'date': '2025-10-22'},
            {'sys': 105, 'dia': 65, 'date': '2025-10-23'},
        ])

    def get_bp_category(self, systolic, diastolic):
        """
        Classifies the blood pressure reading based on American Heart Association (AHA) guidelines.
        [Image of blood pressure categories chart]
        """
        # Hypertension Crisis (Call doctor immediately)
        if systolic >= 180 or diastolic >= 120:
            return "Hypertensive Crisis (EMERGENCY)"
        # Stage 2 Hypertension
        elif (140 <= systolic < 180) or (90 <= diastolic < 120):
            return "Stage 2 Hypertension"
        # Stage 1 Hypertension
        elif (130 <= systolic < 140) or (80 <= diastolic < 90):
            return "Stage 1 Hypertension"
        # Elevated
        elif (120 <= systolic < 130) and (diastolic < 80):
            return "Elevated"
        # Normal
        elif systolic < 120 and diastolic < 80:
            return "Normal"
        # Other cases (e.g., isolated diastolic hypertension)
        else:
            return "Pre-Categorization (Consult a doctor)"


    def add_record(self, systolic, diastolic, date=None):
        """
        Adds a new blood pressure record to the system.

        Args:
            systolic (int): The systolic (top) pressure reading.
            diastolic (int): The diastolic (bottom) pressure reading.
            date (str, optional): The date of the reading. Defaults to today's date.
        """
        if date is None:
            date = datetime.date.today().strftime("%Y-%m-%d")

        try:
            sys_val = int(systolic)
            dia_val = int(diastolic)
            if sys_val < 50 or sys_val > 250 or dia_val < 30 or dia_val > 150:
                 raise ValueError("Readings seem unrealistic. Please check inputs.")
            
            record = {
                'sys': sys_val,
                'dia': dia_val,
                'date': date
            }
            self.records.append(record)
            category = self.get_bp_category(sys_val, dia_val)
            print(f"\n✅ Record added successfully on {date}. Category: {category}")
        
        except ValueError as e:
            print(f"\n❌ Error adding record: {e}. Please ensure inputs are valid integers.")


    def view_records(self):
        """Displays all recorded blood pressure readings."""
        if not self.records:
            print("\n-- No records found. Start by adding a reading. --")
            return

        print("\n" + "="*50)
        print("         BLOOD PRESSURE MONITORING RECORDS")
        print("="*50)
        print(f"{'Date':<12} {'Systolic':<10} {'Diastolic':<10} {'Category':<20}")
        print("-" * 50)

        # Sort records by date for better readability (most recent first)
        sorted_records = sorted(self.records, key=lambda x: x['date'], reverse=True)

        for record in sorted_records:
            category = self.get_bp_category(record['sys'], record['dia'])
            print(f"{record['date']:<12} {record['sys']:<10} {record['dia']:<10} {category:<20}")
        print("-" * 50)


    def analyze_stats(self):
        """Calculates and displays statistics for all readings."""
        if not self.records:
            print("\n-- Cannot analyze. No records available. --")
            return

        sys_readings = [r['sys'] for r in self.records]
        dia_readings = [r['dia'] for r in self.records]
        
        # Calculations
        avg_sys = sum(sys_readings) / len(sys_readings)
        avg_dia = sum(dia_readings) / len(dia_readings)
        max_sys = max(sys_readings)
        min_sys = min(sys_readings)
        max_dia = max(dia_readings)
        min_dia = min(dia_readings)

        overall_category = self.get_bp_category(avg_sys, avg_dia)

        print("\n" + "="*40)
        print("           ANALYSIS SUMMARY")
        print("="*40)
        print(f"Total Readings: {len(self.records)}")
        print(f"\n{'Metric':<15} {'Systolic':<10} {'Diastolic':<10}")
        print("-" * 35)
        print(f"{'Average:':<15} {avg_sys:.1f}:<10 {avg_dia:.1f}:<10")
        print(f"{'Max:':<15} {max_sys:<10} {max_dia:<10}")
        print(f"{'Min:':<15} {min_sys:<10} {min_dia:<10}")
        print("-" * 35)
        print(f"Overall Status based on Average: {overall_category}")
        print("="*40)

    def run_cli(self):
        """Runs the command-line interface for the system."""
        print("===========================================")
        print("  🩸 Blood Pressure Monitoring System v1.0 🩺")
        print("===========================================")
        
        while True:
            print("\nSelect an option:")
            print("1: Add New Reading")
            print("2: View All Records")
            print("3: Analyze Statistics")
            print("4: Exit System")
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                try:
                    sys = input("Enter Systolic (e.g., 120): ")
                    dia = input("Enter Diastolic (e.g., 80): ")
                    date = input("Enter Date (YYYY-MM-DD, or leave blank for today): ") or None
                    self.add_record(sys, dia, date)
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif choice == '2':
                self.view_records()
            
            elif choice == '3':
                self.analyze_stats()
            
            elif choice == '4':
                print("\nThank you for using the Blood Pressure Monitoring System. Goodbye!")
                break
            
            else:
                print("\n❌ Invalid choice. Please select a number between 1 and 4.")

# Entry point of the program
if __name__ == "__main__":
    monitor = BPMonitor()

    monitor.run_cli()

