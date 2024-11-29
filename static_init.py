import random

# Extended dataset for exercise, meal plans, and wellness tips
exercise_plans = {
    "sedentary": ["Start with daily 30-minute walks.", "Try gentle yoga for flexibility."],
    "active": ["Add strength training 3 times a week.", "Incorporate 30-minute cycling sessions."],
    "athletic": ["Try HIIT workouts 4-5 times a week.", "Increase endurance with running or swimming."]
}

nutrition_plans = {
    "weight_loss": ["Increase protein intake (chicken, tofu, fish).", "Reduce carb intake (pasta, bread)."],
    "muscle_gain": ["Focus on calorie-dense foods (nuts, seeds, lean meats).", "Increase carbs (sweet potatoes, rice)."],
    "maintenance": ["Include a balanced mix of protein, carbs, and fats.", "Eat a variety of vegetables and fruits."]
}

wellness_tips = [
    "Drink at least 8 cups of water daily.",
    "Take 5-minute breaks during long sitting hours.",
    "Sleep 7-8 hours per night for optimal recovery."
]

# Advanced features - User attributes
def get_user_health_profile(user_data):
    profile = {}

    # Age-based adjustment to exercise recommendations
    age = user_data["age"]
    if age < 30:
        profile["exercise"] = "athletic"
    elif 30 <= age < 50:
        profile["exercise"] = "active"
    else:
        profile["exercise"] = "sedentary"

    # Gender-specific dietary recommendations
    gender = user_data["gender"]
    if gender == "female":
        profile["nutrition"] = "maintenance"  # General recommendation for females
    else:
        profile["nutrition"] = "muscle_gain"  # General recommendation for males

    # Chronic conditions (e.g., hypertension, diabetes)
    conditions = user_data.get("conditions", [])
    if "hypertension" in conditions:
        profile["wellness"] = "Avoid salty foods and monitor blood pressure regularly."
    elif "diabetes" in conditions:
        profile["wellness"] = "Follow a low-carb diet and track blood sugar levels."

    return profile

# Function to generate personalized recommendations
def generate_recommendations(user_data):
    recommendations = []

    # Get user health profile based on attributes
    profile = get_user_health_profile(user_data)

    # Exercise recommendation based on age and activity level
    activity_level = profile["exercise"]
    recommendations.append(f"Exercise Recommendation: {random.choice(exercise_plans.get(activity_level, []))}")

    # Nutrition recommendation based on gender and goal
    nutrition_goal = profile["nutrition"]
    recommendations.append(f"Nutrition Recommendation: {random.choice(nutrition_plans.get(nutrition_goal, []))}")

    # Wellness tip based on conditions
    wellness_tip = profile.get("wellness", random.choice(wellness_tips))
    recommendations.append(f"Wellness Tip: {wellness_tip}")

    return recommendations

# Sample user data input
user_data = {
    "age": 35,
    "gender": "male",  # Options: "female", "male"
    "activity_level": "active",  # Options: "sedentary", "active", "athletic"
    "goal": "muscle_gain",  # Options: "weight_loss", "muscle_gain", "maintenance"
    "conditions": ["hypertension"]  # Options: ["hypertension", "diabetes", "none"]
}

# Generate recommendations for the user
personalized_recommendations = generate_recommendations(user_data)

# Print personalized health recommendations
print("Personalized Health Recommendations:")
for recommendation in personalized_recommendations:
    print(f"- {recommendation}")
