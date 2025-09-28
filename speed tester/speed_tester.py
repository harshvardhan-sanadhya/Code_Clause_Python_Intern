import random
import time
def word_count(x):
    words=x.split()
    count=len(words)
    return count

def WPM(words,time_taken):
    wpm=(words/time_taken)*60
    return wpm

def accuracy_measure(input_text,actual_text):
    input_text=input_text.split()
    actual_text=actual_text.split()
    correct=0
    for i in range(min(len(input_text),len(actual_text))):
        if input_text[i]==actual_text[i]:
            correct+=1
    accuracy = (correct / len(actual_text)) * 100
    return accuracy
# the random sentances for the test
sentences = [
    "Artificial intelligence is changing many industries by automating routine tasks and helping professionals make better decisions. As tools get smarter, people must focus on learning new skills and adapting quickly. Typing well is a practical skill that saves time and improves productivity across many jobs and study routines.",
    "Effective communication requires clear thinking and precise words. Writing short, well-structured paragraphs helps readers understand complex ideas faster. Typing practice that uses natural punctuation and varied vocabulary prepares you for real-world writing tasks like reports, emails, and documentation where clarity really matters.",
    "Technology connects people across the world and makes collaboration simple. Remote teams rely on fast, accurate typing during chats, shared documents, and issue trackers. Building speed without sacrificing accuracy makes you a more reliable teammate and helps reduce misunderstandings in fast-paced working environments.",
    "Reading widely expands vocabulary and mental models, while typing practice helps turn those words into action. When you type long passages regularly, muscle memory improves and fewer errors occur. This combination of knowledge and mechanical skill makes everyday tasks like coding, writing, and data entry significantly more efficient.",
    "Time management is a crucial skill in any career. Practicing typing in timed sessions trains your focus and teaches you to work under brief, concentrated pressure. Short, frequent sessions that mimic real deadlines will help you develop consistency and the habit of delivering quality work on schedule.",
    "When you type, punctuation and capitalization matter as much as speed. Including commas, parentheses, and dashes in practice paragraphs helps you learn to place them naturally. This reduces the need for later editing and produces cleaner text right away—valuable for reports, messages, and any formal communication.",
    "Learning new technologies requires patience and a willingness to experiment. Small daily improvements add up: five minutes of focused typing practice every day strengthens both speed and accuracy. Over weeks, you will notice fewer mistakes and greater confidence when composing longer, technical documents.",
    "Writing for different audiences requires adjusting tone, length, and word choice. Practice paragraphs that mix formal and conversational language help you switch styles quickly. This flexibility matters when crafting emails to managers, help guides for customers, or informal updates for teammates.",
    "Good documentation reduces support requests and miscommunication. Typing clear, concise guides and examples benefits everyone who reads them. Training yourself to produce accurate, readable paragraphs under time pressure makes it easier to maintain quality documentation even when deadlines are tight.",
    "Creativity often appears under constraints: a short time limit can spark focus and fresh ideas. Typing timed passages encourages you to prioritize essential words and construct stronger sentences. Over time, this habit helps you write more efficiently without losing the meaning and tone you want to convey.",
    "A balanced typing practice includes varied vocabulary and sentence length. Long sentences teach rhythm and flow; short sentences teach clarity. Mixing both kinds in timed sessions helps you develop overall writing control and reduces the tendency to produce repetitive or flat prose.",
    "When preparing for technical interviews or collaborative coding, clear typed communication makes a strong impression. Fast, accurate typing allows you to document solutions, write meaningful commit messages, and explain designs quickly. Employers notice candidates who communicate their thoughts clearly and efficiently in written form.",
    "Learning to type faster also supports learning to think faster. As your fingers keep pace with your thoughts, you can capture ideas in real time without losing momentum. This flow state helps with brainstorming, drafting essays, and quickly composing emails when inspiration strikes.",
    "Practical skills are best learned by doing. Typing long, meaningful passages simulates actual work better than isolated words or short phrases. When practice material relates to your field—technical explanations, business summaries, or creative descriptions—you get double value from both typing and subject practice.",
    "Regular feedback helps improvement: track both speed and accuracy to see true progress. If speed increases but accuracy drops, focus on controlled practice. If accuracy improves but speed stalls, gradually reduce time limits. Balanced training yields steady gains that show in daily tasks and project work.",
    "Typing involves posture, ergonomics, and timing. Good posture and short breaks reduce fatigue and maintain precision during longer sessions. Practicing in a comfortable setup encourages longer, more effective practice sessions without physical strain, leading to more sustainable performance improvements.",
    "Collaboration tools such as issue trackers and shared documents benefit from concise, accurate writing. Typing practice that includes lists, bullet-style sentences, and short explanatory paragraphs prepares you for maintaining clear project notes and status updates that teammates can read quickly and act on.",
    "In many roles, writing is documentation of thought. Clear, typed paragraphs function as a record others can follow. Practicing with realistic content increases the likelihood that your written notes will be useful, searchable, and reusable months later when projects evolve or people change roles.",
    "Speed alone is not the goal: measured, accurate typing is more valuable. Training sessions that reward accuracy first and speed second produce robust improvement. Aim for steady reductions in errors before pushing for faster WPM, and you’ll build a reliable, professional skillset.",
    "Typing under short time limits simulates deadlines and real-world pressure. Use practice paragraphs that include technical terms, punctuation, and compound sentences to create realistic exercises. Over time, this approach will help you maintain clarity and composure even when working on tight schedules."
]

# input aria for user
actual=random.choice(sentences)
print(actual)

start_time=time.time() #start time
input_text=input("Enter your Anser Here: \n")
end_time=time.time() #end time
elapsed=end_time - start_time
print(" ")
print("Results")
print("Total time taken: ",round(elapsed,2))

count=word_count(input_text)
print("Total word typed: ",count)

wpm=WPM(count,elapsed)
print("Word Per Minute: ",round(wpm,2))

acc_score=accuracy_measure(input_text,actual)
print("Accuracy Score: ",round(acc_score,2),"%")


