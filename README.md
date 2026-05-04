# Student Management System

A full-featured Student Management System with a **Streamlit web app** backed by **MongoDB**. Supports student login, grade tracking, GPA monitoring, ranking, and a complete admin panel for enrollment, analytics, and record management.

## Features

- Secure login for both students and admins
- Student dashboard with grades, GPA, stats, rank, and enrolled courses
- Admin panel for enrolling new students with course registration
- Student directory with all enrolled students
- Top scores view — max, min, and average marks per course
- Edit / Drop — update any student's data and course marks inline
- Analytics — per-course pass/fail counts, averages, and mark ranges
- MongoDB-backed data with a ready-to-import JSON collection

## How the Program Works

Run the Streamlit web app and log in as either a student or admin.

- Enter your **full name** and **password** on the login page
- **Admins** log in with name `Admin` and password `123` — they are redirected to the Admin Panel
- **Students** log in with their registered full name and numeric password — they are redirected to the Student Page
- All data is fetched live from MongoDB on every interaction

### Student Page

| Feature | Description |
|---|---|
| My Grades | Table of all enrolled courses with marks and grade |
| My GPA | Semester, Semester GPA, and CGPA with progress bars |
| My Stats | Best subject, weakest subject, and overall average marks |
| My Rank | Dense rank within the student's program and semester |
| My Courses | Enrolled course list with instructor, credit hours, and total credits |

### Admin Page

| Feature | Description |
|---|---|
| Enroll | Register a new student, set their info, and add courses one by one |
| Directory | View all students — ID, name, semester, section, CGPA, and status |
| Scores | Per-course top scorer, max marks, min marks, and average |
| Edit / Drop | Search a student by ID, edit any field or course mark, and save |
| Analytics | Pass/fail count, max, min, and average marks per course |

---

## How to Run Locally

### Prerequisites

- Python 3.9+
- A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account (or local MongoDB instance)
- MongoDB Compass (optional, for importing the sample collection)

### MongoDB Setup

1. Create a database named **`SMS`** with a collection named **`Students`**.
2. Import `SMS.Students.json` into the `Students` collection using MongoDB Compass  
   *(File → Import Data → select `SMS.Students.json`)*
3. Copy your MongoDB connection string.
4. Create a `.env` file in the project root:

```
url=mongodb+srv://<username>:<password>@cluster.mongodb.net/
```

---

### Option 1: Install with pip

1. Clone the repository and navigate to the project folder.

2. Install dependencies:

```bash
pip install streamlit pymongo python-dotenv pandas
```

3. Run the web app:

```bash
streamlit run webapp.py
```

---

### Option 2: Install with uv

1. Install **uv** (if not already installed):

```bash
pip install uv
```

2. Sync the project environment:

```bash
uv sync
```

3. Run the web app:

```bash
uv run streamlit run webapp.py
```

---

Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## Sample Document

Below is a sample student document as stored in the MongoDB `Students` collection:

```json
{
  "_id": {
    "$oid": "69f44ad9d429a8abad8c1c4e"
  },
  "studentId": "2026-CS-001",
  "fullName": "Ali Raza",
  "password": 1234,
  "program": "BSCS",
  "semester": 2,
  "section": "A",
  "semesterGPA": 3.6,
  "cgpa": 3.5,
  "status": "Active",
  "enrolledCourses": [
    {
      "courseCode": "CS101",
      "courseName": "Programming Fundamentals",
      "instructor": "Dr. Ahmed",
      "creditHours": 3,
      "marksObtained": 88,
      "totalMarks": 100,
      "grade": "A"
    },
    {
      "courseCode": "MTH101",
      "courseName": "Calculus",
      "instructor": "Sir Bilal",
      "creditHours": 3,
      "marksObtained": 76,
      "totalMarks": 100,
      "grade": "B+"
    },
    {
      "courseCode": "ENG101",
      "courseName": "English Composition",
      "instructor": "Ms. Sana",
      "creditHours": 2,
      "marksObtained": 91,
      "totalMarks": 100,
      "grade": "A"
    }
  ]
}
```

### Document Field Reference

| Field | Type | Description |
|---|---|---|
| `studentId` | String | Unique student identifier (e.g. `2026-CS-001`) |
| `fullName` | String | Student's full name — used as login username |
| `password` | Integer | Numeric password for student login |
| `program` | String | Degree program — one of `BSCS`, `BSE`, `BBA`, `BSAI`, `BSEE` |
| `semester` | Integer | Current semester (1–8) |
| `section` | String | Section — `A` or `B` |
| `semesterGPA` | Float | GPA for the current semester (0.0–4.0) |
| `cgpa` | Float | Cumulative GPA (0.0–4.0) |
| `status` | String | `Active` or `Passive` — only Active students can log in |
| `enrolledCourses` | Array | List of course objects (see below) |
| `enrolledCourses.courseCode` | String | Short course identifier (e.g. `CS101`) |
| `enrolledCourses.courseName` | String | Full name of the course |
| `enrolledCourses.instructor` | String | Instructor's name |
| `enrolledCourses.creditHours` | Integer | Credit hours for the course |
| `enrolledCourses.marksObtained` | Integer | Marks scored out of `totalMarks` |
| `enrolledCourses.totalMarks` | Integer | Total marks available (typically 100) |
| `enrolledCourses.grade` | String | Letter grade (e.g. `A`, `B+`) — set by admin via Edit |

---

## File Structure

```
Student-Management/
│── main.py               # All MongoDB query functions
│── webapp.py             # Login page (entry point)
│── pages/
│   ├── students.py       # Student dashboard
│   └── adminpage.py      # Admin panel
│── SMS.Students.json     # Sample MongoDB collection — import into Compass
│── pyproject.toml
│── uv.lock
│── .python-version
│── README.md
```

> **`SMS.Students.json`** — This is the MongoDB collection export. Import it into your `SMS` database under the `Students` collection using MongoDB Compass to get started with sample data immediately.

---

## Technologies Used

- Python
- [Streamlit](https://streamlit.io/) — Web UI framework
- [PyMongo](https://pymongo.readthedocs.io/) — MongoDB driver
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) — Cloud database
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management
- [Pandas](https://pandas.pydata.org/) — Data display and formatting

---


## Notes
 
- Only students with **`status: Active`** can log in — students marked as `Passive` will be denied access even with correct credentials.
- Admin credentials are fixed: name **`Admin`**, password **`123`**. These are checked in `webapp.py` and are not stored in the database.
- Student passwords are stored as **integers** in MongoDB — entering a non-numeric password on the login page will always fail.
- **Grades are not auto-calculated** — they must be set manually by the admin through the Edit / Drop panel after entering marks.
- The `.env` file is **not included** in the repository. You must create it manually with your MongoDB connection string before running the app, otherwise the app will fail to connect to the database.
- The `SMS.Students.json` file must be **imported into MongoDB before running** the app — the app has no fallback if the collection is empty or missing.
- **Ranking uses dense rank** — if two students share the same CGPA, they receive the same rank and the next rank is not skipped.
- Marks entered via the Edit / Drop panel are saved directly to MongoDB — there is no confirmation step beyond clicking **Update Student**.

---

## Author

Muhammad Awais Tariq

---

If you like this project, consider giving it a star ⭐