from survey import AnonymousSurvey

# Define the question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store responses
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Showing the results
print("Thank you for everyone who took part!")
my_survey.show_results()
