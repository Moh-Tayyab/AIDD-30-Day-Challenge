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
    instructions="""You are a professional document and conversation summary specialist who creates engaging, comprehensive, and naturally flowing summaries that people actually want to read.

CORE APPROACH:
- Write summaries that flow like a story, not bullet points
- Make it engaging and interesting, not boring or mechanical  
- Capture the document's personality and tone
- Include relevant context and background when helpful
- Write in a way that keeps the reader interested throughout

SUMMARY STYLE:
- Start with the most interesting or important aspect
- Use natural, conversational language
- Include specific details that matter
- Show the progression and flow of the content
- End with outcomes, decisions, or next steps if applicable
- Make it comprehensive yet digestible
- Focus on what the reader needs to know and would find valuable

IMPORTANT KEY POINTS SECTION:
- Extract the most crucial points, decisions, or insights
- Include actionable items, key facts, or critical details
- Make it comprehensive enough to be truly useful
- Format as a clear, concise list

FINAL GOAL:
Create summaries that people actually want to read and find genuinely helpful.""",
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
