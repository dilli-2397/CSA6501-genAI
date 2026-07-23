# Prompt Engineering Demo
# Topic: Applications of Artificial Intelligence in Healthcare

# -----------------------------
# Zero-shot Prompt
# -----------------------------
zero_shot_prompt = """
Write a 200-word blog on 'Applications of Artificial Intelligence in Healthcare'.
"""

zero_shot_output = """
Artificial Intelligence (AI) is transforming the healthcare industry by improving
the quality and efficiency of medical services. AI-powered systems help doctors
diagnose diseases accurately using medical images, laboratory reports, and patient
records. Machine learning algorithms can detect conditions such as cancer, diabetes,
and heart disease at an early stage, increasing the chances of successful treatment.

AI also supports personalized medicine by recommending treatments based on a patient's
medical history and genetic information. Virtual health assistants and chatbots provide
24/7 support by answering health-related questions and scheduling appointments.
Hospitals use AI to manage patient records, predict patient admissions, and optimize
resource allocation. Robotic-assisted surgeries improve precision and reduce recovery
time for patients. Wearable devices powered by AI monitor heart rate, sleep patterns,
and physical activity, helping individuals maintain a healthy lifestyle.

Despite its many benefits, AI also raises concerns regarding data privacy and ethical
use. Proper regulations and secure data management are essential. As technology
continues to advance, AI will play an increasingly important role in improving
healthcare services, reducing costs, and enhancing patient outcomes worldwide.
"""

# -----------------------------
# One-shot Prompt
# -----------------------------
one_shot_prompt = """
Example

Topic: Applications of AI in Education

Blog:
Artificial Intelligence is changing education by providing personalized learning,
automated grading, virtual tutors, and intelligent learning platforms. AI helps
teachers identify students' strengths and weaknesses while making education more
interactive and accessible.

Now write a 200-word blog on 'Applications of Artificial Intelligence in Healthcare'.
"""

one_shot_output = """
Artificial Intelligence has become an important part of modern healthcare by helping
medical professionals deliver faster and more accurate services. AI-based diagnostic
systems analyze medical images and patient records to identify diseases in their
early stages. This reduces diagnostic errors and improves treatment outcomes.

AI is widely used in robotic surgeries, where advanced robots assist surgeons in
performing complex procedures with greater precision. Virtual assistants help
patients schedule appointments, receive medication reminders, and obtain basic
medical guidance. Wearable devices equipped with AI continuously monitor vital signs
such as heart rate, oxygen levels, and sleep quality.

Hospitals use AI for managing electronic health records, predicting patient admissions,
and improving operational efficiency. AI also supports drug discovery by analyzing
large datasets and identifying potential medicines in less time than traditional
methods.

Although challenges such as data privacy and ethical concerns exist, AI continues to
improve healthcare quality and accessibility. As AI technologies advance, they will
help create smarter hospitals, support healthcare professionals, and provide better
patient care across the world.
"""

# -----------------------------
# Few-shot Prompt
# -----------------------------
few_shot_prompt = """
Example 1

Topic: AI in Education

Blog:
AI personalizes learning and automates educational tasks.

Example 2

Topic: AI in Agriculture

Blog:
AI helps farmers monitor crops, predict weather, detect diseases, and improve yields.

Example 3

Topic: AI in Banking

Blog:
AI detects fraud, automates customer service, and improves financial decision-making.

Now write a 200-word blog on 'Applications of Artificial Intelligence in Healthcare'.
"""

few_shot_output = """
Artificial Intelligence is revolutionizing healthcare by improving diagnosis,
treatment, and patient care. AI systems analyze medical data quickly and accurately,
allowing doctors to detect diseases such as cancer, pneumonia, and heart disease
at earlier stages. This leads to timely treatment and better patient outcomes.

AI-powered robots assist surgeons during complex operations, increasing precision
and reducing recovery time. Virtual assistants and chatbots provide healthcare
information, appointment scheduling, and medication reminders. Wearable devices use
AI to monitor health conditions continuously and alert users to possible risks.

Healthcare organizations use AI to manage hospital resources, predict patient flow,
and maintain electronic medical records efficiently. AI also accelerates drug
discovery by analyzing millions of research documents and identifying promising
compounds.

While issues related to privacy, security, and ethics must be carefully addressed,
the benefits of AI continue to grow. With ongoing technological advancements,
Artificial Intelligence will enhance healthcare accessibility, improve medical
research, reduce costs, and support doctors in delivering high-quality care,
creating a healthier future for people around the world.
"""

# -----------------------------
# Display Output
# -----------------------------
print("=" * 60)
print("ZERO-SHOT PROMPT")
print("=" * 60)
print(zero_shot_prompt)
print("\nGenerated Blog:\n")
print(zero_shot_output)

print("\n" + "=" * 60)
print("ONE-SHOT PROMPT")
print("=" * 60)
print(one_shot_prompt)
print("\nGenerated Blog:\n")
print(one_shot_output)

print("\n" + "=" * 60)
print("FEW-SHOT PROMPT")
print("=" * 60)
print(few_shot_prompt)
print("\nGenerated Blog:\n")
print(few_shot_output)
