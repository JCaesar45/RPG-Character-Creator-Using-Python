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
