from flask import Flask, request
import pandas as pd

app = Flask(__name__)

CSV_FILE = "students.csv"

# Function: Load CSV
def load_data():
    return pd.read_csv(CSV_FILE)

# Function: Save CSV
def save_data(df):
    df.to_csv(CSV_FILE, index=False)


# -------------------------
# 1️⃣ READ (GET) - show all data
# -------------------------
@app.route("/students", methods=["GET"])
def get_students():
    df = load_data()
    return df.to_dict(orient="records")


# -------------------------
# 2️⃣ CREATE (POST) - Add new student
# -------------------------
@app.route("/student", methods=["POST"])
def add_student():
    df = load_data()
    data = request.json

    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    save_data(df)

    return {"msg": "Student added", "data": data}


# -------------------------
# 3️⃣ UPDATE (PUT)
# -------------------------
@app.route("/student/<int:index>", methods=["PUT"])
def update_student(index):
    df = load_data()
    data = request.json

    df.loc[index] = data
    save_data(df)

    return {"msg": "Updated", "data": data}


# -------------------------
# 4️⃣ DELETE (DELETE)
# -------------------------
@app.route("/student/<int:index>", methods=["DELETE"])
def delete_student(index):
    df = load_data()
    deleted = df.loc[index].to_dict()

    df = df.drop(index).reset_index(drop=True)
    save_data(df)

    return {"msg": "Deleted", "data": deleted}


if __name__ == "__main__":
    app.run(debug=True)
