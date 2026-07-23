# Prompt Engineering Demo
# Topic: Promotional Social Media Post for an AI Workshop

# --------------------------------------------------
# Zero-shot Prompt
# --------------------------------------------------

zero_prompt = """
Write a promotional social media post for an AI Workshop.
"""

zero_post = """
🚀 Join our AI Workshop!

Learn the fundamentals of Artificial Intelligence, Machine Learning,
and Prompt Engineering through hands-on sessions led by industry experts.
Enhance your skills, work on real-world projects, and earn a certificate
of participation.

📅 Date: 15 August 2026
📍 Venue: ABC College
📝 Register Now!

#AI #MachineLearning #Workshop #Innovation
"""

# --------------------------------------------------
# One-shot Prompt
# --------------------------------------------------

one_prompt = """
Example

Task:
Write a promotional social media post for a Cyber Security Workshop.

Post:
🔒 Join our Cyber Security Workshop!
Learn ethical hacking, network security, and cyber defense techniques.
Register today and earn a participation certificate.

Now write a promotional social media post for an AI Workshop.
"""

one_post = """
🤖 AI Workshop 2026 – Register Today!

Discover the exciting world of Artificial Intelligence through expert
sessions, live demonstrations, and practical activities.
Gain valuable knowledge in Machine Learning, Deep Learning, and AI tools.

📅 Date: 15 August 2026
📍 Venue: ABC College
🎓 Certificate Provided

#ArtificialIntelligence #AIWorkshop #Learning #Technology
"""

# --------------------------------------------------
# Few-shot Prompt
# --------------------------------------------------

few_prompt = """
Example 1

Task:
Write a post for a Python Workshop.

Post:
Learn Python programming with hands-on practice and expert guidance.

Example 2

Task:
Write a post for a Data Science Workshop.

Post:
Master Data Science concepts using real-world datasets and projects.

Example 3

Task:
Write a post for a Cloud Computing Workshop.

Post:
Explore cloud technologies and build scalable applications.

Now write a promotional social media post for an AI Workshop.
"""

few_post = """
🌟 Ready to Explore Artificial Intelligence?

Join our exclusive AI Workshop and gain practical experience in
Machine Learning, Prompt Engineering, and AI applications.
Interact with experts, build exciting AI projects, and receive a
certificate upon completion.

📅 Date: 15 August 2026
📍 Venue: ABC College
🎯 Limited Seats – Register Now!

#AIWorkshop #ArtificialIntelligence #FutureTech #Innovation #CareerGrowth
"""

# --------------------------------------------------
# Display Output
# --------------------------------------------------

print("=" * 60)
print("ZERO-SHOT PROMPT")
print("=" * 60)
print(zero_prompt)
print("\nGenerated Social Media Post:\n")
print(zero_post)

print("\n" + "=" * 60)
print("ONE-SHOT PROMPT")
print("=" * 60)
print(one_prompt)
print("\nGenerated Social Media Post:\n")
print(one_post)

print("\n" + "=" * 60)
print("FEW-SHOT PROMPT")
print("=" * 60)
print(few_prompt)
print("\nGenerated Social Media Post:\n")
print(few_post)

# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
1. Creativity
   - Zero-shot : Good
   - One-shot  : Better
   - Few-shot  : Excellent

2. Engagement
   - Zero-shot : Attractive
   - One-shot  : More engaging
   - Few-shot  : Highly engaging with strong call-to-action

3. Formatting
   - Zero-shot : Good
   - One-shot  : Well-structured
   - Few-shot  : Best use of emojis, hashtags, and layout

4. Completeness
   - Zero-shot : Includes workshop details
   - One-shot  : Includes details and benefits
   - Few-shot  : Includes details, benefits, certificate, and call-to-action

Conclusion:
Few-shot prompting produces the most attractive, engaging, and complete promotional social media post.
""")
