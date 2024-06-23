import openai
import time

# Set your OpenAI API key here
openai.api_key = '[API KEY]'

def process_prompt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the correct model name
            messages=[
                {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3700  # Adjust max_tokens as needed
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    input_file = 'input_prompts.txt'  # File containing prompts
    output_file = 'output_responses.txt'

    with open(input_file, 'r') as file:
        prompts = file.readlines()

    with open(output_file, 'w') as file:
        for i, prompt in enumerate(prompts, start=1):
            print(f"Processing prompt {i} of {len(prompts)}: {prompt.strip()}")
            response = process_prompt(prompt)
            print(response)
            file.write(f"Prompt: {prompt}\nResponse: {response}\n\n")
            if i < len(prompts):
                time.sleep(60)  # Wait for one minute

    print("All prompts have been processed.")

if __name__ == "__main__":
    main()
