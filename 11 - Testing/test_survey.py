import unittest
from survey import AnonymousSurvey

class TestAnonymouseSurvey(unittest.TestCase):
    # Testing class
    def setUp(self):
        # Creating the survey and respones to be used in test methods
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Chinese']

    def test_store_single(self):
        # Test a single response is stored correctly
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_responses(self):
        # Test a single response is stored correctly
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
