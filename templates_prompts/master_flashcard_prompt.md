# Master Flashcard Generation Prompt

Create exactly 20 high-quality flashcards from the provided research paper using this TSV format:

```
Front	Back	Context
```

## Coverage Requirements
Include 4-5 cards each for:
- Key findings and conclusions
- Methods and experimental design  
- Important definitions and terminology
- Statistical results and data
- Limitations and implications

## Question Quality Standards
- Use specific, testable questions with quantitative details
- Avoid vague terms like "What is..." or "Describe..."
- Include study specifics (sample sizes, timeframes, measurements)
- Test understanding and application, not just recall
- Use question stems like: "According to [Author, Year], what was the correlation between..." or "In the study of [N] participants, how did..."

## Answer Quality Standards
- Provide complete, precise answers with specific numbers and percentages
- Include effect sizes, significance levels, and sample sizes when available
- Use the paper's exact terminology and definitions
- Keep answers concise but comprehensive enough to stand alone

## Context Field Requirements
The context field must be detailed enough to serve as a substitute for reading the paper. Include:
- Extended background explaining why this finding matters
- Full methodological details that inform the result (study design, measures, controls)
- Complete definitions of all abbreviations and technical terms used
- Important caveats, limitations, or conditions that affect interpretation
- Connections to broader theoretical frameworks or related research mentioned

## Formatting Requirements
- Title format: "AuthorLastName, Year, abbreviated topic"
- Use single tabs between Front, Back, and Context fields
- No line breaks within individual fields
- Replace any internal tabs with spaces

## Quality Examples

**Good Question**: "In Smith et al.'s longitudinal study, what was the correlation between daily meditation minutes and cortisol reduction after 8 weeks (n=156)?"

**Good Answer**: "r = -.42, p < .001, indicating 18% of variance in cortisol reduction explained by meditation duration"

**Good Context**: "This finding comes from a randomized controlled trial where participants were randomly assigned to meditation or control groups. Cortisol was measured via saliva samples at baseline and 8 weeks. The moderate correlation suggests practical significance, but the authors note that individual differences in baseline stress levels may moderate this relationship. Cortisol reduction was measured as percentage change from baseline using validated immunoassay techniques."

Now create 20 flashcards following these guidelines for the attached research paper.