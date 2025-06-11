

A terminal-based quiz game powered by OpenAI's GPT-3.5-Turbo that generates unique **Yes/No** questions based on your chosen category. Ideal for students or anyone who enjoys quick quizzes.

---

## 🎮 Features

- 🧠 Generates AI-powered Yes/No questions.
- 🎓 User selects a quiz topic.
- ✅ Tracks correct and incorrect answers.
- 🔁 Option to restart the quiz.
- ❌ Handles invalid inputs.

---

## 📦 Requirements

- Python 3.7+
- [OpenAI Python SDK](https://github.com/openai/openai-python)

Install dependencies:

```bash
pip install openai
🔑 OpenAI API Key Setup
To use this app, you need an OpenAI API key. Get yours here.

Replace this line in the script:

python
Copy
Edit
openai.api_key = "your-api-key-here"
Alternatively (recommended): use an environment variable:

python
Copy
Edit
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
Then set it in your terminal:

Linux/macOS:

bash
Copy
Edit
export OPENAI_API_KEY=your-key-here
Windows (CMD):

cmd
Copy
Edit
set OPENAI_API_KEY=your-key-here
🚀 How to Run
Clone this repository or download the quiz_game.py script.

Set your API key (see above).

Run the script:

bash
Copy
Edit
python quiz_game.py
🧪 Example
vbnet
Copy
Edit
Welcome to my AI Generated Quiz!
Choose category: history
Let's start the game!
Question 1 : Was Abraham Lincoln a U.S. president?
Answer (yes/no): yes
Correct!
...
You answered 4/5 questions
Do you want to play again? no
Thanks for playing!
📈 Customization
🔢 Change the number of questions: edit the line for i in range(5) in the start_quiz() function.

🧩 Add more question formats or scoring options.

❗ Security Warning
⚠️ Never share your API key publicly or commit it to GitHub. Always use environment variables in production environments.

📌 Future Improvements
Add support for multiple-choice questions.

Track high scores.

Add GUI using Tkinter or PyQt.

Handle API errors and rate limits.

👤 Author
Created by a developer using ChatGPT assistance.
Feel free to fork, modify, and improve this project!

