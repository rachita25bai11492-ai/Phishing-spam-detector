📄 PROJECT REPORT:🚨Cybercrime Detection System
🔐 Cybercrime Detection System (Rule-Based AI)
________________________________________
🟢Cover Page:
Project Title: Cybercrime Detection System Using Rule-Based AI
Submitted By: Rachita Patel
Course: Artificial Intelligence & Machine Learning
Institution: VIT Bhopal University
Date: 28/03/2026
________________________________________
🟢Introduction:
In the modern digital era, communication through online platforms has increased significantly. However, this has also led to a rise in cybercrimes such as phishing, spam messages, and online fraud. These attacks often trick users into sharing sensitive information.
This project presents a simple Cybercrime Detection System that identifies whether a message is safe, suspicious, or fraudulent using a rule-based Artificial Intelligence approach.
________________________________________
🟢Problem Statement:
Cybercrime activities such as fake messages, phishing links, and fraud schemes are increasing rapidly
Users often fail to identify such threats, leading to financial and data loss.
This project aims to develop a system that can automatically detect and classify suspicious messages.
________________________________________
🟢 Functional Requirements:
•	Accept user input (message text)
•	Convert text into lowercase
•	Check for suspicious keywords
•	Calculate a score based on keyword matches
•	Classify message as:
o	Safe
o	Suspicious
o	Fraud
•	Display result to user
•	Allow multiple inputs
________________________________________
🟢Non-Functional Requirements:
•	Fast execution
•	User-friendly interface
•	Lightweight (no external libraries)
•	Platform independent
•	Reliable output
________________________________________
🟢System Architecture:
The system follows a simple pipeline:
Input → Preprocessing → Keyword Matching → Score Calculation → Decision → Output
________________________________________
🟢Design Diagrams:
🔹 Use Case Diagram
User interacts with system to:
•	Enter message
•	View result
🔹 Workflow Diagram
Start → Input → Process → Check Keywords → Decision → Output → End
🔹 Sequence Diagram
User → System → Processing → Decision → Output → User
🔹 Class / Component Diagram
Components:
•	Input Module
•	Processing Module
•	Detection Module
        Output Modul
  🟢Flowchart:
    ┌───────────────┐
    │     Start     │
    └───────┬───────┘
            │
            ▼
     ┌─────────────────────┐
     │ Enter Message Input │
     └─────────┬───────────┘
               │
               ▼
     ┌─────────────────────┐
     │ Convert to Lowercase│
     └─────────┬───────────┘
               │
               ▼
     ┌─────────────────────┐
     │ Initialize Score = 0│
     └─────────┬───────────
               ▼
     ┌────────────────────────────┐
     │ Check for Keywords (loop)  │
     │ (win, free, otp, bank...)  │
     └─────────┬────────────────
               ▼
     ┌─────────────────────┐
     │ Increase Score if   │
     │ keyword found       │
     └─────────┬───────────┘
               │
               ▼
      ┌─────────────────────┐
      │  Score ≥ 3 ?   │
      └───────┬─────┬───────┘
            │Yes No │
           ▼      ▼
   ┌──────────────────┐   
   │ High Risk Fraud  │   
   │ Score == 2 ?  │
   └─────────┬────────┘   
        │Yes  │No│
       ▼           ▼
      ┌──────────────┐
        │ Display  │ 
       │ Suspicious  │
         │ Result   │   
      └──────┬───────┘ 
             ▼
       ┌──────────────┐
        │ Display    │
          │ Result  │
       └──────┬───────┘
              ▼
        ┌──────────────┐  
        │   Safe Msg   │
          │   End  │
        └──────┬───────┘  
               ▼
        ┌──────────────┐
        │ Display      │
        │ Result       │
        └──────┬───────┘
               ▼
        ┌──────────────┐
            │End │     
        └──────┬───────┘
🟢Algorithm:
1.	Start 
2.	Input message from user 
3.	Convert message to lowercase 
4.	Initialize score = 0 
5.	For each keyword in the list: 
o	If keyword is found → increase score 
6.	If score ≥ 3 → High Risk Fraud 
7.	If score = 2 → Suspicious 
8.	Else → Safe 
9.	Display result 
10.	End 
________________________________________
🟢Design Decisions & Rationale:
•	Chose rule-based AI for simplicity
•	Avoided ML libraries to ensure easy execution
•	Used keyword detection for faster processing
•	Designed multi-level classification for better results
________________________________________


 
🟢 Implementation Details:
•	Language: Python
•	Approach: Rule-Based AI
•	Logic:
o	Convert message to lowercase
o	Match keywords
o	Calculate score
o	Classify output
🟢Screenshots / Results:
Example Outputs:
Input: "Win free money now"
Output: 🚨 High Risk Fraud
Input: "Let's meet tomorrow"
Output: ✅ Safe Message
 
________________________________________
🟢 Testing Approach:
•	Tested with multiple inputs
•	Used both fraud and safe messages
•	Verified classification accuracy
•	Checked edge cases
________________________________________
🟢 Challenges Faced:
•	Identifying correct keywords
•	Avoiding false positives
•	Maintaining simplicity while ensuring accuracy
🟢Learnings & Key Takeaways:
•	Understanding of AI concepts
•	Real-world problem solving
•	Implementation of rule-based systems
•	Importance of cyber security
________________________________________
🟢Future Enhancements:
•	Add Machine Learning models
•	Improve accuracy using datasets
•	Develop GUI/Web app
•	Detect phishing URLs
•	Integrate real-time systems
________________________________________
🟢 References:
•	Python Documentation
•	AI/ML Study Material
•	Cyber Security Awareness Resources
•	Vityarthi
________________________________________
✅ Conclusion:
This project demonstrates how a simple AI-based system can help detect cybercrime and improve user awareness. It provides a strong foundation for future AI-based security systems.


