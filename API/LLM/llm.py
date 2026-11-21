import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class LLM:
    def __init__(self):
        local_dir = "LLM/Model"
        self.model = AutoModelForCausalLM.from_pretrained(local_dir)
        self.tokenizer = AutoTokenizer.from_pretrained(local_dir)
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.model.to(self.device)

    def generate(self, prompt):
        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        generated_ids = self.model.generate(**model_inputs, max_new_tokens=32768)
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

        if 151668 in output_ids:
            index = len(output_ids) - output_ids[::-1].index(151668)
            thinking_content = self.tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
            content = self.tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
        else:
            thinking_content = ""
            content = self.tokenizer.decode(output_ids, skip_special_tokens=True).strip("\n")
        return {"thinking_content": thinking_content, "content": content}