import csv

class DataFrame:
    def __init__(self, data):
        self.data = data

    def select(self, columns):
        output = []

        for row in self.data:
            new_row = {}
            for col in columns:
                if col in row:
                    new_row[col] = row[col]
            output.append(new_row)

        return DataFrame(output)

    def filter(self, condition):
        filtered = []
        for row in self.data:
            if condition(row):
                filtered.append(row)

        return DataFrame(filtered)
    
    def show(self):
        for row in self.data:
            print(row)
        return self
    
    def group_by(self, key):
        grouped = {}
        for row in self.data:
            group_key = row.get(key)
            if group_key not in grouped:
                grouped[group_key] = []

            grouped[group_key].append(row)

        return grouped

def load_csv(filename):
    output = []

    try:
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                cleaned_row = {}

                for k, v in row.items():
                    if v.isdigit():
                        cleaned_row[k] = int(v)
                    else:
                        cleaned_row[k] = v

                output.append(cleaned_row)

    except FileNotFoundError:
        print("File not found.")

    return output

df = DataFrame(load_csv("student.csv"))

df.filter(lambda r: int(r["marks"]) > 80)\
  .select(["name", "marks"])\
  .show()