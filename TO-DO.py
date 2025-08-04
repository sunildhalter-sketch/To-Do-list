import time
tasks = []

def add_task():
    while True:
        user_querry = input("Write your task here (press 'Enter' to exit): ")
        tasks.append(user_querry)
        if user_querry == "":
            tasks.pop()
            break

def delete_task():
    # tasks_list = ''.join(tasks)
    print("Your Tasks List:")
    for i, j in enumerate(tasks,start=1):
        print(f'''        {i}.{j}        ''')
    while True:
        user_querry = input("Which task you want to delete?(press 'Enter' to exit): ")
        if user_querry != "":
            convtInt = int(user_querry)
            convtInt-=1
            find_index = tasks[convtInt]
            tasks.remove(find_index)
            print("Task Removed Succesfully!!",)
            print("Your Tasks List:")
            for i, j in enumerate(tasks, start=1):
                print(f'''        {i}.{j}        ''')
        if tasks == []:
            print('''<><><><><><>[ list is empty!! ]<><><><><>
            << Add Task Now >> ''')
            break
        elif user_querry == "":
            break

def show_task():
    print("Your Tasks List: ")
    for i , j in enumerate(tasks,start=1):
        print(f'''        {i}.{j}        ''')

def task_completed():
    print("Your Tasks List: ")
    for i, j in enumerate(tasks, start=1):
        print(f'''        {i}.{j}        ''')
    print("-------------------")
    while True:
        user_querry = input("Which task did you completed?(press 'Enter' to exit): ")
        if user_querry != "":
            convtInt= int(user_querry)
            convtInt-=1
            findIndex = tasks[convtInt]
            result = f'''"{findIndex}" <= Completed Succesfully  !!'''
            tasks.insert(convtInt,result)
            tasks.remove(findIndex)
            
            for i, j in enumerate(tasks, start=1):
                print(f'''        {i}.{j}        ''')
                
        if user_querry = "":
            print(tasks)
            break




while True:
    time.sleep(0.9)
    ask_user = int(input('''To-Do List
    1. Add Task
    2. Remove Task
    3. Show Tasks
    4. Task Completed
    5. Exit : '''))

    if ask_user == 1 :
        add_task()

    elif ask_user == 2 :
        delete_task()

    elif ask_user == 3 :
        show_task()

    elif ask_user == 4:
        task_completed()
        
    elif ask_user == 5:
        Print("Thanks for using our application!!")
        break
    

