import unittest 
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""
    def test_store_single_response(self): 
        """Testa se uma única resposta é armazenada de forma apropriada."""         
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    
    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma apropriada.""" 
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin'] 
        for response in responses: 
            my_survey.store_response(response)
            for response in responses:
                self.assertIn(response, my_survey.response)

unittest.main() 