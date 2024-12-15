def main():
    tasks = []
    while True:

        print("====== TO DO LIST ========\n")
        print("1. Add Task")
        print("2. Show Task")

        action = input("Enter number of action want to perform: ")

        if action == "1":
            print()
            n_tasks = int(input("Enter how many task want to add: "))

            for i in range(n_tasks):
                task=input("Enter the task: ")
                tasks.append({"task":task,"done":False})
                print("Task added....!")
        
        elif action == "2":
            print("\ntasks")

            for index,task in enumerate(tasks):
                status = "Done" if task["done"] else "not done"
                print(f"{index + 1}.{task["task"]} - {status}")

if __name__ == "__main__":
    main()
