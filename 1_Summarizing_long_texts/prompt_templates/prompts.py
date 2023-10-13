map_prompt = """
The following is a part of a speech
{text_chunk}
Based on this particular part of the speech, please write a concise summary
Helpful Answer:
"""

reduce_prompt = """The following is set of summaries:
{text_summaries}
Take these and combine them into a final, consolidated summary of the full speech.
Helpful Answer:
"""
