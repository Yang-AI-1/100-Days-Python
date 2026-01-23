"""
FOR LOOPS vs COMPREHENSIONS: Understanding the One-Liner
==========================================================
Why you can sometimes skip colons and indentation
"""

# ============================================================================
# PART 1: THE TRADITIONAL FOR LOOP (What Angela taught you)
# ============================================================================

print("=" * 70)
print("TRADITIONAL FOR LOOP")
print("=" * 70)

# Building a list the traditional way
squares = []
for num in [1, 2, 3, 4, 5]:
    result = num ** 2
    squares.append(result)
    print(f"Processing {num}: {num}² = {result}")

print(f"\nFinal list: {squares}")


# ============================================================================
# PART 2: LIST COMPREHENSION (The one-liner version)
# ============================================================================

print("\n" + "=" * 70)
print("LIST COMPREHENSION (One-liner)")
print("=" * 70)

# The exact same result, but in one line
squares = [num ** 2 for num in [1, 2, 3, 4, 5]]
print(f"Final list: {squares}")

print("\nThey produce IDENTICAL results!")


# ============================================================================
# PART 3: SIDE-BY-SIDE COMPARISON
# ============================================================================

print("\n" + "=" * 70)
print("SIDE-BY-SIDE ANATOMY")
print("=" * 70)

print("""
TRADITIONAL LOOP:                   LIST COMPREHENSION:
─────────────────                   ──────────────────
squares = []                        squares = [num ** 2 for num in [1,2,3]]
for num in [1, 2, 3]:                         │      │          │
    squares.append(num ** 2)                  │      │          └─ sequence
                                               │      └─ loop variable
                                               └─ expression

Key difference: Comprehension is BACKWARDS!
- Traditional: for → variable → do something → append
- Comprehension: what to append → for → variable → from where
""")


# ============================================================================
# PART 4: YOUR LOVE SCORE EXAMPLE EXPLAINED
# ============================================================================

print("=" * 70)
print("YOUR LOVE SCORE EXAMPLE - BOTH WAYS")
print("=" * 70)

combined = "kanyewestkimkardashian"

# METHOD 1: Traditional loop (what you're used to)
print("\nMETHOD 1 - Traditional loop:")
true_count = 0
for letter in "true":
    count = combined.count(letter)
    true_count += count
    print(f"  Letter '{letter}': found {count} times → running total: {true_count}")

print(f"✓ Final true_count: {true_count}")


# METHOD 2: Generator expression with sum (the one-liner)
print("\nMETHOD 2 - Generator expression:")
true_count = sum(combined.count(letter) for letter in "true")
print(f"✓ Final true_count: {true_count}")

print("\nHow it works internally:")
print("  1. for letter in 'true' → loops: t, r, u, e")
print("  2. combined.count(letter) → generates: 2, 1, 0, 4")
print("  3. sum(...) → adds them: 2 + 1 + 0 + 4 = 7")


# ============================================================================
# PART 5: THE THREE TYPES OF COMPREHENSIONS
# ============================================================================

print("\n" + "=" * 70)
print("THREE TYPES OF COMPREHENSIONS IN PYTHON")
print("=" * 70)

# 1. LIST COMPREHENSION [creates a list]
print("\n1. LIST COMPREHENSION → creates a [list]")
list_result = [x * 2 for x in range(5)]
print(f"   [x * 2 for x in range(5)] = {list_result}")
print(f"   Type: {type(list_result)}")

# 2. GENERATOR EXPRESSION (creates a generator - memory efficient)
print("\n2. GENERATOR EXPRESSION → creates a (generator)")
gen_result = (x * 2 for x in range(5))
print(f"   (x * 2 for x in range(5)) = {gen_result}")
print(f"   Type: {type(gen_result)}")
print(f"   Values: {list(gen_result)} ← converts to list to see values")

# 3. DICTIONARY COMPREHENSION {creates a dict}
print("\n3. DICTIONARY COMPREHENSION → creates a {{dict}}")
dict_result = {x: x**2 for x in range(5)}
print(f"   {{x: x**2 for x in range(5)}} = {dict_result}")
print(f"   Type: {type(dict_result)}")


# ============================================================================
# PART 6: WHEN TO USE WHICH?
# ============================================================================

print("\n" + "=" * 70)
print("WHEN TO USE EACH STYLE")
print("=" * 70)

print("""
USE TRADITIONAL FOR LOOPS WHEN:
✓ You need to do multiple things in each iteration
✓ The logic is complex (multiple if statements, nested operations)
✓ You're still learning and want clarity
✓ You need to use break/continue statements

Example:
    for user in users:
        if user.is_active:
            send_email(user)
            log_action(user)
            update_database(user)

USE COMPREHENSIONS WHEN:
✓ You're transforming one sequence into another
✓ The operation is simple (one expression)
✓ You want cleaner, more readable code
✓ You care about memory efficiency (generators)

Example:
    active_emails = [user.email for user in users if user.is_active]
""")


# ============================================================================
# PART 7: PROGRESSIVE EXAMPLES (Simple → Complex)
# ============================================================================

print("=" * 70)
print("PROGRESSIVE EXAMPLES: Building Complexity")
print("=" * 70)

# Level 1: Basic transformation
print("\n📊 Level 1 - Basic transformation:")
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(f"Original: {numbers}")
print(f"Doubled:  {doubled}")

# Level 2: With filtering
print("\n📊 Level 2 - With filtering:")
even_doubled = [n * 2 for n in numbers if n % 2 == 0]
print(f"Even numbers doubled: {even_doubled}")

# Level 3: With conditional expression
print("\n📊 Level 3 - With conditional expression:")
labeled = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Labeled: {labeled}")

# Level 4: Nested comprehension (2D list)
print("\n📊 Level 4 - Nested (creating a grid):")
grid = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print("Multiplication table:")
for row in grid:
    print(f"  {row}")


# ============================================================================
# PART 8: MEMORY EFFICIENCY DEMONSTRATION
# ============================================================================

print("\n" + "=" * 70)
print("BONUS: MEMORY EFFICIENCY")
print("=" * 70)

import sys

# List comprehension - creates entire list in memory
list_comp = [x for x in range(1000)]
print(f"\nList comprehension size: {sys.getsizeof(list_comp):,} bytes")

# Generator expression - creates values on demand
gen_exp = (x for x in range(1000))
print(f"Generator expression size: {sys.getsizeof(gen_exp):,} bytes")

print("\n💡 Generators are ~100x more memory efficient!")
print("   That's why sum() uses a generator expression, not a list.")


# ============================================================================
# FINAL COMPARISON: Your Love Score
# ============================================================================

print("\n" + "=" * 70)
print("YOUR LOVE SCORE: ALL THREE METHODS")
print("=" * 70)

combined = "kanyewestkimkardashian"

# Method 1: Your original way (most explicit)
print("\n1️⃣  ORIGINAL (4 loops, very explicit):")
true_count = 0
for letter in combined:
    if letter in "true":
        true_count += 1
print(f"   Result: {true_count}")

# Method 2: Optimized loop (fewer iterations)
print("\n2️⃣  OPTIMIZED LOOP (cleaner, fewer iterations):")
true_count = 0
for letter in "true":
    true_count += combined.count(letter)
print(f"   Result: {true_count}")

# Method 3: One-liner (most Pythonic)
print("\n3️⃣  PYTHONIC ONE-LINER (most concise):")
true_count = sum(combined.count(letter) for letter in "true")
print(f"   Result: {true_count}")

print("\n" + "=" * 70)
print("All three give the same answer! Pick what makes sense to YOU.")
print("=" * 70)