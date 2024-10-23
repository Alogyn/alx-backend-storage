# 0x02. Redis Basic 🛠️

![Redis](https://img.shields.io/badge/Redis-InMemoryDB-red?style=flat-square&logo=redis) ![Python](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=python)

## 📖 Project Overview
This project introduces **Redis**, a powerful in-memory key-value store, and its usage with Python. You'll learn how to perform basic operations, implement caching, and work with Redis commands to build efficient applications.

## 🎯 Learning Objectives
- 🗄️ **Redis Basics**: Understand Redis operations for key-value management.
- 🚀 **Caching**: Learn how to use Redis as a caching mechanism.
- 🧑‍💻 **Redis in Python**: Apply Redis commands in Python to improve performance.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=python) **Python 3.7** on **Ubuntu 18.04 LTS**
- ![Redis](https://img.shields.io/badge/Redis-Database-red?style=flat-square&logo=redis) **Redis** key-value store
- ![Pycodestyle](https://img.shields.io/badge/Code-Style-green?style=flat-square&logo=python) **Pycodestyle** for Python code formatting
- **Redis Python Client** for Redis-Python interaction

## 📋 Requirements
- Python files must be interpreted/compiled on **Ubuntu 18.04 LTS** using `python3` (version 3.7).
- All Python files should end with a new line.
- Code must follow the `pycodestyle` style guide (version 2.5).
- Every module, class, and function must be well-documented.
- Functions and coroutines must be type-annotated.

## 🚀 Installation

1. Install Redis on Ubuntu:
    ```bash
    sudo apt-get -y install redis-server
    ```

2. Install Redis Python Client:
    ```bash
    pip3 install redis
    ```

3. Configure Redis:
    ```bash
    sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
    ```

4. Start Redis server in a container:
    ```bash
    service redis-server start
    ```

## 🏗️ Project Structure
- **Cache class**: Implements basic Redis operations.
- **Decorators**: Track method calls and store input/output histories.
- **Redis commands**: Use commands like `INCR`, `RPUSH`, `LPUSH`, `LRANGE`.

## 📌 Tasks

0. **Writing strings to Redis** ✏️:
    - Implement a `store` method to save data in Redis with a randomly generated key.

1. **Reading from Redis and recovering original type** 📜:
    - Implement a `get` method to retrieve stored data and convert it back to its original format.

2. **Incrementing values** 🔢:
    - Use the `INCR` command to count how many times methods are called using a custom decorator.

3. **Storing lists** 📝:
    - Implement a `call_history` decorator to store input/output lists for method calls.

4. **Retrieving lists** 📂:
    - Create a `replay` function to retrieve the history of method calls and their results.

5. **Expiring web cache and tracker (Advanced)** 🌐:
    - Implement a `get_page` function to track URL access frequency and cache the result with expiration.

## ⚙️ How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/Alogyn/alx-backend-storage/0x02-redis_basic#
    cd alx-backend-storage/0x02-redis_basic#
    ```

2. Run the Python files:
    ```bash
    python3 main.py
    ```

## 👨‍💻 Author
Mohamed Derfoufi  
📧 [Email](mailto:mohamed.derfoufi.tech@gmail.com) | 🌐 [Linkdin](https://www.linkedin.com/in/mohamed-derfoufi-b50566309/)
