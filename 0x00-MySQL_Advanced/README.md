# 0x00. MySQL Advanced 📊

Welcome to the **MySQL Advanced** project! This project covers advanced database management techniques using MySQL. You will learn to create tables with constraints, optimize queries, and explore stored procedures, views, and triggers.

## 📝 Learning Objectives

By completing this project, you will:

- 🔍 **Master Table Constraints:** Learn to create tables with constraints such as `UNIQUE`, `FOREIGN KEY`, and `CHECK`.
- ⚡ **Optimize Query Performance:** Use indexes to improve the speed and efficiency of database queries.
- 🛠️ **Implement Stored Procedures and Functions:** Create stored procedures and functions to handle complex database operations.
- 👁️ **Use Views:** Learn how to create views to simplify complex queries.
- ⏰ **Create Triggers:** Automate tasks with database triggers that execute in response to specific actions.

## 📚 Resources

### Read or Watch:

- 📘 [MySQL 5.7 Reference Manual](https://dev.mysql.com/doc/refman/5.7/en/)
- 🎥 [Database Indexing for Performance](https://www.youtube.com/watch?v=7vbnyYXy2ow)
- 📄 [Stored Procedures in MySQL](https://www.mysqltutorial.org/mysql-stored-procedure-tutorial.aspx)
- 📄 [MySQL Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- 📘 [MySQL Views](https://www.mysqltutorial.org/mysql-views-tutorial.aspx)
- 🎥 [Optimizing MySQL Queries](https://www.youtube.com/watch?v=FUPaKXLZzD0)
- 📘 [MySQL Constraints](https://www.mysqltutorial.org/mysql-constraints.aspx)

## 📂 Project Structure

This project includes the following tasks:

0. **Task 0: Unique Table**  
   - **File:** [0-unique_table.sql](./0-unique_table.sql)  
   - **Description:** Create a table with a `UNIQUE` constraint on specific columns.

1. **Task 1: Index Optimization**  
   - **File:** [1-index_optimization.sql](./1-index_optimization.sql)  
   - **Description:** Add indexes to optimize query performance for frequently accessed data.

2. **Task 2: Stored Procedure**  
   - **File:** [2-stored_procedure.sql](./2-stored_procedure.sql)  
   - **Description:** Write a stored procedure to automate a common task in the database.

3. **Task 3: View Creation**  
   - **File:** [3-view_creation.sql](./3-view_creation.sql)  
   - **Description:** Create a view to simplify a complex query by aggregating results from multiple tables.

4. **Task 4: Trigger Automation**  
   - **File:** [4-trigger_automation.sql](./4-trigger_automation.sql)  
   - **Description:** Implement a trigger that automatically updates a table when a specific event occurs.

5. **Task 5: Foreign Key**  
   - **File:** [5-foreign_key.sql](./5-foreign_key.sql)  
   - **Description:** Create a table with a foreign key constraint linking it to another table.

6. **Task 6: Join Optimization**  
   - **File:** [6-join_optimization.sql](./6-join_optimization.sql)  
   - **Description:** Optimize a query involving multiple table joins.

7. **Task 7: Advanced Stored Procedure**  
   - **File:** [7-advanced_stored_procedure.sql](./7-advanced_stored_procedure.sql)  
   - **Description:** Write an advanced stored procedure that accepts parameters and returns a result set.

8. **Task 8: Data Validation Trigger**  
   - **File:** [8-data_validation_trigger.sql](./8-data_validation_trigger.sql)  
   - **Description:** Create a trigger to validate data before it’s inserted into a table.

9. **Task 9: Complex Query Using Views**  
    - **File:** [9-complex_view.sql](./9-complex_view.sql)  
    - **Description:** Create a complex view involving multiple tables and joins.

10. **Task 10: Query with Subqueries**  
    - **File:** [10-query_with_subqueries.sql](./10-query_with_subqueries.sql)  
    - **Description:** Write a complex query using subqueries for better data aggregation.

11. **Task 11: Transactions**  
    - **File:** [11-transactions.sql](./11-transactions.sql)  
    - **Description:** Implement a transaction mechanism that ensures data integrity.

12. **Task 12: Rollback Mechanism**  
    - **File:** [12-rollback_mechanism.sql](./12-rollback_mechanism.sql)  
    - **Description:** Write a transaction with a rollback feature to revert changes on failure.

13. **Task 13: User Privileges**  
    - **File:** [13-user_privileges.sql](./13-user_privileges.sql)  
    - **Description:** Manage user privileges and permissions on specific tables and databases.

## ⚙️ Setup Instructions

1. **Install MySQL 5.7**:
   - To install MySQL on Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install mysql-server
     sudo mysql_secure_installation
     ```

2. **Clone the repository**:
   - Clone this project to your local machine:
     ```bash
     git clone https://github.com/Alogyn/alx-mysql-advanced.git
     cd alx-mysql-advanced
     ```

3. **Run SQL files**:
   - To execute any of the SQL files, use the following command:
     ```bash
     mysql -u root -p < filename.sql
     ```

## 📜 License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).

---

© 2024 [ALX](https://www.alxafrica.com/). All rights reserved.
