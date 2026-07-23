# Prompt Engineering Demo
# Product: Smart Fitness Watch

# -----------------------------
# Zero-shot Prompt
# -----------------------------
zero_shot_prompt = """
Write a product description for a Smart Fitness Watch.
Include:
- Heart Rate Monitoring
- Sleep Tracking
- GPS
- Water Resistance
- Long Battery Life
- Smartphone Connectivity
"""

zero_shot_output = """
Smart Fitness Watch is your perfect fitness companion.
It features heart rate monitoring, sleep tracking, built-in GPS,
water resistance, and long-lasting battery life.
Stay connected with smartphone notifications while tracking
your daily activities and workouts.
Its stylish design makes it ideal for everyday use.
"""

# -----------------------------
# One-shot Prompt
# -----------------------------
one_shot_prompt = """
Example:

Product: Wireless Bluetooth Earbuds

Description:
Experience crystal-clear sound with Wireless Bluetooth Earbuds.
Enjoy noise cancellation, 24-hour battery life, and seamless Bluetooth connectivity.

Now write a product description for a Smart Fitness Watch.
"""

one_shot_output = """
Take your fitness journey to the next level with the Smart Fitness Watch.
Monitor your heart rate, sleep quality, and daily steps.
With built-in GPS, water resistance, long battery life,
and smartphone connectivity, it helps you stay healthy,
active, and connected wherever you go.
"""

# -----------------------------
# Few-shot Prompt
# -----------------------------
few_shot_prompt = """
Example 1

Product: Wireless Bluetooth Earbuds

Description:
Enjoy premium sound quality with noise cancellation and long battery life.

Example 2

Product: Smart Water Bottle

Description:
Track your hydration with smart reminders and temperature control.

Example 3

Product: Portable Power Bank

Description:
Fast charging, compact design, and high-capacity battery.

Now write a product description for a Smart Fitness Watch.
"""

few_shot_output = """
Achieve your fitness goals with the Smart Fitness Watch.
It offers heart rate monitoring, sleep tracking, GPS,
multiple sports modes, water resistance, and smartphone notifications.
Its lightweight design and long battery life make it the perfect
choice for workouts and everyday activities.
"""

# Display Results
print("=" * 60)
print("ZERO-SHOT PROMPT")
print("=" * 60)
print(zero_shot_prompt)
print("\nGenerated Description:")
print(zero_shot_output)

print("\n" + "=" * 60)
print("ONE-SHOT PROMPT")
print("=" * 60)
print(one_shot_prompt)
print("\nGenerated Description:")
print(one_shot_output)

print("\n" + "=" * 60)
print("FEW-SHOT PROMPT")
print("=" * 60)
print(few_shot_prompt)
print("\nGenerated Description:")
print(few_shot_output)
