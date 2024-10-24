from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from problems.models import Solutions, Tasks
from problems.utils.samples import sample_solution, sample_task, sample_tests


class TestProblems(TestCase):
    def setUp(self):
        tests_dir = f"{Path(__file__).resolve().parent.parent}/tasks/tests_for_tasks"
        self.test_tests = sample_tests(tests_dir)

        self.test_problem = sample_task("Two sums", self.test_tests)

    def test_count_problem(self):
        self.assertEqual(Tasks.objects.count(), 1)

    def test_max_limit_name_task(self):
        with self.assertRaises(ValidationError):
            sample_task("N" * 500, self.test_tests)

    def test_max_limit_description_task(self):
        with self.assertRaises(ValidationError):
            sample_task("U" * 5000, self.test_tests)

    def test_error_choices_task(self):
        with self.assertRaises(ValidationError):
            sample_task("Test", self.test_tests, category="Physics")


class TestSolutions(TestCase):
    def setUp(self):
        tests_dir = f"{Path(__file__).resolve().parent.parent}/tasks/tests_for_tasks"
        self.test_tests = sample_tests(tests_dir)

        self.task = sample_task("Two sums", self.test_tests)

        self.client = Client()

        self.user = get_user_model()(username="Oleg")
        self.user.set_password("12345678")
        self.user.save()

        self.solution = sample_solution(self.user, self.task)

    def test_solution(self):
        self.assertEqual(Solutions.objects.count(), 1)

    def test_bad_choice_status(self):
        with self.assertRaises(ValidationError):
            sample_solution(self.user, self.task, status=10)
