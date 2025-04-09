from django.conf import settings

class MongoDBModel:
    def __init__(self, collection_name):
        self.collection = settings.MONGO_DB[collection_name]

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def find(self, query=None):
        return self.collection.find(query or {})

    def update_one(self, query, update):
        return self.collection.update_one(query, {'$set': update})

    def delete_one(self, query):
        return self.collection.delete_one(query)

# Example usage for users collection
class User(MongoDBModel):
    def __init__(self):
        super().__init__('users')

# Similar classes can be created for Team, Activity, Leaderboard, and Workout collections.
class Team(MongoDBModel):
    def __init__(self):
        super().__init__('teams')

class Activity(MongoDBModel):
    def __init__(self):
        super().__init__('activities')

class Leaderboard(MongoDBModel):
    def __init__(self):
        super().__init__('leaderboards')

class Workout(MongoDBModel):
    def __init__(self):
        super().__init__('workouts')
