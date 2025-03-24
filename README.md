# 💁 Education Helper

## **🎓 What We'll Learn**

Hey there\! In this task, you will **improve a simple Q\&A AI driven web application** built with Django. The final project will:

1. **Use Google's Gemini API** to generate answers.
2. **Have nicer, cleaner CSS** so the interface is user-friendly.
3. **Remove unnecessary JavaScript code** and keep the script neat.
4. **Include updated documentation** that walks through all the changes.

By completing this project, you'll learn:

- How to make **basic Django views and routes**.
- How to integrate an external AI API (Google Gemini) in Python.
- How to **refine CSS** styles for a better user experience.
- How to **organize and simplify JavaScript** code.
- How to write a **friendly, clear README** with instructions and explanations.

## **📁 Project Structure**

For a detailed overview of the project's organization and what each file does, please check the [STRUCTURE.md](STRUCTURE.md) file. This will help you navigate the codebase and understand where to make changes.

---

## **🌱 Task**

1. **Improve the CSS**

   - Open `static/css/style.css`.
   - Make it look more visually appealing. For example, adjust fonts, colors, spacing, or anything you find helpful. Keep it simple, but ensure it’s comfortable to read and use.

2. **Integrate Google Gemini**

   - Remove the placeholder code (or any old comments) in `views.py` where we previously had a “placeholder” response.
   - Use the **Gemini API** with your **own API key** to generate answers.
   - Here’s a [Google’s AI documentation](https://ai.google.dev/gemini-api/docs/quickstart?lang=python) you might find useful
   - Make sure you replace `"YOUR_API_KEY"` with your actual [Gemini API key](https://aistudio.google.com/app/apikey). You can store this key in an environment variable (like `GEMINI_API_KEY`) and load it in Django.

3. **Remove unused JavaScript**

   - Check out `static/js/script.js`.
   - There might be some lines or placeholders you no longer need (for instance, if there was old code for a placeholder answer).
   - Clean them up, but be careful not to break the functionality of the Q\&A forms.

4. **Update Documentation**

   - In this file `README.md`, explain how someone can:
     1. Install dependencies (Django, `google-genai`, etc.).
     2. Set the `GEMINI_API_KEY` in their environment.
     3. Run the server locally.
     4. Use the project (step-by-step instructions).

     Start from [README_EXAMPLE.md](README_EXAMPLE.md)

5. **Push to GitHub**

   - Include your final solution in a public GitHub repository.
   - Make sure your **README.md** is crystal clear so others can try your Q\&A app without confusion\!


---



