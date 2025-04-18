import os
import yaml
import re

def generate_nav():
    problems_dir = "docs/problems"
    nav_items = []
    
    # Get all problem files
    files = []
    for file in os.listdir(problems_dir):
        if file.endswith('.md'):
            problem_num = file.split('.')[0]
            # Convert to integer for proper numerical sorting
            try:
                num = int(problem_num)
                files.append((num, file))
            except ValueError:
                # Handle non-numeric filenames
                files.append((float('inf'), file))
    
    # Sort files numerically by problem number
    files.sort()
    
    for _, file in files:
        problem_num = file.split('.')[0]
        
        # Read file content
        with open(os.path.join(problems_dir, file), 'r') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            frontmatter_text = frontmatter_match.group(1)
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
                if 'title' in frontmatter and frontmatter['title']:
                    title = frontmatter['title']
                    # Check if title already includes the problem number
                    if title.startswith(f"{problem_num}."):
                        nav_items.append({title: f"problems/{file}"})
                    else:
                        nav_items.append({f"{problem_num}. {title}": f"problems/{file}"})
                    continue
            except Exception:
                pass
        
        # Fallback if frontmatter parsing fails
        nav_items.append({f"{problem_num}. ---": f"problems/{file}"})
        
    return nav_items


def update_mkdocs_yml():
    nav_items = generate_nav()
    
    # Read the current mkdocs.yml
    with open("mkdocs.yml", 'r') as f:
        content = f.read()
    
    # Split the content at the nav section
    parts = re.split(r'(nav:.*?)(?=\n\w+:|\Z)', content, maxsplit=1, flags=re.DOTALL)
    
    if len(parts) >= 2:
        # Found the nav section, replace it entirely
        before_nav = parts[0]
        after_nav = parts[2] if len(parts) > 2 else ""
        
        # Create a completely new nav section
        new_nav = "nav:\n  - Home: index.md\n  - Problems:\n"
        for item in nav_items:
            for title, path in item.items():
                new_nav += f"      - {title}: {path}\n"
        
        # Combine the parts
        new_content = before_nav + new_nav + after_nav
    else:
        # Nav section not found, append it
        new_nav = "\nnav:\n  - Home: index.md\n  - Problems:\n"
        for item in nav_items:
            for title, path in item.items():
                new_nav += f"      - {title}: {path}\n"
        
        new_content = content + new_nav
    
    # Write the updated content back
    with open("mkdocs.yml", 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_mkdocs_yml()
    print("Updated mkdocs.yml with problem navigation")
