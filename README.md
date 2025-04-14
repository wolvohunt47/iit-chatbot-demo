# IIT(ISM) Dhanbad Chatbot

A smart AI-powered chatbot for IIT(ISM) Dhanbad website, built with Flask and OpenAI's GPT. This chatbot provides information about admissions, courses, departments, faculty, campus facilities, and other college-related topics.

## Features

- 🤖 AI-powered responses using OpenAI's GPT model
- 💬 Interactive chat interface with typing indicators
- 📱 Responsive design for desktop and mobile
- 🚀 Easy to deploy and integrate with existing websites
- 🎓 Specifically tuned for IIT(ISM) Dhanbad related queries

## Demo

[Add screenshots or GIF of your application here]

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- An OpenAI API key

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/iit-ism-chatbot.git
   cd iit-ism-chatbot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`

## Customization

### Modifying the System Prompt

To update the information provided by the chatbot, edit the `system_prompt` variable in `app.py`.

### Updating the UI

The UI can be customized by modifying the files in the `templates` and `static` directories.

## Deployment

### Deploying to Heroku

1. Create a Heroku account if you don't have one: [https://signup.heroku.com/](https://signup.heroku.com/)

2. Install the Heroku CLI: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

3. Login to Heroku from the terminal:

   ```bash
   heroku login
   ```

4. Create a new Heroku app:

   ```bash
   heroku create your-app-name
   ```

5. Add your OpenAI API key to Heroku config variables:

   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_api_key_here
   ```

6. Push your code to Heroku:

   ```bash
   git push heroku main
   ```

7. Open your app in the browser:

   ```bash
   heroku open
   ```

### Deploying to Other Platforms

This application can be deployed to any platform that supports Python applications, such as AWS, Google Cloud, or Azure.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenAI for providing the GPT API
- Flask framework
- IIT(ISM) Dhanbad for inspiration