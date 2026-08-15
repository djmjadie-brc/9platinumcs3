# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Dierrel Jed M. Jadie
**Section:** 9-Platinum
**Last Name:** Jadie
**Date:** August 15, 2026
---

## Step 1: Identify the Big Problem
### Main Problem

The PSHS school canteen often gets crowded during lunch break because the process is inefficient due to it mostly being manual and the lack of visibility on items.

---
## Step 2: Identify the Sub-Problems
1. Many students take too long to decide what to order as they cannot see the menu easily, making ordering times longer.
2. Manually calculating totals and change to the person makes payments slower.
3. Staff cannot easily tell whether a food item is running out due to having no tracker.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Many students take too long to decide what to order as they cannot see the menu easily, making ordering times longer. | Abstraction | Add a digital menu outside the waiting line and show only high-demand items and the menu items for the pay-as meal plan to make ordering faster and easier to read. |
| Manually calculating totals and change to the person makes payments slower. | Algorithm Design | Create a program where the cashier inputs the total price of the order and the money given by the student in which it automatically shows the change needed to be given.|
| Staff cannot easily tell whether a food item is running out due to having no tracker. | Algorithm Desgin | Create a program where if a food item is running out, it tells them what item is running out of stock in which it needs to be restocked.
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Staff cannot easily tell whether a food item is running out due to having no tracker.
### Pseudocode
START

INPUT number of items ordered
OUTPUT "enter price of each item"
INPUT price of each item
OUTPUT total price

OUTPUT "enter amount given by the student"
INPUT amt given by the student

IF total price <= amt given:
  OUTPUT (amt given) - (total price)
ELIF total price > amt given:
  OUTPUT "short on payment by (total price) - (amt given)
ELSE:
  OUTPUT "invalid payment"

END
---
