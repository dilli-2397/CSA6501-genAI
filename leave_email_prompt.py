# Prompt Engineering Demo
# Topic: Leave Request Email Due to Illness

# --------------------------------------------------
# Zero-shot Prompt
# --------------------------------------------------

zero_prompt = """
Write a professional email requesting leave due to illness.
"""

zero_email = """
Subject: Leave Request Due to Illness

Dear Sir/Madam,

I am feeling unwell due to illness and am unable to attend work today.
I kindly request leave for one day so that I can recover properly.
I will resume my duties as soon as my health improves.

Thank you for your understanding.

Yours sincerely,
John
"""

# --------------------------------------------------
# One-shot Prompt
# --------------------------------------------------

one_prompt = """
Example

Task:
Write a professional email requesting permission to attend a family function.

Email:
Subject: Leave Request

Dear Sir,

I request leave for one day to attend a family function.
I will complete my pending work after returning.

Thank you.

Now write a professional email requesting leave due to illness.
"""

one_email = """
Subject: Sick Leave Request

Dear Sir/Madam,

I am writing to inform you that I am suffering from a fever and have been
advised to take rest. Therefore, I kindly request leave for today.
I will return to work as soon as I recover and complete any pending tasks.

Thank you for your consideration.

Sincerely,
John
"""

# --------------------------------------------------
# Few-shot Prompt
# --------------------------------------------------

few_prompt = """
Example 1

Task:
Write an email requesting leave for a family event.

Email:
Dear Sir,
I request leave for one day to attend a family event.
Thank you.

Example 2

Task:
Write an email requesting leave for an examination.

Email:
Dear Sir,
I request leave to attend my examination.
Thank you.

Example 3

Task:
Write an email requesting leave for personal reasons.

Email:
Dear Sir,
I request leave due to personal reasons.
Thank you.

Now write a professional email requesting leave due to illness.
"""

few_email = """
Subject: Request for Sick Leave

Dear Sir/Madam,

I hope you are doing well. I am writing to inform you that I am feeling
unwell due to illness and my doctor has advised me to take rest.
Therefore, I kindly request leave for one day.

I will keep you updated about my health and complete any pending work
once I return.

Thank you for your understanding and support.

Yours faithfully,
John
"""

# --------------------------------------------------
# Display Output
# --------------------------------------------------

print("=" * 60)
print("ZERO-SHOT PROMPT")
print("=" * 60)
print(zero_prompt)
print("\nGenerated Email:\n")
print(zero_email)

print("\n" + "=" * 60)
print("ONE-SHOT PROMPT")
print("=" * 60)
print(one_prompt)
print("\nGenerated Email:\n")
print(one_email)

print("\n" + "=" * 60)
print("FEW-SHOT PROMPT")
print("=" * 60)
print(few_prompt)
print("\nGenerated Email:\n")
print(few_email)

# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
1. Tone
   - Zero-shot : Professional
   - One-shot  : More polite and formal
   - Few-shot  : Highly professional and courteous

2. Grammar
   - Zero-shot : Correct
   - One-shot  : Excellent
   - Few-shot  : Excellent

3. Formatting
   - Zero-shot : Includes subject, greeting, and closing
   - One-shot  : Well-organized
   - Few-shot  : Best structure and formatting

4. Completeness
   - Zero-shot : Covers the basic request
   - One-shot  : Includes reason and assurance
   - Few-shot  : Includes reason, leave request, future update, and appreciation

Conclusion:
Few-shot prompting produces the most professional, complete, and well-formatted email.
""")
