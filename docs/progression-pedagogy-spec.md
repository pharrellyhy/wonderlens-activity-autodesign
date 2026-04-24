# Comprehensive Progression Pedagogy & Mechanics Specification

**Document Purpose:** 
This specification maps the Wonderlens AI Progression Engine mechanics to the official early childhood education (ECE) guidelines of three major frameworks:
1. **Colorado Early Learning and Development Guidelines (USA)** - 187 pages
2. **Development Matters: EYFS Statutory Framework (UK)** - 128 pages
3. **Ministry of Education 3-6 Year Old Learning Guidelines (China)** - 44 pages

**Agent Instructions:** 
When generating Python state-transition logic, system prompts, or conversational agent dialogue, use the "System Action" and "Pedagogical Evidence" below to ensure the AI's decision-making adheres strictly to global ECE consensus.

---

## 1. Core Architecture: Per-Axis State vs. Global Level
The runtime tracks 7 independent cognitive axes (e.g., Form, Function, Causation) per child, rather than a single global "XP level." 

* **Engine Trigger:** Child completes a session. State updates are written to `topic_axis` specific objects.
* **System Action:** A child can be served a Level 3 (L3) activity in *Form* and a Level 1 (L1) activity in *Causation* on the same day. The system must not average these out.
* **Pedagogical Evidence:**
    * **US (Colorado, p. 8 & 23):** "The development of children unfolds along individual pathways whose trajectories are characterized by continuities and discontinuities... Infants and toddlers will grow and develop particular skills at their own unique pace."
    * **UK (EYFS, p. 9):** "Babies and young children do not develop in a fixed way. Their development is like a spider’s web with many strands, not a straight line."
    * **China (MoE, p. 5):** "每个幼儿在沿着相似进程发展的过程中，各自的发展速度和到达某一水平的时间不完全相同... 切忌用一把“尺子”衡量所有幼儿。" *(Each child's speed of development and time to reach a certain level are not the same... Never use a single "ruler" to measure all children.)*

---

## 2. The Soft-Reframe (The "Gentle Nudge" & Wait Time)
Used when a child is engaged but struggling to find the precise answer, or requires more time to process.

* **Engine Trigger:** `silence > 6s` after a correct response, or a `mixed / slow but on-topic` response. 
* **System Action:** Maintain the current difficulty Rung. Do not demote. Output a gentler prompt, utilize wait time, and provide scaffolding (e.g., multiple-choice or hints).
* **Pedagogical Evidence:**
    * **US (Colorado, p. 124 & 121):** "Vary 'wait time,' or the amount of time children are allowed to respond." ... "Assist a frustrated child by providing just enough help (e.g., 'You are working so hard on that puzzle! Would that piece fit if you turned it a little bit?')."
    * **UK (EYFS, p. 17 & 29):** "Help children to think about what will support them most, taking care not to offer help too soon... When talking with young children, give them plenty of processing time (at least 10 seconds). This gives them time to understand what you have said and think of their reply."
    * **China (MoE, p. 14):** "当幼儿因为急于表达而说不清楚的时候，提醒他不要着急，慢慢说；同时要耐心倾听，给予必要的补充，帮助他理清思路..." *(When a child cannot speak clearly because they are anxious, remind them not to rush; listen patiently and provide necessary supplements to help them clarify their thoughts.)*

---

## 3. Demote & Dignity Reframe (Pivot to Modeling)
Used when the current cognitive load is too high, causing repeated failure or frustration. 

* **Engine Trigger:** `2 failed attempts` (silence > 6s, completely off-topic, or repeats prompt).
* **System Action:** Silently decrement the difficulty Rung (L_current - 1). The AI script agent MUST NOT use phrases like "Let's try again," "That's wrong," or "No." Instead, use the `Dignity Reframe` flag to pivot to observational modeling (e.g., *"Let me show you what I notice first"*).
* **Pedagogical Evidence:**
    * **US (Colorado, p. 128 & 136):** "Talk through different approaches to problems and value children’s thinking regardless of accuracy." ... "Create an environment where children feel supported and can take risks (i.e., they aren't afraid to try and fail)."
    * **UK (EYFS, p. 27 & 57):** "Instead of correcting them, reply to what they say and use the words they have mispronounced. Children will then learn from your positive model, without losing the confidence to speak." ... "Show that mistakes are an important part of learning and going back is trial and error not failure."
    * **China (MoE, p. 44 & 15):** "肯定幼儿作品的优点，用表达自己感受的方式引导其提高。" *(Affirm the merits of the child's work, and guide their improvement by expressing your own feelings/observations.)* ... "即使做得不够好，也应鼓励并给予一定的指导，让他在做事中树立自尊和自信。" *(Even if they don't do it well enough, encourage and provide guidance, allowing them to build self-esteem and confidence.)*

---

## 4. The Hold (Expected Pacing & Consolidation)
Used when a child succeeds at the current difficulty, but requires repetition to solidify the concept before moving to a harder level.

* **Engine Trigger:** `1 clean-correct round`.
* **System Action:** Log the success. Keep the state at the current Rung for the next activity. Do not rush to escalate difficulty; prioritize deep comprehension.
* **Pedagogical Evidence:**
    * **US (Colorado, p. 124):** "Involve children in sustained conversations, pursuing their interests with questions and comments... Ask open-ended questions that require more than a 'yes' or 'no' response."
    * **UK (EYFS, p. 4 & 16):** "Depth in learning matters much more than moving from one band to the next or trying to cover everything. There is no value in rushing..." ... "Help young children to develop by accepting the pace of their learning. Give them plenty of time to make connections and repeat activities."
    * **China (MoE, p. 37):** "结合具体事物让幼儿通过多次比较逐渐理解..." *(Help children gradually understand through multiple comparisons combining concrete objects...)*

---

## 5. Promote & Sibling-Axis Jump (The Spontaneous Leap)
Used when a child masters a level, or spontaneously demonstrates understanding of a higher-order concept unprompted.

* **Engine Trigger:** `3 consecutive same-axis successes` OR a `spontaneous_l_plus_1` response. If ceiling (L3) is hit, trigger `Sibling-axis jump`.
* **System Action:** Increment the difficulty Rung (L_current + 1). If at L3, pivot the next activity to L1 of a conceptually related sibling axis (e.g., from *Function* L3 to *Systems/Connection* L1). This preserves novelty while expanding the child's worldview laterally.
* **Pedagogical Evidence:**
    * **US (Colorado, p. 135 & 121):** "Change plans if children initiate a more interesting idea or experience." ... "Ask children to generate ideas and try them out..."
    * **UK (EYFS, p. 15 & 19):** "Extend children’s interests by providing stimulating resources for them to play with... in response to their fascinations." ... "Help children to extend their ideas through sustained discussion that goes beyond what they, and you, have noticed. Consider ‘how’ and ‘why’ things happen."
    * **China (MoE, p. 31 & 23):** "支持和鼓励幼儿大胆联想、猜测问题的答案，并设法验证。" *(Support and encourage children to make bold associations, guess the answers to problems, and try to verify them.)* ... "鼓励幼儿尝试有一定难度的任务，并注意调整难度，让他感受经过努力获得的成就感。" *(Encourage children to attempt tasks with a certain degree of difficulty, paying attention to adjusting the difficulty so they can feel a sense of achievement through effort.)*

---

## Developer Notes for Coding Agent
1. **Wait Time Execution:** In Voice/Audio integrations, standard silence detection thresholds (e.g., 2 seconds) MUST be overridden. Global ECE standards explicitly require 6-10 seconds of processing time for toddlers/preschoolers before triggering a "No Response" or "Soft-Reframe" action.
2. **Implicit Correction:** When writing AI Dialogue generation prompts, explicitly ban the phrases "No," "That's incorrect," or "Try again." Inject system instructions to utilize **Implicit Correction via Modeling** (e.g., User: "I runned fast." AI: "Wow, you ran so fast!").
3. **Lateral Jumps:** Implement the `Sibling-Axis Jump` table as a distinct logic branch. Hitting a ceiling (L3) should never result in a repetitive loop; the AI must immediately transition to the adjacent IB Key Concept. 
