# Prompt Engineering - Article Summarization
# Zero-shot, One-shot, and Few-shot Prompt Demo

# --------------------------------------------------
# Article to Summarize
# --------------------------------------------------

article = """
Artificial Intelligence (AI) is transforming many industries by automating tasks,
improving decision-making, and increasing efficiency. In healthcare, AI helps doctors
diagnose diseases, predict patient outcomes, and recommend personalized treatments.
In education, AI enables personalized learning, automated grading, and virtual tutors.
In agriculture, AI assists farmers in monitoring crop health, detecting diseases,
and improving productivity. Despite its benefits, AI also raises concerns about
privacy, security, bias, and job displacement. Responsible development and ethical
use are essential to maximize the benefits of AI while minimizing its risks.
"""

# --------------------------------------------------
# Zero-shot Prompt
# --------------------------------------------------

zero_prompt = """
Summarize the following article in exactly 50 words.

Article:
""" + article

zero_summary = """
Artificial Intelligence improves healthcare, education, and agriculture through
automation, accurate decision-making, and personalized services. It enhances
diagnosis, learning, and crop management while increasing efficiency. However,
privacy, security, bias, and employment concerns remain important. Ethical AI
development is necessary to ensure responsible and beneficial use.
"""

# --------------------------------------------------
# One-shot Prompt
# --------------------------------------------------

one_prompt = """
Example

Article:
Renewable energy reduces pollution and protects the environment.
Solar and wind power are sustainable energy sources.

Summary (50 words):
Renewable energy protects the environment by reducing pollution and
using sustainable resources such as solar and wind power. It helps
meet energy needs while minimizing environmental damage and supporting
long-term economic and ecological development.

Now summarize the given AI article in 50 words.
"""

one_summary = """
Artificial Intelligence transforms industries by improving efficiency,
automating tasks, and supporting better decisions. It strengthens
healthcare through diagnosis, education through personalized learning,
and agriculture through crop monitoring. Challenges include privacy,
security, and bias. Responsible AI practices are essential for
maximizing benefits while reducing risks.
"""

# --------------------------------------------------
# Few-shot Prompt
# --------------------------------------------------

few_prompt = """
Example 1

Article:
Electric vehicles reduce fuel consumption and air pollution.

Summary:
Electric vehicles improve environmental sustainability by reducing
fuel usage and harmful emissions.

Example 2

Article:
Cloud computing enables data storage and online services.

Summary:
Cloud computing provides scalable storage, easy access, and cost-effective
online computing services.

Example 3

Article:
Cybersecurity protects computer systems from attacks.

Summary:
Cybersecurity safeguards data, networks, and systems against digital threats.

Now summarize the given AI article in exactly 50 words.
"""

few_summary = """
Artificial Intelligence enhances healthcare, education, and agriculture
by automating processes, improving decisions, and increasing productivity.
It supports disease diagnosis, personalized learning, and crop monitoring.
Although AI offers significant benefits, challenges including privacy,
security, bias, and ethics require responsible implementation and governance.
"""

# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("="*70)
print("ZERO-SHOT PROMPT")
print("="*70)
print(zero_prompt)
print("\nGenerated Summary:\n")
print(zero_summary)

print("\n" + "="*70)
print("ONE-SHOT PROMPT")
print("="*70)
print(one_prompt)
print("\nGenerated Summary:\n")
print(one_summary)

print("\n" + "="*70)
print("FEW-SHOT PROMPT")
print("="*70)
print(few_prompt)
print("\nGenerated Summary:\n")
print(few_summary)

print("\n" + "="*70)
print("COMPARISON")
print("="*70)

print("""
1. Accuracy
   - Zero-shot : Good
   - One-shot  : Very Good
   - Few-shot  : Excellent

2. Completeness
   - Zero-shot : Covers most important points.
   - One-shot  : Covers all key ideas clearly.
   - Few-shot  : Covers all important points concisely.

3. Readability
   - Zero-shot : Easy to understand.
   - One-shot  : Well-structured and smooth.
   - Few-shot  : Most clear, concise, and natural.
""")
