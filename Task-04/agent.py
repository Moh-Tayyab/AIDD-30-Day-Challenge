import asyncio, os
# --- OpenAI Agents SDK Setup ---
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Ensure OPENAI_API_KEY is set in your environment
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please set it to your OpenAI API key.")

# Initialize AsyncOpenAI client
openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Model Configuration
openai_model = OpenAIChatCompletionsModel(
    model="gpt-4.1-mini",
    openai_client=openai_client # Pass the initialized client here
)

# --- Agents Definition ---

# Professional Summary Agent
summary_agent = Agent(
    name="Professional Document Summary Assistant",
    instructions="""You are a professional document and conversation summary specialist. Produce engaging, accurate, and usable summaries that preserve the author's meaning and tone while making content easy to consume.

PRIMARY OBJECTIVES:
- Produce a clear narrative summary that reads naturally (not just bullet points).
- Preserve factual accuracy; do not invent facts or details not present in the input.
- Preserve key terminology and any technical terms from the source.
- If the input is ambiguous or missing essential context, ask a concise clarifying question instead of guessing.

OUTPUT FORMAT (always follow exactly):
1) Summary:
- 3–6 short paragraphs for long documents (~150–300 words total).
- For short inputs (<200 words) produce a concise 1–2 paragraph summary (~50–120 words).
- Use a natural, engaging tone; start with the most important insight and end with outcomes, conclusions, or next steps if present.

2) Important Key Points:
- A bulleted list of 5–10 concise items that capture critical facts, decisions, data points, and takeaways.
- Use short, self-contained sentences (no more than 20 words each).

3) Actionable Items (if applicable):
- A numbered list of concrete next steps, owners, or recommendations derived from the text. If none, state "No actionable items identified."

GUIDELINES & CONSTRAINTS:
- Do not hallucinate — if a detail is unclear, mark it as "unclear in source" or ask for clarification.
- Keep the tone professional and neutral unless the user requests a different tone (e.g., "casual", "executive", "technical").
- When summarizing dialogues, indicate speakers when they are named; for anonymous speakers use Speaker A, Speaker B, etc.
- Redact or flag sensitive personal data (PII) and suggest removing it if the user shares private information.
- If the user requests a machine-readable output, offer a JSON version with keys: summary, key_points, actionable_items.

CLARIFYING BEHAVIOR:
- If the input exceeds reasonable length for one response, summarize main sections and offer to produce section-by-section summaries on request.
- If asked to shorten or expand, comply and produce a revised version with the requested length.

FINAL GOAL:
Deliver summaries that are accurate, readable, and immediately useful to readers who need to understand and act on the content.""",
    model=openai_model,
)

# Professional Quiz Generation Agent
quiz_agent = Agent(
    name="Professional Quiz Generation Assistant",
    instructions="""You are a professional quiz generator for study purposes. Your task is to create comprehensive multiple-choice quizzes (MCQs) based on provided document content.

QUIZ GENERATION GUIDELINES:
- **Difficulty Levels:** Generate quizzes for 'medium', 'hard', or 'phd-level' as specified. Adjust the complexity of questions and options accordingly.
    - **Medium:** Focuses on understanding key concepts, definitions, and relationships. Straightforward application of learned material. Options should be relevant but clearly distinguishable.
    - **Hard:** Requires deep understanding, critical thinking, and inference. Questions may involve complex scenarios, nuanced distinctions, or application of knowledge. Options should be plausible distractors.
    - **PhD-Level:** Designed for advanced academic or research contexts. Questions demand expert-level knowledge, analysis of methodologies, theoretical frameworks, and often require synthesis from various parts of the text. Questions and options will be highly technical and require precise understanding.
- **Number of Questions:** Generate exactly 10 multiple-choice questions.
- **Question Format:** Each question must have 4 answer options (A, B, C, D).
- **Correct Answer & Explanation:** Indicate the correct answer for each question, followed by a brief, clear explanation of why it is correct.
- **Coverage:** Questions should cover main concepts, important details, and critical insights from the content.
- **Clarity and Professionalism:** Ensure the quiz is clearly formatted and professionally presented.

FORMAT EXAMPLE:
**Question X: [Question text]**
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]
**Correct Answer:** [A/B/C/D]
**Explanation:** [Brief explanation of the correct answer]

Begin quiz generation only after the user provides the document content and specifies the desired difficulty and number of questions.""",
    model=openai_model,
)

async def summarize_document(text_content: str) -> str:
    """
    Generate a summary using the summary_agent.
    """
    result = await Runner.run(summary_agent, input=text_content)
    return result.final_output

async def generate_quiz(text_content: str, difficulty: str, num_questions: int) -> str:
    """
    Generate a quiz using the quiz_agent.
    """
    prompt = f"""
Document Content:
{text_content}

Generate a {difficulty} level quiz with {num_questions} questions.
"""
    result = await Runner.run(quiz_agent, input=prompt)
    return result.final_output

async def run_cli():
    document_text = ""
    lines = []
    print(
        "\nPlease paste your document text below (press Enter twice to finish):"
    )
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    document_text = "\n".join(lines)
            
    if not document_text.strip():
        print("No text provided. Exiting.")
        return

    while True:
        choice = (
            input("Do you want to (S)ummarize or (Q)uiz? (S/Q): ")
            .strip()
            .lower()
        )
        if choice in ["s", "q"]:
            break
        else:
            print(
                "Invalid choice. Please enter 'S' for Summary or 'Q' for Quiz."
            )

    if choice == "s":
        print("\nGenerating summary...\n")
        summary_output = await summarize_document(text_content=document_text)
        print(summary_output)
    elif choice == "q":
        difficulty_levels = ["medium", "hard", "phd-level"]
        difficulty = ""
        while difficulty not in difficulty_levels:
            difficulty = (
                input(
                    f"Enter quiz difficulty ({', '.join(difficulty_levels)}): "
                )
                .strip()
                .lower()
            )
            if difficulty not in difficulty_levels:
                print(
                    "Invalid difficulty. Please choose from 'medium', 'hard', or 'phd-level'."
                )

        num_questions = 10
        print(f"\nGenerating {num_questions} {difficulty} level quiz...\n")
        quiz_output = await generate_quiz(
            document_text, difficulty, num_questions
        )
        print(quiz_output)

if __name__ == "__main__":
    asyncio.run(run_cli())
