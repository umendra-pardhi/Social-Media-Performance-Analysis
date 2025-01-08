import csv
import random

class SocialMediaDataGenerator:
    def __init__(self):
        # Content types with engagement patterns
        self.content_types = {
            'carousel': {'weight': 0.25, 'engagement_multiplier': 1.5},
            'reel': {'weight': 0.3, 'engagement_multiplier': 2.0},
            'static_post': {'weight': 0.2, 'engagement_multiplier': 1.0},
            'story': {'weight': 0.15, 'engagement_multiplier': 0.8},
            'igtv': {'weight': 0.1, 'engagement_multiplier': 1.2},
        }
        
        # Hashtag categories
        self.hashtag_categories = [
            'lifestyle', 'tech', 'food', 'travel', 'fitness',
            'fashion', 'beauty', 'business', 'art', 'music'
        ]

    def generate_hashtags(self):
        """Generate a relevant set of hashtags."""
        num_hashtags = random.randint(3, 8)
        return random.sample(self.hashtag_categories, num_hashtags)

    def calculate_engagement_rate(self, likes, comments, shares, impressions):
        """Calculate engagement rate as percentage."""
        total_engagement = likes + comments + shares
        return round((total_engagement / impressions) * 100, 2)

    def generate_data(self, num_records=500):
        """Generate social media performance data."""
        data = []
        
        for _ in range(num_records):
            # Select content type based on weights
            content_type = random.choices(
                list(self.content_types.keys()),
                weights=[t['weight'] for t in self.content_types.values()]
            )[0]
            
            # Base metrics
            base_impressions = random.randint(1000, 5000)
            engagement_multiplier = self.content_types[content_type]['engagement_multiplier']
            
            # Generate engagement metrics
            impressions = int(base_impressions * engagement_multiplier)
            reach = int(impressions * random.uniform(0.6, 0.9))  # Reach is typically 60-90% of impressions
            likes = int(random.randint(50, 300) * engagement_multiplier)
            comments = int(random.randint(5, 75) * engagement_multiplier)
            shares = int(random.randint(10, 100) * engagement_multiplier)
            saves = int(random.randint(5, 50) * engagement_multiplier)
            
            record = {
                'content_type': content_type,
                'hashtag_categories': ','.join(self.generate_hashtags()),
                'impressions': impressions,
                'reach': reach,
                'likes': likes,
                'comments': comments,
                'shares': shares,
                'saves': saves,
                'engagement_rate': self.calculate_engagement_rate(
                    likes, comments, shares, impressions
                )
            }
            data.append(record)
            
        return data

    def save_to_csv(self, data, filename='social_media_mock_dataset.csv'):
        """Save the generated data to a CSV file."""
        fieldnames = [
            'content_type', 'hashtag_categories', 'impressions', 'reach',
            'likes', 'comments', 'shares', 'saves', 'engagement_rate'
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Enhanced dataset created: {filename}")

# Generate the data
generator = SocialMediaDataGenerator()
social_media_data = generator.generate_data(100)
generator.save_to_csv(social_media_data)