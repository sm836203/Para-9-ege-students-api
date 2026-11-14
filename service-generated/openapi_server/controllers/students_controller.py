import flask
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.delete_result import DeleteResult  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.student_create import StudentCreate  # noqa: E501
from openapi_server.models.student_response import StudentResponse  # noqa: E501
from openapi_server.models.student_update import StudentUpdate  # noqa: E501
from openapi_server.models.subject import Subject  # noqa: E501
from openapi_server import util


def create_student(body):  # noqa: E501
    """Добавить ученика

    Создает карточку ученика на основании переданных данных. # noqa: E501

    :param student_create: Данные нового ученика.
    :type student_create: dict | bytes

    :rtype: Union[StudentResponse, Tuple[StudentResponse, int], Tuple[StudentResponse, int, Dict[str, str]]
    """
    student_create = body
    if flask.request.is_json:
        student_create = StudentCreate.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_student(student_id):  # noqa: E501
    """Удалить ученика

    Удаляет карточку ученика по идентификатору. # noqa: E501

    :param student_id: Уникальный идентификатор ученика.
    :type student_id: int

    :rtype: Union[DeleteResult, Tuple[DeleteResult, int], Tuple[DeleteResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_student(student_id):  # noqa: E501
    """Получить карточку ученика

    Возвращает сведения об одном ученике по его идентификатору. # noqa: E501

    :param student_id: Уникальный идентификатор ученика.
    :type student_id: int

    :rtype: Union[StudentResponse, Tuple[StudentResponse, int], Tuple[StudentResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_students(subject=None):  # noqa: E501
    """Получить список учеников

    Возвращает всех учеников, при необходимости отфильтрованных по предмету. # noqa: E501

    :param subject: Предмет ЕГЭ для фильтрации.
    :type subject: dict | bytes

    :rtype: Union[List[StudentResponse], Tuple[List[StudentResponse], int], Tuple[List[StudentResponse], int, Dict[str, str]]
    """
    if isinstance(subject, dict):
        subject = Subject.from_dict(subject)  # noqa: E501
    return 'do some magic!'


def update_student(student_id, body):  # noqa: E501
    """Обновить данные ученика

    Позволяет изменить только переданные поля, например текущий балл. # noqa: E501

    :param student_id: Уникальный идентификатор ученика.
    :type student_id: int
    :param student_update: Поля карточки, которые требуется изменить.
    :type student_update: dict | bytes

    :rtype: Union[StudentResponse, Tuple[StudentResponse, int], Tuple[StudentResponse, int, Dict[str, str]]
    """
    student_update = body
    if flask.request.is_json:
        student_update = StudentUpdate.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'
