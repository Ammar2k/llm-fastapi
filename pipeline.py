# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
# Use a pipeline as a high-level helper
from transformers import pipeline


# tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-0.5B")
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen1.5-0.5B")

prompt = "tell me about the charter of democracy in Pakistani politics."

# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": prompt}
# ]

# text = tokenizer.apply_chat_template(
#     messages,
#     tokenize=False,
#     add_generation_prompt=True
# )

# model_inputs = tokenizer([text], return_tensors="pt")

# generated_ids = model.generate(
#     model_inputs.input_ids,
#     max_new_tokens=512
# )

# generated_ids = [
#     output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
# ]

# response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
# print(response)

pipe = pipeline("text-generation", model="Qwen/Qwen1.5-0.5B")

answer = pipe(prompt)
print(answer)
