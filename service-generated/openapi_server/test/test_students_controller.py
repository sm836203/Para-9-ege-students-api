import unittest

from flask import json

from openapi_server.models.delete_result import DeleteResult  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.student_create import StudentCreate  # noqa: E501
from openapi_server.models.student_response import StudentResponse  # noqa: E501
from openapi_server.models.student_update import StudentUpdate  # noqa: E501
from openapi_server.models.subject import Subject  # noqa: E501
from openapi_server.test import BaseTestCase


class TestStudentsController(BaseTestCase):
    """StudentsController integration test stubs"""

    def test_create_student(self):
        """Test case for create_student

        Добавить ученика
        """
        student_create = {"fullName":"Иванов Петр","subject":"SOCIAL_STUDIES","examYear":2027,"targetScore":85,"currentScore":64}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/students',
            method='POST',
            headers=headers,
            data=json.dumps(student_create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_student(self):
        """Test case for delete_student

        Удалить ученика
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/students/{student_id}'.format(student_id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_student(self):
        """Test case for get_student

        Получить карточку ученика
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/students/{student_id}'.format(student_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_students(self):
        """Test case for list_students

        Получить список учеников
        """
        query_string = [('subject', openapi_server.Subject())]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/students',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_student(self):
        """Test case for update_student

        Обновить данные ученика
        """
        student_update = {"fullName":"fullName","subject":"SOCIAL_STUDIES","examYear":2031,"currentScore":60,"targetScore":14,"status":"ACTIVE"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/students/{student_id}'.format(student_id=1),
            method='PATCH',
            headers=headers,
            data=json.dumps(student_update),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
