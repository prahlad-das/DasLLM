import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(device)

local_dir = "./Model"

tokenizer = AutoTokenizer.from_pretrained(local_dir)
model = AutoModelForCausalLM.from_pretrained(local_dir)

prompt = "How much is two thousand forty added to five thousand"

messages = [{"role": "user", "content": prompt}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(**model_inputs, max_new_tokens=32768)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

index = len(output_ids) - output_ids[::-1].index(151668)
thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("Thinking Content: \n", thinking_content)
print("______________________________________________")
print("Content:\n", content)


# RESULT

# Thinking Content: 
#  <think>
# Okay, so I need to figure out how much two thousand forty is added to five thousand. Let me start by breaking down the numbers. 

# First, two thousand forty. That's 2,040, right? Because "two thousand" is 2,000 and then "forty" is 40, so adding those together gives 2,000 + 40 = 2,040. 

# Then, five thousand is straightforward, that's 5,000. So the problem is asking for 2,040 plus 5,000. 

# Let me write that out as an equation: 2,040 + 5,000. 

# Hmm, adding these two numbers. Let me think about how to add them. Since 5,000 is a whole number and 2,040 is also a whole number, I can just add the thousands and the hundreds, tens, and ones separately. 

# Starting with the thousands place: 5,000 has 5 thousands, and 2,040 has 2 thousands. So 5 + 2 = 7 thousands. Then the hundreds place: 5,000 has 0 hundreds, and 2,040 has 0 hundreds as well. So 0 + 0 = 0 hundreds. 

# Next, the tens place: 5,000 has 0 tens, and 2,040 has 4 tens. So 0 + 4 = 4 tens. 

# Finally, the ones place: 5,000 has 0 ones, and 2,040 has 0 ones. So 0 + 0 = 0 ones. 

# Putting it all together: 7 thousands, 0 hundreds, 4 tens, and 0 ones. That would be 7,040. 

# Wait, let me check that again. If I have 5,000 + 2,040, maybe I can add them step by step. 

# 5,000 plus 2,000 is 7,000. Then, adding the remaining 40 to that. So 7,000 + 40 = 7,040. Yes, that matches. 

# Alternatively, I can think of 2,040 as 2,000 + 40. So adding 5,000 + 2,000 is 7,000, and then adding 40 gives 7,040. 

# Another way to check is to write both numbers vertically:

#   5,000
# + 2,040
# --------
#   7,040

# Adding the digits in each column:

# Starting from the rightmost digit (ones place): 0 + 0 = 0.

# Tens place: 0 + 4 = 4.

# Hundreds place: 0 + 0 = 0.

# Thousands place: 5 + 2 = 7.

# So the result is 7,040. 

# I think that's correct. Let me see if there's another way to approach this. Maybe converting them to words and then adding. 

# Five thousand is 5,000. Two thousand forty is 2,040. So adding 5,000 and 2,040. If I think of 5,000 + 2,000 = 7,000, and then 7,000 + 40 = 7,040. Yep, same answer. 

# I don't think I made any mistakes here. The key is to make sure that when adding the numbers, the place values are aligned correctly. Since 2,040 is two thousand and forty, which is 2,000 + 40, and adding that to five thousand (5,000) is straightforward. 

# Alternatively, if I convert both numbers to words and then add them. Five thousand plus two thousand forty. Five thousand plus two thousand is seven thousand, and then plus forty is seven thousand forty. Which is 7,040. 

# So all methods lead to the same answer. I think that's solid. I don't see any errors in my reasoning. The answer should be 7,040.
# </think>
# ______________________________________________
# Content:
#  To solve the problem of adding **two thousand forty** to **five thousand**, we begin by expressing both numbers in numerical form:

# - **Two thousand forty** is written as **2,040**.
# - **Five thousand** is written as **5,000**.

# Now, we perform the addition:

# $$
# 2,040 + 5,000
# $$

# We can break this down by place value:

# - **Thousands place**: $5,000 + 2,000 = 7,000$
# - **Tens place**: $0 + 40 = 40$

# Adding these together:

# $$
# 7,000 + 40 = 7,040
# $$

# Alternatively, we can add the numbers directly:

# $$
# \begin{array}{r}
#   5,000 \\
# + 2,040 \\
# \hline
#   7,040 \\
# \end{array}
# $$

# Thus, the final result is:

# $$
# \boxed{7040}
# $$

