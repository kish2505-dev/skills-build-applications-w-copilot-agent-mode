from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', team='marvel')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='avengers', members=['ironman', 'hulk'])
        self.assertEqual(team.name, 'avengers')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', activity='run', duration=30)
        self.assertEqual(activity.activity, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='testuser', score=100)
        self.assertEqual(lb.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='yoga', description='Yoga session')
        self.assertEqual(workout.name, 'yoga')
