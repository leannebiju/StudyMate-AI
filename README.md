# StudyMate AI


## Basic Details
### Team Name: Techsy


### Team Members
- Member 1: Anusree U - CUSAT
- Member 2: Leanne Roslyn Biju - CUSAT
- Member 3: Christina Jogy - CUSAT

### Hosted Project Link
[[StudyMate - AI]
](https://studymate-ai.onrender.com/)
### Project Description
StudyMate - AI is an intelligent study planner designed to enhance learning efficiency. It includes features like sticky notes, a to-do list, a quiz generator, a Pomodoro timer, and an AI chatbot for doubt-solving. With AI-powered assistance, it helps students stay organized and improve productivity.

### The Problem statement
Students face challenges in organizing their study schedules, tracking tasks, and revising effectively. Traditional learning methods often result in poor time management and inefficient study habits. Finding quick answers to doubts can be difficult, leading to delays in learning. A smarter, AI-powered solution is needed to enhance productivity and retention.


### The Solution

1. **Sticky Notes 📝** – Helps students quickly jot down important points, reminders, and concepts, reducing the chances of forgetting key information.  
2. **To-Do List ✅** – Enables students to organize tasks, set priorities, and track progress, ensuring better time management.  
3. **Quiz Generator ❓** – Uses AI to generate topic-based quizzes, helping students test their knowledge and reinforce learning effectively.  
4. **Pomodoro Timer ⏳** – Implements the Pomodoro technique to improve focus, reduce procrastination, and enhance productivity.  
5. **AI Chatbot 🤖** – Provides instant AI-powered doubt resolution, offering explanations and guidance to facilitate quick and effective learning.

## Technical Details
### Technologies/Components Used
Here’s the list of software, libraries, and tools used in your project:

 **Software:**
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask
- **Database:** SQLite

 **Libraries Used:**
- **Flask:** For creating the web application
- **Flask-CORS:** To handle cross-origin requests
- **SQLite3:** For managing user authentication and storing notes
- **Werkzeug.security:** For hashing and verifying passwords
- **Google Generative AI (Gemini API):** For AI-powered quiz generation, doubt-solving, and flashcard generation
- **dotenv:** For managing environment variables securely
- **re (Regex):** For parsing AI-generated quiz responses
- **jsonify & flash:** For handling API responses and displaying messages

 **Tools Used:**
- **Postman:** For API testing
- **VS Code / PyCharm:** For development
- **Git & GitHub:** For version control
- **Google Gemini API:** For AI-powered features




### Implementation
### **Software Requirements**  

#### **Installation Steps**  

1. **Install Python and Virtual Environment**  
   - Update system packages and install Python:  
     ```bash
     sudo apt update && sudo apt install python3 python3-venv python3-pip -y
     ```  

2. **Set Up Virtual Environment**  
   - Create a virtual environment:  
     ```bash
     python3 -m venv venv
     ```  
   - Activate the virtual environment:  
     ```bash
     source venv/bin/activate   # On Windows: venv\Scripts\activate
     ```  

3. **Install Required Python Libraries**  
   - Install Flask and CORS:  
     ```bash
     pip install flask flask-cors
     ```  
   - Install LangChain and Gemini AI API:  
     ```bash
     pip install langchain google-generativeai
     ```  

4. **Frontend Setup (If Required)**  
   - Install dependencies using Node.js:  
     ```bash
     npm install
     ```  

5. **Run the Backend Server**  
   - Start the Flask application:  
     ```bash
     python app.py
     ```  

6. **Run the Frontend**  
   - Start the frontend using a live server:  
     ```bash
     npx live-server  
     ```  
  


# Run
python app.py

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![![WhatsApp Image 2025-02-09 at 10 09 23_9a2cbe70](https://github.com/user-attachments/assets/fe199192-044f-47e8-89bc-1cbddf6f04b6)
]
Home page
*The Home Page displays the project name prominently, along with Login and Register buttons, allowing users to access or create an account to utilize the platform’s features.*

![![WhatsApp Image 2025-02-09 at 10 09 16_821f15ff](![WhatsApp Image 2025-02-09 at 10 09 01_d0a1fcb0](https://github.com/user-attachments/assets/18f8fdc4-1029-4598-b7d1-0d64e1507e3b))]
Register Page
*The Register Page allows new users to create an account by entering their Name, Email, Password, and Confirm Password, ensuring secure authentication and access to the platform.*

![![WhatsApp Image 2025-02-09 at 10 09 16_fc73ae4a](https://github.com/user-attachments/assets/41d105bd-e7f9-45f5-a8d5-6aefbff2658c)
]
Login Page
*The Login Page enables registered users to access their accounts by entering their Email and Password, ensuring secure authentication.*

![![WhatsApp Image 2025-02-09 at 10 15 02_07f0d68b](https://github.com/user-attachments/assets/0a9d0ed1-d4b2-4e61-b6f9-d0a4d9784977)
]
Dashboard
*The Dashboard provides users with a structured interface featuring five key functionalities, each represented as interactive boxes with icons:  

1. **Sticky Notes** – Create, edit, and manage quick notes.  
2. **To-Do List** – Organize and track tasks efficiently.  
3. **Quiz Generator** – Generate AI-powered quizzes based on topics and difficulty levels.  
4. **AI Chatbot** – Get AI-powered answers to study-related queries.  
5. **Pomodoro Timer** – Improve focus with structured study intervals.*

![![WhatsApp Image 2025-02-09 at 10 08 19_fce8ffb4](https://github.com/user-attachments/assets/1afae3bd-426e-4f39-ae17-db5a0e06ac33)
]
Sticky Notes
*The Sticky Notes feature allows users to create, edit, and manage digital notes efficiently. Users can add important points, reminders, or study-related content, ensuring quick access and organization. Notes are visually represented as sticky cards for easy reference.*

![![WhatsApp Image 2025-02-09 at 10 11 28_c14bf8f9](https://github.com/user-attachments/assets/8ea792d2-5506-4a8b-8cbb-c02b1313b88c)
]
To-Do List
*The To-Do List feature helps users manage their tasks effectively by allowing them to add, edit, mark as completed, and delete tasks. It provides a structured way to track pending activities and stay organized.*

![![WhatsApp Image 2025-02-09 at 10 12 18_c4dd2379](https://github.com/user-attachments/assets/2e673859-c8c7-48d8-9314-c1e7febdeefe)
]
AI Chatbot
*The AI Chatbot assists users by answering queries, providing explanations, and offering study-related support. It leverages AI to deliver accurate and context-aware responses, enhancing the learning experience.*

![![WhatsApp Image 2025-02-09 at 10 13 23_618a232c](https://github.com/user-attachments/assets/19633c66-ac83-4a51-ab51-41b23b5f94ca)
]
Quiz Generator
*The Quiz Generator allows users to create AI-powered multiple-choice quizzes by selecting a topic and difficulty level. Users can view the correct answer only when they click the "Show Answer" button.*

![![WhatsApp Image 2025-02-09 at 10 14 46_c9b6f128](https://github.com/user-attachments/assets/85bc3c74-a54c-4f99-b8b2-b1c9227c67e3)
]
Pomodoro Timer
*The Pomodoro Timer helps users stay focused by implementing the Pomodoro technique, featuring a countdown timer with start, pause, and reset options.*





## Team Contributions
- [Christina Jogy]: [Frontend]
- [Leanne Roslyn Biju]: [Frontend]
- [Anusree U]: [Backend]

---
Made with ❤️ at TinkerHub
