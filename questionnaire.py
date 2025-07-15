import gradio as gr


def assess_user(name, age, email, employment, income, net_worth, objective, agree_docs):
    if not agree_docs:
        return "You must agree to the documents to proceed."

    user_data = {
        "Full Name": name,
        "Age": age,
        "Email": email,
        "Employment": employment,
        "Income": income,
        "Net Worth": net_worth,
        "Investment Objective": objective
    }

    summary = f"✅ Thank you, {name}!\n\nHere is your recorded profile:\n"
    for key, value in user_data.items():
        summary += f"- {key}: {value}\n"

    return summary


def investor_profile_gradio(
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
):
    score = 0
    ESG_P = False

    # Question 1
    if "Low risk/low return" in q1: score += 1
    elif "Some risk/medium return" in q1: score += 2
    elif "Higher risk/high return" in q1: score += 3
    elif "Highest risk/highest return" in q1: score += 4

    # Question 2
    if "Change the Portfolio" in q2: score += 1
    elif "Stay the Course" in q2: score += 3

    # Question 3
    if "I agree" in q3: score += 1
    elif "I somewhat agree" in q3: score += 2
    elif "I disagree" in q3: score += 3

    # Question 4
    if "Always" in q4: score += 4
    elif "Usually" in q4: score += 3
    elif "Sometimes" in q4: score += 2
    elif "Never" in q4: score += 1

    # Question 5
    if "strongly agree" in q5: score += 1
    elif "in between" in q5: score += 2
    elif "strongly disagree" in q5: score += 3

    # Question 6
    if "do not plan" in q6: score += 1
    elif "as I am able" in q6: score += 2
    elif "annual contributions" in q6: score += 3

    # Question 7
    if "All of it" in q7: score += 5
    elif "More than half" in q7: score += 4
    elif "Half" in q7: score += 3
    elif "Less than half" in q7: score += 2
    elif "Very little" in q7: score += 1

    # Question 8
    if "$200 gain" in q8: score += 1
    elif "$800 gain" in q8: score += 2
    elif "$2,600 gain" in q8: score += 3
    elif "$4,800 gain" in q8: score += 4

    # Question 9 – ESG
    ESG_P = q9 == "Yes"

    # Classification
    if score <= 12:
        profile = "🟦 Conservative"
        description = "You prioritize protecting your capital over high returns."
    elif score <= 24:
        profile = "🟨 Moderate"
        description = "You balance return and risk with moderate tolerance."
    else:
        profile = "🟥 Aggressive"
        description = "You pursue high growth and accept strong market volatility."

    return f"""**🎯 Profile:** {profile}  
**📊 Risk Score:** {score}  
**🌱 ESG Preference:** {"Yes" if ESG_P else "No"}  
**📈 Experience Investing:** {q10}

**🧭 Summary:** {description}
"""

def launch_questionnaires():
    
    user_ui = gr.Interface(
    fn=assess_user,
    inputs=[
        gr.Textbox(label="Full Name"),
        gr.Number(label="Age"),
        gr.Textbox(label="Email"),
        gr.Radio(["Student", "Employed", "Unemployed", "Retired", "Self-employed"], label="Employment Status"),
        gr.Radio(["€0–€30,000", "€30,000–€50,000", "€50,000–€80,000", "€80,000–€120,000", "€120,000+"], label="Annual Income"),
        gr.Radio(["€0–€10,000", "€10,000–€30,000", "€30,000–€100,000", "€100,000+"], label="Net Worth"),
        gr.Dropdown([
            "Long-term investments to maximize wealth growth",
            "Infrequent investments only when I see an opportunity",
            "Frequent investments focused on generating ongoing income",
            "Preserve capital with minimal risk",
            "Invest to learn"
        ], label="Investment Objective"),
        gr.Checkbox(label="I agree to all terms and documents")
    ],
    outputs=gr.Textbox(label="Summary"),
    title="RoboAdvisor - User Questionnaire"
    )
    
    risk_ui = gr.Interface(
    fn=investor_profile_gradio,
    inputs=[
        gr.Radio([
            "A. Low risk/low return (2–3% yearly; lose 2–5% in a bad year)",
            "B. Some risk/medium return (4% yearly; lose 10%)",
            "C. Higher risk/high return (6% yearly; lose 20%)",
            "D. Highest risk/highest return (7% yearly; lose 25%)"
        ], label="1. If you had €22,000 to invest for 10 years, which would you prefer?"),

        gr.Radio([
            "A. Change the Portfolio",
            "B. Stay the Course"
        ], label="2. If your portfolio drops by 15% in a year, what do you do?"),

        gr.Radio([
            "A. I agree",
            "B. I somewhat agree",
            "C. I disagree"
        ], label="3. When the market drops, do you shift to safer assets?"),

        gr.Radio([
            "A. Always",
            "B. Usually",
            "C. Sometimes",
            "D. Never"
        ], label="4. I would go for the best return even with risk involved."),

        gr.Radio([
            "A. I strongly agree with this statement",
            "B. I’m in between",
            "C. I strongly disagree with this statement"
        ], label="5. I prefer safety and slow growth even if overall return is lower."),

        gr.Radio([
            "A. I do not plan to make future contributions",
            "B. I plan to contribute as I can, not every year",
            "C. I plan to make annual contributions"
        ], label="6. Future investment contributions?"),

        gr.Radio([
            "A. All of it",
            "B. More than half",
            "C. Half",
            "D. Less than half",
            "E. Very little, if any"
        ], label="7. How much would you invest in high-risk opportunities?"),

        gr.Radio([
            "A. $200 gain best / $0 worst",
            "B. $800 gain best / $200 loss",
            "C. $2,600 gain best / $800 loss",
            "D. $4,800 gain best / $2,400 loss"
        ], label="8. Choose a best/worst case investment outcome:"),

        gr.Radio(["Yes", "No", "I'm not sure"], label="9. Would you prioritize ESG even with slightly lower returns?"),

        gr.Radio(["Yes", "No"], label="10. Do you have experience investing in financial markets?")
    ],
    outputs=gr.Markdown(),
    title="💼 Investor Risk Profile + ESG Preferences",
    description="This interactive quiz helps determine your risk appetite, ESG preference, and investment profile."
    )
    return user_ui, risk_ui
