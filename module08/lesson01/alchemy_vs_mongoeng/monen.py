import mongoengine as me

# Define the connection to the MongoDB database
me.connect('mydatabase', host='localhost', port=27017)

# Define a sample document
class User(me.Document):
    name = me.StringField(required=True)
    age = me.IntField(required=True)
    city = me.StringField(required=True)

# Create (Add) a new user
if User.objects.count() == 0:  # Only insert if the collection is empty
    users = [
        User(name="John Doe", age=30, city="New York"),
        User(name="Jane Doe", age=25, city="Los Angeles"),
        User(name="Alice Smith", age=30, city="Chicago"),
        User(name="Bob Brown", age=40, city="New York"),
        User(name="Carol White", age=25, city="Los Angeles")
    ]
    for user in users:
        user.save()

# Read (Query) all users
users = User.objects()
for user in users:
    print(user.name, user.age)

# Read (Query) specific user by name
specific_user = User.objects(name="John Doe").first()
print(specific_user.name, specific_user.age)

# Update a user's age
specific_user.update(set__age=31)

# Re-fetch the updated user to verify the change
updated_user = User.objects(name="John Doe").first()
print(updated_user.name, updated_user.age)

# Delete a user
specific_user.delete()

# Search for users by age
users_by_age = User.objects(age__gt=25)
for user in users_by_age:
    print(user.name, user.age)


# Aggregation pipeline
pipeline = [
    {
        "$group": {
            "_id": "$city",
            "total_users": {"$sum": 1},
            "average_age": {"$avg": "$age"}
        }
    },
    {
        "$sort": {"total_users": -1}  # Sort by total_users in descending order
    }
]

# Execute the aggregation
result = User.objects.aggregate(*pipeline)

# Print the results
for entry in result:
    print(f"City: {entry['_id']}, Total Users: {entry['total_users']}, Average Age: {entry['average_age']}")
