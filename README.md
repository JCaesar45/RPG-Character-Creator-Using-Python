```
# RPG Character Creator

A Python module for creating and validating RPG characters with specific stat requirements.

## Description

This module provides a function to create RPG characters by validating a character name and three stats (strength, intelligence, and charisma). The function ensures all inputs meet specific criteria before generating a formatted character sheet.

## Function

```python
def create_character(name, strength, intelligence, charisma):
    # Validate name
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return "The character name should not contain spaces"
    
    # Validate stats
    stats = [strength, intelligence, charisma]
    
    # Check if all stats are integers
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    
    # Check if all stats are within the valid range
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    
    # Check if stats sum to 7
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    # Format the output
    result = [name]
    
    # Format each stat line
    stat_names = ["STR", "INT", "CHA"]
    for i, stat in enumerate(stats):
        filled_dots = "●" * stat
        empty_dots = "○" * (10 - stat)
        result.append(f"{stat_names[i]} {filled_dots}{empty_dots}")
    
    return "\n".join(result)
``

## Usage

The `create_character` function takes four parameters:
1. `name` (string): The character's name
2. `strength` (int): The character's strength stat (1-4)
3. `intelligence` (int): The character's intelligence stat (1-4)
4. `charisma` (int): The character's charisma stat (1-4)

### Validation Rules

**Name Requirements:**
- Must be a string
- Maximum 10 characters
- Cannot contain spaces

**Stat Requirements:**
- All stats must be integers
- Each stat must be between 1 and 4 (inclusive)
- The sum of all stats must equal 7

### Examples

#### Valid Input
```python
print(create_character("ren", 4, 2, 1))
``

**Output:**
``
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
``

#### Invalid Inputs

**Non-string name:**
```python
print(create_character(123, 4, 2, 1))
``
**Output:**
``
The character name should be a string
``

**Name too long:**
```python
print(create_character("verylongname", 4, 2, 1))
``
**Output:**
``
The character name is too long
``

**Name with space:**
```python
print(create_character("ren hoek", 4, 2, 1))
``
**Output:**
``
The character name should not contain spaces
``

**Non-integer stat:**
```python
print(create_character("ren", 4.5, 2, 1))
``
**Output:**
``
All stats should be integers
``

**Stat too low:**
```python
print(create_character("ren", 0, 3, 4))
``
**Output:**
``
All stats should be no less than 1
``

**Stat too high:**
```python
print(create_character("ren", 5, 1, 1))
``
**Output:**
``
All stats should be no more than 4
``

**Stats don't sum to 7:**
```python
print(create_character("ren", 3, 3, 3))
``
**Output:**
``
The character should start with 7 points
``

## Testing

To test the function, run the provided test cases that verify all validation rules and output formatting.
