# 📝 Takser

A simple command-line task manager to keep track of your to-dos! This tool allows you to add, remove, sort, and update the status of tasks directly from your terminal. 🚀

*(Yes, I know "Tasker" is the correct spelling, but I made a mistake on purpose — because creativity matters!)* 😎

## 📌 Features

- Add new tasks ✅
- Remove tasks ❌
- List all tasks 🗂️
- Mark tasks as "done" ✅ or "in progress" ⏳
- Sort tasks by ID, text, or status 🔀
- Beautiful CLI output with bold and strikethrough formatting ✨

## 📥 Installation

Clone the repository and navigate to the project directory:

```sh
$ git clone https://github.com/VolDenMaks1/Takser.git
$ cd Takser
$ chmod +x install.sh 
$ sudo ./install.sh
```

## 🚀 Usage

Run the script with different commands to manage your tasks.

### 🏷️ List all tasks

```sh
$ takser
```

### ➕ Add new tasks

```sh
$ takser add "Buy groceries" "Finish project"
```

### ❌ Remove tasks by ID

```sh
$ takser remove 1 3
```

### ✅ Mark tasks as done

```sh
$ takser done 2
```

### ⏳ Mark tasks as in progress

```sh
$ takser in progress 4
```

### 🔀 Sort tasks

Sort by ID:

```sh
$ takser sort id
```

Sort by text:

```sh
$ takser sort text
```

Sort by status:

```sh
$ takser sort status
```

## ⚙️ How It Works

- The tasks are stored in `tasks.json`
- Each task has an `id`, `text`, and `status`
- The script reads, updates, and saves tasks dynamically
- Uses ANSI escape codes for a stylish CLI experience 💅

## 🛠️ Requirements

- Python 3.x

## 📜 License

This project is licensed under the MIT License. Feel free to modify and improve it! 🎉


