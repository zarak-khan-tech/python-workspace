import os
import sys

# ---------------------------
# 1. CREATE TEMPLATES FOLDER AND FILES
# ---------------------------

TEMPLATES_DIR = "templates"
HTML_FILES = {
    "base.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Tasty Bites{% endblock %}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: system-ui, 'Segoe UI', 'Helvetica Neue', sans-serif;
        }
        body {
            background: #fef9f0;
            color: #2c3e2f;
        }
        nav {
            background: #ff7b2c;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        .logo a {
            color: white;
            font-size: 1.8rem;
            font-weight: bold;
            text-decoration: none;
            letter-spacing: 1px;
        }
        .nav-links a {
            color: white;
            text-decoration: none;
            margin-left: 2rem;
            font-weight: 500;
            transition: 0.2s;
        }
        .nav-links a:hover {
            text-decoration: underline;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        footer {
            text-align: center;
            padding: 2rem;
            background: #2c3e2f;
            color: #ddd;
            margin-top: 3rem;
        }
        .btn {
            display: inline-block;
            background: #ff7b2c;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
        }
        .btn:hover {
            background: #e05f1a;
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #ff7b2c;
        }
        @media (max-width: 700px) {
            .nav-links a {
                margin-left: 1rem;
            }
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav>
        <div class="logo"><a href="/">🍲 Tasty Bites</a></div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/recipes">All Recipes</a>
        </div>
    </nav>

    <div class="container">
        {% block content %}{% endblock %}
    </div>

    <footer>
        &copy; 2025 Tasty Bites – Made with Python & Flask
    </footer>
</body>
</html>""",
    "index.html": """{% extends "base.html" %}

{% block title %}Home – Tasty Bites{% endblock %}

{% block content %}
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1>Welcome to Tasty Bites</h1>
        <p style="font-size: 1.2rem;">Discover delicious recipes from around the world.</p>
    </div>

    <h2>🌟 Featured Recipes</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 1.5rem;">
        {% for id, recipe in recipes.items() %}
        <div style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <img src="{{ recipe.image }}" alt="{{ recipe.title }}" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 1.2rem;">
                <h3>{{ recipe.title }}</h3>
                <p style="color: #555; margin: 0.5rem 0;">{{ recipe.description[:100] }}...</p>
                <a href="/recipe/{{ id }}" class="btn" style="margin-top: 0.5rem;">View Recipe →</a>
            </div>
        </div>
        {% endfor %}
    </div>
{% endblock %}""",
    "recipes.html": """{% extends "base.html" %}

{% block title %}All Recipes{% endblock %}

{% block content %}
    <h1>📖 All Recipes</h1>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 2rem;">
        {% for id, recipe in recipes.items() %}
        <div style="background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="{{ recipe.image }}" style="width: 100%; height: 180px; object-fit: cover;">
            <div style="padding: 1rem;">
                <h3>{{ recipe.title }}</h3>
                <p>{{ recipe.description[:80] }}…</p>
                <a href="/recipe/{{ id }}" class="btn">Cook this →</a>
            </div>
        </div>
        {% endfor %}
    </div>
{% endblock %}""",
    "recipe_detail.html": """{% extends "base.html" %}

{% block title %}{{ recipe.title }} - Tasty Bites{% endblock %}

{% block content %}
    <a href="/recipes" style="display: inline-block; margin-bottom: 1.5rem;">← Back to all recipes</a>

    <div style="display: flex; flex-wrap: wrap; gap: 2rem; background: white; border-radius: 24px; padding: 2rem; box-shadow: 0 4px 16px rgba(0,0,0,0.05);">
        <div style="flex: 1; min-width: 250px;">
            <img src="{{ recipe.image }}" alt="{{ recipe.title }}" style="width: 100%; border-radius: 20px;">
        </div>
        <div style="flex: 2;">
            <h1 style="margin-top: 0;">{{ recipe.title }}</h1>
            <p style="font-size: 1.1rem; line-height: 1.5;">{{ recipe.description }}</p>

            <h3>🥕 Ingredients</h3>
            <ul style="margin-left: 1.5rem; line-height: 1.6;">
                {% for item in recipe.ingredients %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>

            <h3>🍳 Instructions</h3>
            <ol style="margin-left: 1.5rem; line-height: 1.6;">
                {% for step in recipe.steps %}
                <li>{{ step }}</li>
                {% endfor %}
            </ol>
        </div>
    </div>
{% endblock %}"""
}

def setup_templates():
    """Create templates directory and all HTML files if they don't exist."""
    if not os.path.exists(TEMPLATES_DIR):
        os.makedirs(TEMPLATES_DIR)
        print(f"📁 Created folder: {TEMPLATES_DIR}/")
    for filename, content in HTML_FILES.items():
        filepath = os.path.join(TEMPLATES_DIR, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"📄 Created template: {filepath}")
        else:
            print(f"✓ Template already exists: {filepath}")

# ---------------------------
# 2. FLASK APPLICATION CODE
# ---------------------------

try:
    from flask import Flask, render_template, abort
except ImportError:
    print("❌ Flask is not installed. Please install it with: pip install flask")
    sys.exit(1)

app = Flask(__name__)

# Sample recipe data (dictionary)
recipes = {
    1: {
        "title": "Spaghetti Carbonara",
        "image": "https://images.unsplash.com/photo-1612874742237-6526221588e3?w=600",
        "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.",
        "ingredients": [
            "200g spaghetti",
            "100g pancetta or guanciale",
            "2 large eggs",
            "50g Pecorino Romano cheese",
            "50g Parmesan cheese",
            "Black pepper",
            "Salt"
        ],
        "steps": [
            "Boil salted water and cook spaghetti al dente.",
            "Fry pancetta until crisp.",
            "Beat eggs with grated cheeses and black pepper.",
            "Drain pasta, reserving some water. Mix hot pasta with pancetta.",
            "Remove from heat, add egg mixture and toss quickly.",
            "Add a little pasta water if needed. Serve immediately."
        ]
    },
    2: {
        "title": "Vegan Buddha Bowl",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
        "description": "A colourful, nutritious bowl with quinoa, roasted veggies, and a tahini dressing.",
        "ingredients": [
            "1 cup quinoa",
            "Sweet potato",
            "Chickpeas",
            "Kale",
            "Avocado",
            "Tahini",
            "Lemon juice",
            "Garlic"
        ],
        "steps": [
            "Cook quinoa according to package instructions.",
            "Roast sweet potato and chickpeas at 200°C for 20 min.",
            "Massage kale with olive oil and lemon.",
            "Make dressing: tahini + lemon + garlic + water.",
            "Assemble bowl: quinoa, veggies, avocado, drizzle dressing."
        ]
    },
    3: {
        "title": "Chicken Tikka Masala",
        "image": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600",
        "description": "Tender chicken in a creamy, spiced tomato curry. Perfect with rice or naan.",
        "ingredients": [
            "500g chicken breast",
            "1 cup yogurt",
            "Garam masala",
            "Tomato puree",
            "Heavy cream",
            "Onion",
            "Garlic & ginger",
            "Cilantro"
        ],
        "steps": [
            "Marinate chicken in yogurt + spices for 1 hour.",
            "Sauté onions, garlic, ginger. Add tomato puree and spices.",
            "Grill or pan-fry chicken until charred.",
            "Add chicken to sauce, stir in cream.",
            "Garnish with cilantro. Serve with basmati rice."
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html', recipes=recipes)

@app.route('/recipes')
def recipes_list():
    return render_template('recipes.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = recipes.get(recipe_id)
    if not recipe:
        abort(404)
    return render_template('recipe_detail.html', recipe=recipe, recipe_id=recipe_id)

# ---------------------------
# 3. RUN EVERYTHING
# ---------------------------
if __name__ == '__main__':
    print("\n🍽️  Setting up your Food Website...")
    setup_templates()
    print("\n🚀 Starting Flask server...")
    print("🌐 Open your browser at: http://127.0.0.1:5000")
    print("Press CTRL+C to stop.\n")
    app.run(debug=True)