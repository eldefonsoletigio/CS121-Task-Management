Final Project
Task Management System
CS121: Advanced Computer Programming
Letigio, Eldefonso Jr. A. || IT-2105

The task management system you’re developing is designed to address the challenges of cramming and procrastination, particularly for students and workers, by offering a solution that encourages better planning and time management. The system allows users to enter tasks and categorize them into relevant areas, such as “Work,” “Study,” or “Household,” making it easier to stay organized and keep track of priorities. By incorporating a prioritization feature, users can assign levels of urgency to each task, ensuring that the most important tasks are tackled first. Overall, the system is designed to balance workloads more effectively, preventing overwhelming pressure and reducing the tendency to procrastinate, ultimately fostering a more productive and less stressful approach to completing tasks.

The core functions of the system is the user can enter tasks, enter the start data and end date being an optional, selecting category, the level of prioritization, and the status if the task is done, not yet done, or in progress. The program cannot integrate a real-time inputting of dates or scheduling, advanced analytics, and customizing the system itself. The target users or the intended audience of the system is generally the students and employees as they are really prone to procrastination and being piled up with a lot of work. 
The system will help students and workers reduce cramming and procrastination by enabling task entry, categorization, prioritization, and progress tracking through a simple, user-friendly interface.

The system aims to increase task completion rates by at least 20% within the first implementation of the project.
The project will focus on core features such as task entry, prioritization, and categorizing tasks, ensuring these functionalities are sturdy and user-friendly to use.
The outcomes align with the need for effective time management tools that support students and workers in managing workloads and reducing stress, fulfilling the system's core purpose.
The system is already complete and will undergo a feedback and enhancement phase over the following days and the feedback will be gathered for refining the general functionality of the system.

This Python program is designed as a comprehensive Task Management System using the Tkinter library for the graphical user interface (GUI) and MySQL for database interaction. The system allows users to efficiently manage their tasks by providing a range of functions such as task entry, updating, deletion, and display. The main GUI window, handled by the MainWindow class, includes several components: labels for instructions, entry fields for task name, start and due dates, and combo boxes for selecting categories, priorities, and statuses. These elements ensure the user can easily interact with the system and input task details.

The tasks are stored and displayed in a Treeview widget, which organizes them into columns showing task ID, task name, start and end dates, category, priority, and status. This allows users to quickly review and manage their ongoing tasks. The program uses MySQL to contain the data through the mysql.connector library. Tasks are inserted into, updated in, and deleted from a MySQL database. The system also includes functions to interact with the database, such as inserting new tasks and updating existing ones, with proper error handling to prevent issues.

In addition to the task management features, the program includes a HelpInfo class that provides guidance to users. This help window explains the purpose of the system, its core features, and its alignment with Sustainable Development Goals (SDGs) such as "Quality Education" and "Decent Work and Economic Growth." These goals are integrated into the design of the system, helping users manage their tasks efficiently and effectively, thus contributing to better time management and productivity. Error handling is a key part of the design. The system includes checks for inputs and ensures the smooth run of the database. For instance, it clears the input fields after a task is added, updated, or deleted to improve the user experience and prevent confusion. The program provides feedback to users through success or error messages after each operation, enhancing its usability and reliability.

Overall, this task management system is not only focused on making task handling more efficient but also designed to reduce procrastination and cramming, especially for students and workers. It achieves this by offering a clear structure for task prioritization, deadlines, and categories, making it easier for users to balance workloads.

The MainWindow or the Main System is connected to a MySQL database using the mysql.connector library. The connect() function establishes a connection to the local MySQL server and accesses the task2 database. The taskData() function ensures that a Tasks table exists with fields like task_id, taskName, startDate, endDate, Category, Priority, and Status. The addRec() function allows adding new tasks to the table, while viewData() retrieves all tasks in the database. The deleteRec() function deletes a specific task by its task_id, and the dataUpdate() function updates an existing task's details, with optional parameters for each field. The Desc() function fetches tasks in descending order by id, ensuring that the most recent tasks are shown first. Lastly, the taskData() function is called at the end of the script to ensure the table is created when the script is first run. Each function interacts with the database using SQL queries, and the connection is committed and closed after each operation to ensure changes are saved.

This program promotes two (2) Sustainable Development Goals or the SDGs. It promotes Quality Education and Decent Work and Economic Growth. The main focus of the system is the students and workers/employees. They are prone to procrastination and cramming if they don't manage their time properly. This will lead to poor performance in schools or the workplace. 
Quality Education is one of the SDGs because you can use this system in academics. Poor task management can result in poor performance which can further result in quality education. With a task management system, when their time is managed, the procrastination and cramming will be reduced. Also, this system promoted productivity. 
Decent Work and Economic Growth is another SDG in the system because workers are usually being piled up with a lot of work and offices. The other tasks that needed to be done have been ignored as a series of workloads are being put into the workers. This will also lead to cramming which will reduce their performance in their respective workplace.
The program can contribute to the goals of the abovementioned SDG as it promotes productivity for the well-being of not just the person but of the society.  

***** INSTRUCTION *****
PROGRAM/SYSTEM INSTRUCTIONS
Run the program

The program will direct you to the main system

Enter Tasks, Category, Level of Priority, and Status. The input of the start date and date has been made optional.

After inputting data, click add task.

To display, click display task and if to hide, click the hide task.

To update the data or the task, just click the task you want to update and the field of where you will make an update. Afterwards, click the update task.

To view instructions, click the Help and Information Button at the button center of the screen of the window.

Click the button of the information you wish to know and click exit to return to the main window.

To terminate the program, click exit.


