import pandas as pd
import random
from transformers import pipeline

# Generate a larger dataset
policy_titles = [
    "National Policy for the Empowerment of Women, Ministry of Women & Child Development",
    "National Policy for Children, Ministry of Women & Child Development",
    "National Nutrition Policy",
    "National Health Policy",
    "National Policy for Rare Diseases",
    "National Health Policy Update",
    "Policy for Antimicrobial Resistance Control",
    "Tobacco Control Bill",
    "National Population Policy",
    "Information Security Policy Guidelines",
    "Minority Scholarship Program",
    "National Farmer Support Policy",
    "Farm Price Policy",
    "Education for All Policy",
    "Affordable Housing Policy",
    "Urban Development Strategy",
    "Renewable Energy Policy",
    "National Digital Literacy Program",
    "Policy for Small Business Development",
    "Climate Change Action Plan",
    "Women's Employment Initiative",
    "Healthcare for All Program",
    "Basic Income Support Policy",
    "Policy for Economic Upliftment of the Poor",
    "Technology Access Policy",
    "Senior Citizen Welfare Policy",
    "Disability Support Policy",
    "Youth Entrepreneurship Program",
    "Clean Air Initiative",
    "Rural Electrification Policy",
    "Tax Reform Bill",
    "Wealth Redistribution Act",
    "Affordable Internet Initiative",
    "Water Conservation Policy",
    "Agricultural Innovation Strategy",
    "Safe Transportation Policy",
    "Drug Abuse Prevention Policy",
    "Mental Health Awareness Initiative",
    "Affordable Healthcare Bill",
    "Social Security Expansion Act",
    "Women's Safety and Security Act",
    "Policy on Child Protection",
    "LGBTQ Rights Protection Act",
    "Policy for Employment Generation",
    "Disaster Relief Management Policy",
    "National Tourism Boost Initiative",
    "Policy on Wildlife Protection",
    "Energy Conservation Act",
    "Public Transport Modernization",
    "Policy for Poverty Alleviation"
]

policy_info = ["Brief information about the policy, targeting specific needs in the community."] * 50

# Adding varied target groups
target_groups = [
    "Females", "Children", "General Public", "Minorities", "Farmers",
    "Lower Economic Class", "Upper Economic Class", "Youth", "Senior Citizens",
    "Healthcare Workers", "Government Employees", "Small Business Owners",
    "Students", "Environment Advocates", "Industrial Workers", "Rich Class",
    "Poor Class", "LGBTQ Community", "Families", "Taxpayers"
]

# Adding feedback with varied sentiments
feedback = [
    "This policy is very beneficial to the community.",
    "I think this is a waste of resources.",
    "Great initiative, much needed for today's time.",
    "Not sure how effective this policy will be.",
    "This will improve lives for many people.",
    "Not the best policy, lacks focus.",
    "It’s refreshing to see a policy addressing this.",
    "This only benefits a small portion of the population.",
    "A well-thought-out policy with long-term benefits.",
    "Could have been planned better, limited impact.",
    "Finally addressing a major issue in society.",
    "Not sure if this will reach the people who need it most.",
    "Fantastic support for those who need it.",
    "I doubt this policy will make much difference.",
    "Addresses a real problem effectively.",
    "Too little too late, the issue has evolved.",
    "Important step forward for our country.",
    "Feels like just another political move.",
    "Much needed policy, very timely.",
    "This policy seems redundant.",
    "Great for economic stability.",
    "Why are we spending on this?",
    "Hope this policy brings real change.",
    "Not enough resources allocated.",
    "Finally a focus on marginalized communities.",
    "Unnecessary focus, could have been avoided.",
    "Empowering the vulnerable through this policy.",
    "Doesn’t seem like the best solution.",
    "Positive impact on society.",
    "Policy looks good on paper only.",
    "A practical approach to a tough problem.",
    "This isn’t a sustainable solution.",
    "Hope this policy lasts long-term.",
    "A step in the right direction.",
    "Probably won’t impact the rich class.",
    "Effective for lower economic groups.",
    "Very inclusive and supportive.",
    "Seems aimed more at middle class.",
    "Likely won't benefit the intended groups.",
    "Encouraging self-reliance among people.",
    "Seems mostly targeted at urban areas.",
    "Provides essential services.",
    "More beneficial for rural areas.",
    "Targets important social issues.",
    "This policy is outdated.",
    "Much needed, especially for poor class.",
    "Rich class will barely notice this.",
    "Aims to bring equality.",
    "Not sure how well this will be implemented.",
    "Empowers specific groups significantly.",
    "Shows a forward-thinking approach."
]

# Generating 50 rows of data
data = {
    "Policy_title": random.choices(policy_titles, k=50),
    "policy_info": random.choices(policy_info, k=50),
    "Target_group": random.choices(target_groups, k=50),
    "feedback": random.choices(feedback, k=50)
}

# Create the DataFrame
df = pd.DataFrame(data)

# Set up the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment in the feedback column and include confidence score
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return pd.Series([result["label"], result["score"]])

# Apply sentiment analysis and add results to DataFrame
df[["Sentiment", "Confidence"]] = df["feedback"].apply(analyze_sentiment)

# Display the DataFrame with sentiment and confidence
print("\nPolicy DataFrame with Sentiment Analysis and Confidence Score:\n", df)
