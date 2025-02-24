
# import openai

# # Welcome the user
# def welcome_user():
#    print("Welcome to Your Personal AI Tutor!")
#    print("I can help you learn in a fun and adaptive way. Let's get started!\n")

# # Lessons and quizzes
# lessons = {
#     "Math": [
#         {"question": "What is 2 + 2?", "answer": "4"},
#         {"question": "Solve for x: 2x + 3 = 7", "answer": "2"}
#     ],
#     "Science": [
#         {"question": "What is photosynthesis?", "answer": "The process by which green plants use sunlight to synthesize food."},
#         {"question": "Name three states of matter.", "answer": "Solid, Liquid, Gas"}
#     ]
# }

# # Adjust difficulty based on performance
# def adjust_difficulty(score):
#     if score > 80:
#         return "advanced"
#     elif score > 50:
#         return "intermediate"
#     else:
#         return "beginner"
    
# # Get explanation using OpenAI API
# def get_explanation(topic):
#     try:
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=f"Explain {topic} in simple terms.",
#             max_tokens=100
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return f"Error fetching explanation: {e}"    
    
#     # Quiz user and provide feedback
# def quiz_user(topic):
#     print(f"\nStarting quiz on {topic}!\n")
#     questions = lessons.get(topic, [])
#     score = 0

#     for q in questions:
#         print(q["question"])
#         user_answer = input("Your answer: ").strip()
#         if user_answer.lower() == q["answer"].lower():
#             print("Correct!\n")
#             score += 10
#         else:
#             print(f"Incorrect. The correct answer is: {q['answer']}\n")

#     print(f"Your score: {score}/{len(questions) * 10}")
#     return score

# # Main function
# def main():
   
#     while True:
#         print("Available topics: ")
#         for topic in lessons.keys():
#             print(f"- {topic}")

#         chosen_topic = input("Choose a topic to learn (or type 'exit' to quit): ").strip()
#         if chosen_topic.lower() == "exit":
#             print("Thank you for using the AI Tutor. Keep learning!")
#             break

#         if chosen_topic not in lessons:
#             print("Invalid topic. Please choose from the available topics.\n")
#             continue

#         explanation = get_explanation(chosen_topic)
#         print(f"\nHere is a brief explanation of {chosen_topic}:\n{explanation}\n")

#         score = quiz_user(chosen_topic)
#         level = adjust_difficulty(score)
#         print(f"Your suggested learning level is: {level}\n")

# if __name__ == "__main__":
#     main()