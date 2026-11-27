
import streamlit as st

st.set_page_config(
    page_title="AI Master Quiz",
    page_icon="🧠",
    layout="centered"
)

questions = [
    ("AI stands for:", ["Automated Information", "Artificial Intelligence", "Advanced Internet", "Artificial Integration"], "B"),
    ("Machine Learning is a subset of:", ["Networking", "AI", "Hardware", "Operating System"], "B"),
    ("Deep Learning is a subset of:", ["Machine Learning", "Cybersecurity", "Database", "Robotics"], "A"),
    ("Which AI performs a specific task?", ["General AI", "Super AI", "Narrow AI", "Human AI"], "C"),
    ("General AI refers to:", ["Task-specific intelligence", "Human-level general intelligence", "Basic programming", "Data storage"], "B"),
    ("Super AI is:", ["Commonly available", "Hypothetical intelligence beyond humans", "A computer", "A search engine"], "B"),
    ("Generative AI is used to:", ["Generate new content", "Delete files", "Repair hardware", "Increase RAM"], "A"),
    ("Which is an example of Generative AI?", ["ChatGPT", "Calculator", "Keyboard", "Monitor"], "A"),
    ("LLM stands for:", ["Large Language Model", "Long Learning Machine", "Linear Language Method", "Large Logic Memory"], "A"),
    ("Machine Learning allows machines to:", ["Learn patterns from data", "Work without electricity", "Replace hardware", "Only store information"], "A"),
    ("A collection of data is called:", ["Algorithm", "Dataset", "Program", "Network"], "B"),
    ("Features in ML are:", ["Input characteristics", "Output devices", "Programming errors", "Hardware"], "A"),
    ("Teaching a model using data is called:", ["Testing", "Training", "Browsing", "Formatting"], "B"),
    ("A trained ML model makes:", ["Predictions", "Hardware", "Keyboards", "Networks"], "A"),
    ("Which data evaluates a trained model?", ["Training data", "Testing data", "Deleted data", "Unused data"], "B"),
    ("KNN stands for:", ["K-Nearest Neighbour", "Key Network Node", "Kernel Neural Network", "Known Number"], "A"),
    ("KNN is a:", ["Supervised algorithm", "Unsupervised algorithm", "Sorting algorithm", "Clustering-only algorithm"], "A"),
    ("KNN makes predictions based on:", ["Nearest data points", "Random selection", "Largest dataset", "Memory"], "A"),
    ("KNN classification uses:", ["Majority voting", "Random guessing", "Data deletion", "Sorting"], "A"),
    ("K-Means is mainly used for:", ["Classification", "Clustering", "Programming", "Networking"], "B"),
    ("K-Means is an example of:", ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Deep Learning"], "B"),
    ("The centre of a cluster is called:", ["Feature", "Centroid", "Dataset", "Neuron"], "B"),
    ("Naive Bayes is based on:", ["Newton's Law", "Bayes' Theorem", "Ohm's Law", "Boolean Algebra"], "B"),
    ("Naive Bayes is commonly used for:", ["Classification", "Clustering", "Hardware design", "Storage"], "A"),
    ("Which algorithm performs clustering?", ["KNN", "Naive Bayes", "K-Means", "All three"], "C"),
    ("Google Maps uses AI to:", ["Predict traffic", "Create hardware", "Edit photos", "Play music"], "A"),
    ("Spotify recommends songs based on:", ["Listening history", "Phone battery", "Screen size", "Keyboard speed"], "A"),
    ("Google Photos uses AI for:", ["Image recognition", "Calling", "Networking", "Programming"], "A"),
    ("Voice assistants use which technology?", ["NLP", "HTML", "CSS", "SQL"], "A"),
    ("Netflix uses AI mainly for:", ["Content recommendations", "Hardware manufacturing", "Internet speed", "File compression"], "A")
]

if "started" not in st.session_state:
    st.session_state.started = False

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

st.title("🧠 AI MASTER QUIZ")
st.caption("B.Tech CSE | Artificial Intelligence & Machine Learning")

st.divider()

if not st.session_state.started:

    st.subheader("Welcome to the AI Quiz!")

    st.write("📚 Total Questions: 30")
    st.write("🎯 Each question carries 1 mark.")
    st.write("📱 Mobile and laptop friendly.")
    st.write("⏳ No time limit.")

    if st.button("🚀 Start Quiz", use_container_width=True):
        st.session_state.started = True
        st.rerun()

elif st.session_state.current < len(questions):

    i = st.session_state.current
    q = questions[i]

    st.progress((i + 1) / len(questions))

    st.subheader(f"Question {i + 1} of {len(questions)}")

    st.write("### " + q[0])

    selected = st.radio(
        "Choose your answer:",
        ["A", "B", "C", "D"],
        format_func=lambda x: f"{x}. {q[1][ord(x) - 65]}",
        key=f"question_{i}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if i > 0:
            if st.button("⬅ Previous", use_container_width=True):
                st.session_state.current -= 1
                st.rerun()

    with col2:
        if st.button(
            "Next ➡" if i < len(questions) - 1 else "Submit Quiz",
            use_container_width=True
        ):
            st.session_state.answers[i] = selected

            if i < len(questions) - 1:
                st.session_state.current += 1
            else:
                st.session_state.current = len(questions)

            st.rerun()

else:

    score = 0

    for i, q in enumerate(questions):
        if st.session_state.answers.get(i) == q[2]:
            score += 1

    percentage = (score / len(questions)) * 100

    st.balloons()

    st.header("🏆 Quiz Completed!")

    st.metric("Your Score", f"{score} / 30")
    st.metric("Percentage", f"{percentage:.2f}%")

    st.write("Correct Answers:", score)
    st.write("Wrong Answers:", len(questions) - score)

    if score >= 27:
        st.success("Excellent performance! 🔥")
    elif score >= 21:
        st.success("Good performance! Keep it up.")
    elif score >= 15:
        st.warning("Average performance. Keep practising.")
    else:
        st.error("Needs improvement. Revise the topics.")

    st.divider()

    st.subheader("📋 Answer Review")

    for i, q in enumerate(questions):
        user_answer = st.session_state.answers.get(i, "Not answered")

        with st.expander(f"Q{i+1}. {q[0]}"):
            st.write("Your answer:", user_answer)
            st.write("Correct answer:", q[2])
            st.write("Correct option:", q[1][ord(q[2]) - 65])

            if user_answer == q[2]:
                st.success("Correct!")
            else:
                st.error("Incorrect!")

    if st.button("🔄 Restart Quiz", use_container_width=True):
        st.session_state.started = False
        st.session_state.current = 0
        st.session_state.answers = {}
        st.rerun()
