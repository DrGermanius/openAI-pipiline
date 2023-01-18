import os
import urllib.request
import uuid
import openai


def download_image(url):
    path = "./generated/images/{name}.jpg"
    urllib.request.urlretrieve(url, path.format(name=str(uuid.uuid4())))


def generate_image_prompt():
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt="generate description of the person. Describe "
        #        "in details the face, hair, body, eyes, clothes, eye {}",
        prompt="generate wide description of appearance of media person's face",
        temperature=0.99,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["{}"]
    )
    return response.choices[0].text.strip()


def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    image_prompt = generate_image_prompt()
    print(image_prompt)

    image_url = generate_image(image_prompt)
    download_image(image_url)


if __name__ == '__main__':
    main()
