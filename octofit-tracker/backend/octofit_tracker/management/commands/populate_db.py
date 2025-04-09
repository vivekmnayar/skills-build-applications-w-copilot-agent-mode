from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User().collection.delete_many({})
        Team().collection.delete_many({})
        Activity().collection.delete_many({})
        Leaderboard().collection.delete_many({})
        Workout().collection.delete_many({})

        # Add test users
        user1 = User().insert_one({'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'})
        user2 = User().insert_one({'username': 'jane_doe', 'email': 'jane@example.com', 'password': 'password123'})

        # Add test teams
        Team().insert_one({'name': 'Team Alpha', 'members': [user1.inserted_id, user2.inserted_id]})

        # Add test activities
        Activity().insert_one({'user': user1.inserted_id, 'activity_type': 'Running', 'duration': '00:30:00'})
        Activity().insert_one({'user': user2.inserted_id, 'activity_type': 'Cycling', 'duration': '01:00:00'})

        # Add test leaderboard entries
        Leaderboard().insert_one({'user': user1.inserted_id, 'score': 100})
        Leaderboard().insert_one({'user': user2.inserted_id, 'score': 150})

        # Add test workouts
        Workout().insert_one({'name': 'Morning Yoga', 'description': 'A relaxing yoga session to start the day.'})
        Workout().insert_one({'name': 'HIIT', 'description': 'High-Intensity Interval Training for fat burning.'})

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
