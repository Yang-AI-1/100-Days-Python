"""
Breaking down the loop logic in detail
"""

print("=" * 70)
print("COMPARING LOOP APPROACHES")
print("=" * 70)

name1 = "Kanye West"
name2 = "Kim Kardashian"

# ============================================================================
# YOUR ORIGINAL APPROACH (4 separate loops)
# ============================================================================
print("\n📌 YOUR ORIGINAL APPROACH (4 loops):")
print("-" * 70)

true_holder = 0
love_holder = 0

print(f"\nProcessing name1: '{name1}'")
print("Loop 1 - Counting TRUE letters in name1:")
for letter in name1.lower():
    if letter == "t" or letter == "r" or letter == "u" or letter == "e":
        true_holder += 1
        print(f"  Found '{letter}' → true_holder = {true_holder}")

print(f"\nLoop 2 - Counting LOVE letters in name1:")
for letter in name1.lower():
    if letter == "l" or letter == "o" or letter == "v" or letter == "e":
        love_holder += 1
        print(f"  Found '{letter}' → love_holder = {love_holder}")

print(f"\nProcessing name2: '{name2}'")
print("Loop 3 - Counting TRUE letters in name2:")
for letter in name2.lower():
    if letter == "t" or letter == "r" or letter == "u" or letter == "e":
        true_holder += 1
        print(f"  Found '{letter}' → true_holder = {true_holder}")

print(f"\nLoop 4 - Counting LOVE letters in name2:")
for letter in name2.lower():
    if letter == "l" or letter == "o" or letter == "v" or letter == "e":
        love_holder += 1
        print(f"  Found '{letter}' → love_holder = {love_holder}")

print(f"\n✓ Final counts: TRUE={true_holder}, LOVE={love_holder}")
print(f"✓ Love score = {true_holder}{love_holder}")

# ============================================================================
# IMPROVED APPROACH (2 operations using count())
# ============================================================================
print("\n" + "=" * 70)
print("📌 IMPROVED APPROACH (using .count() method):")
print("-" * 70)

# Step 1: Combine names
combined = (name1 + name2).lower()
print(f"\nStep 1 - Combined names: '{combined}'")

# Step 2: Count TRUE letters
print(f"\nStep 2 - Counting TRUE letters:")
print(f"  't' appears: {combined.count('t')} times")
print(f"  'r' appears: {combined.count('r')} times")
print(f"  'u' appears: {combined.count('u')} times")
print(f"  'e' appears: {combined.count('e')} times")

true_count = sum(combined.count(letter) for letter in "true")
print(f"  → Total TRUE letters: {true_count}")

# Step 3: Count LOVE letters
print(f"\nStep 3 - Counting LOVE letters:")
print(f"  'l' appears: {combined.count('l')} times")
print(f"  'o' appears: {combined.count('o')} times")
print(f"  'v' appears: {combined.count('v')} times")
print(f"  'e' appears: {combined.count('e')} times")

love_count = sum(combined.count(letter) for letter in "love")
print(f"  → Total LOVE letters: {love_count}")

print(f"\n✓ Final counts: TRUE={true_count}, LOVE={love_count}")
print(f"✓ Love score = {true_count}{love_count}")

# ============================================================================
# DETAILED BREAKDOWN OF LIST COMPREHENSION
# ============================================================================
print("\n" + "=" * 70)
print("📌 UNDERSTANDING: sum(combined.count(letter) for letter in 'true')")
print("-" * 70)

print("\nThis line does 3 things in one go:")
print("\n1. 'for letter in \"true\"' → loops through: t, r, u, e")
print("2. 'combined.count(letter)' → counts each letter in the string")
print("3. 'sum(...)' → adds all the counts together")

print("\nLet's see it step by step:")
counts = []
for letter in "true":
    count = combined.count(letter)
    counts.append(count)
    print(f"  Letter '{letter}': found {count} times")

print(f"\nCounts list: {counts}")
print(f"sum(counts) = {sum(counts)}")

print("\n" + "=" * 70)
print("EFFICIENCY COMPARISON:")
print("-" * 70)
print(f"Your approach: Loops through '{combined}' 4 times")
print(f"Length of combined string: {len(combined)} characters")
print(f"Total iterations: {len(combined)} × 4 = {len(combined) * 4}")
print(f"\nImproved approach: Uses .count() which is optimized in C")
print(f"Total operations: 8 counts (4 for TRUE, 4 for LOVE)")
print("=" * 70)