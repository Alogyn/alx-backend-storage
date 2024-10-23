# 0x01. NoSQL 📚

Welcome to the **NoSQL** project, part of the ALX Backend curriculum. In this project, you'll learn about NoSQL databases, particularly MongoDB, and how to manipulate data using MongoDB with Python.

## 📋 Learning Objectives

By completing this project, you will:

- Understand **NoSQL** and its differences from SQL databases.
- Learn about **ACID** properties.
- Explore **document storage** and **NoSQL types**.
- Learn how to **query**, **insert**, **update**, and **delete** information in MongoDB.
- Practice Python integration with MongoDB using **PyMongo**.

## 📂 Project Structure

This project contains the following tasks:

- **Task 0: List all databases**  
   - **File:** [0-list_databases](./0-list_databases)  
   - **Description:** Script that lists all databases in MongoDB.

- **Task 1: Create a database**  
   - **File:** [1-use_or_create_database](./1-use_or_create_database)  
   - **Description:** Script that creates or uses a database called `my_db`.

- **Task 2: Insert document**  
   - **File:** [2-insert](./2-insert)  
   - **Description:** Script that inserts a document in the `school` collection with the name "Holberton school".

- **Task 3: All documents**  
   - **File:** [3-all](./3-all)  
   - **Description:** Script that lists all documents in the `school` collection.

- **Task 4: All matches**  
   - **File:** [4-match](./4-match)  
   - **Description:** Script that lists all documents with `name="Holberton school"` in the `school` collection.

- **Task 5: Count**  
   - **File:** [5-count](./5-count)  
   - **Description:** Script that displays the number of documents in the `school` collection.

- **Task 6: Update**  
   - **File:** [6-update](./6-update)  
   - **Description:** Script that adds a new attribute `address` to the document with `name="Holberton school"`.

- **Task 7: Delete by match**  
   - **File:** [7-delete](./7-delete)  
   - **Description:** Script that deletes all documents with `name="Holberton school"`.

- **Task 8: List all documents in Python**  
   - **File:** [8-all.py](./8-all.py)  
   - **Description:** Python function that lists all documents in a collection.

- **Task 9: Insert a document in Python**  
    - **File:** [9-insert_school.py](./9-insert_school.py)  
    - **Description:** Python function that inserts a new document in the `school` collection.

- **Task 10: Change school topics**  
    - **File:** [10-update_topics.py](./10-update_topics.py)  
    - **Description:** Python function that updates the topics of a school document.

- **Task 11: Where can I learn Python?**  
    - **File:** [11-schools_by_topic.py](./11-schools_by_topic.py)  
    - **Description:** Python function that returns the list of schools having a specific topic.

- **Task 12: Log stats**  
    - **File:** [12-log_stats.py](./12-log_stats.py)  
    - **Description:** Python script that provides stats about Nginx logs stored in MongoDB.

- **Task 13: Regex filter**  
    - **File:** [100-find](./100-find)  
    - **Description:** Script that lists all documents with a name starting with "Holberton".

- **Task 14: Top students**  
    - **File:** [101-students.py](./101-students.py)  
    - **Description:** Python function that returns all students sorted by average score.

- **Task 15: Log stats - new version**  
    - **File:** [102-log_stats.py](./102-log_stats.py)  
    - **Description:** Python script that lists the top 10 most frequent IPs in the `nginx` collection.

## 📚 Resources

- [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
- [What is NoSQL?](https://www.mongodb.com/nosql-explained)
- [MongoDB with Python Crash Course](https://www.mongodb.com/quickstart/python-mongodb)
- [Aggregation in MongoDB](https://www.mongodb.com/docs/manual/aggregation/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/mongo/)

## ⚙️ Setup Instructions

1. **Install MongoDB on Ubuntu 18.04**:
   - First, add the MongoDB key:
     ```bash
     wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
     ```
   - Then, add MongoDB to your system's package source:
     ```bash
     echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
     ```
   - Update the package list:
     ```bash
     sudo apt-get update
     ```
   - Install MongoDB:
     ```bash
     sudo apt-get install -y mongodb-org
     ```
   - Start the MongoDB service:
     ```bash
     sudo service mongod start
     ```

2. **Install PyMongo**:
   - Install the PyMongo library to allow Python to communicate with MongoDB:
     ```bash
     pip3 install pymongo
     ```

3. **Verify MongoDB Installation**:
   - To verify that MongoDB is correctly installed, check the version:
     ```bash
     mongo --version
     ```

4. **Clone the repository**:
   - Clone this project to your local machine:
     ```bash
     git clone https://github.com/Alogyn/alx-backend-storage/0x01-NoSQL
     cd alx-backend-storage/0x01-NoSQL
     ```

5. **Run the MongoDB Scripts**:
   - You can run the MongoDB `.js` or `.sql` scripts using the following command:
     ```bash
     mongo <script_name>
     ```

6. **Run Python scripts**:
   - To run the Python scripts, make sure you have installed the necessary libraries and simply run them as:
     ```bash
     python3 <script_name.py>
     ```

7. **Using the MongoDB Shell**:
   - You can interact with MongoDB using its shell:
     ```bash
     mongo
     ```
   - In the shell, you can execute MongoDB commands, such as listing databases:
     ```bash
     show dbs
     ```
   - Switch to a specific database:
     ```bash
     use <database_name>
     ```

## 🧪 Running Tests

- For Python tasks, you can create and run unit tests using Python's built-in `unittest` library. Example:
  ```bash
  python3 -m unittest discover -s tests
  ```
- For MongoDB, ensure your test data is properly set up by writing mock data insertion scripts and testing queries.

## 📜 License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).

---

© 2024 [ALX](https://www.alxafrica.com/). All rights reserved.
