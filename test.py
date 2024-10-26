import unittest
from flask import Flask
from flask.testing import FlaskClient
import json
from main import app, Rule, session, Base, engine

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        # Create test client
        self.app = app.test_client()
        # Create fresh tables for each test
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        
    def tearDown(self):
        session.close()
        
    def test_create_rule(self):
        """Test rule creation with various conditions"""
        # Test single condition rule
        response = self.app.post('/create_rule', 
            json={'rule_string': 'age > 25'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertIn('ast', data)
        
        # Test compound rule with AND
        response = self.app.post('/create_rule', 
            json={'rule_string': '(age > 25 AND income > 50000)'})
        self.assertEqual(response.status_code, 200)
        
        # Test compound rule with OR
        response = self.app.post('/create_rule', 
            json={'rule_string': '(age > 25 OR income > 50000)'})
        self.assertEqual(response.status_code, 200)
        
    def test_combine_rules(self):
        """Test combining multiple rules"""
        # Create two rules
        r1 = self.app.post('/create_rule', 
            json={'rule_string': 'age > 25'})
        r2 = self.app.post('/create_rule', 
            json={'rule_string': 'income > 50000'})
        
        r1_data = json.loads(r1.data)
        r2_data = json.loads(r2.data)
        
        # Combine rules
        response = self.app.post('/combine_rules', 
            json={'rule_ids': [r1_data['id'], r2_data['id']]})
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertIn('combined_ast', data)
        
    def test_evaluate_rule(self):
        """Test rule evaluation with different scenarios"""
        # Create a rule
        rule_response = self.app.post('/create_rule', 
            json={'rule_string': '(age > 25 AND income > 50000)'})
        rule_data = json.loads(rule_response.data)
        
        # Test true case
        response = self.app.post('/evaluate_rule', 
            json={
                'rule_id': rule_data['id'],
                'data': {'age': 30, 'income': 60000}
            })
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertTrue(result['result'])
        
        # Test false case
        response = self.app.post('/evaluate_rule', 
            json={
                'rule_id': rule_data['id'],
                'data': {'age': 20, 'income': 60000}
            })
        result = json.loads(response.data)
        self.assertFalse(result['result'])
        
    def test_modify_rule(self):
        """Test rule modification"""
        # Create initial rule
        rule_response = self.app.post('/create_rule', 
            json={'rule_string': 'age > 25'})
        rule_data = json.loads(rule_response.data)
        
        # Modify rule
        response = self.app.post('/modify_rule', 
            json={
                'rule_id': rule_data['id'],
                'new_rule_string': 'age > 30'
            })
        self.assertEqual(response.status_code, 200)
        
        # Verify modification by evaluating
        eval_response = self.app.post('/evaluate_rule', 
            json={
                'rule_id': rule_data['id'],
                'data': {'age': 28}
            })
        result = json.loads(eval_response.data)
        self.assertFalse(result['result'])
        
    def test_error_handling(self):
        """Test error handling scenarios"""
        # Test invalid rule ID
        response = self.app.post('/evaluate_rule', 
            json={
                'rule_id': 999,
                'data': {'age': 30}
            })
        self.assertEqual(response.status_code, 404)
        
        # Test invalid rule modification
        response = self.app.post('/modify_rule', 
            json={
                'rule_id': 999,
                'new_rule_string': 'age > 30'
            })
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()