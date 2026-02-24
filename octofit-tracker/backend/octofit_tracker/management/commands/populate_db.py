from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from djongo import models

from django.conf import settings

from pymongo import MongoClient

# Sample data
USERS = [
    {"username": "superman", "email": "superman@dc.com", "team": "dc"},
    {"username": "batman", "email": "batman@dc.com", "team": "dc"},
    {"username": "wonderwoman", "email": "wonderwoman@dc.com", "team": "dc"},
    {"username": "spiderman", "email": "spiderman@marvel.com", "team": "marvel"},
    {"username": "ironman", "email": "ironman@marvel.com", "team": "marvel"},
    {"username": "captainamerica", "email": "captainamerica@marvel.com", "team": "marvel"},
]

TEAMS = [
    {"name": "marvel", "members": ["spiderman", "ironman", "captainamerica"]},
    {"name": "dc", "members": ["superman", "batman", "wonderwoman"]},
]

ACTIVITIES = [
    {"user": "superman", "activity": "flying", "duration": 120},
    {"user": "batman", "activity": "training", "duration": 90},
    {"user": "spiderman", "activity": "web-slinging", "duration": 60},
]

LEADERBOARD = [
    {"user": "superman", "score": 1000},
    {"user": "spiderman", "score": 900},
    {"user": "ironman", "score": 850},
]

WORKOUTS = [
    {"name": "strength", "description": "Strength training workout"},
    {"name": "cardio", "description": "Cardio workout"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Create unique index on email for users
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
