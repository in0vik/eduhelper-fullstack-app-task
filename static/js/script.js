document.addEventListener('DOMContentLoaded', () => {
  // DOM elements
  const questionForm = document.getElementById('question-form');
  const questionInput = document.getElementById('question-input');
  const askButton = document.getElementById('ask-button');
  const loading = document.getElementById('loading');
  const answerContainer = document.getElementById('answer-container');
  const answerContent = document.getElementById('answer-content');
  const saveButton = document.getElementById('save-button');
  const errorMessage = document.getElementById('error-message');

  // CSRF token for Django
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')
    ? document.querySelector('[name=csrfmiddlewaretoken]').value
    : '';

  const debugMode = false; 
  let sampleData = [];

  function generatePlaceholderAnswer(question) {
    return `This is a placeholder for your question: "${question}"`;
  }

  
  let currentQuestion = '';
  let currentAnswer = '';

  // Handle form submit
  questionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();
    if (!question) {
      showError('Please enter a question.');
      return;
    }
    currentQuestion = question;
    askQuestion(question);
  });

  // Send question to the server
  async function askQuestion(question) {
    loading.classList.remove('hidden');
    answerContainer.classList.add('hidden');
    errorMessage.classList.add('hidden');
    askButton.disabled = true;

    try {
      const placeholder = generatePlaceholderAnswer(question);
      currentAnswer = placeholder;

      // const response = await fetch('/ask/', {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //     'X-CSRFToken': csrfToken
      //   },
      //   body: JSON.stringify({ question })
      // });
      // const data = await response.json();

      // if (!response.ok) {
      //   throw new Error(data.error || 'Failed to retrieve the answer.');
      // }
      // currentAnswer = data.answer;
      displayAnswer(currentAnswer);

    } catch (error) {
      showError(error.message);
    } finally {
      loading.classList.add('hidden');
      askButton.disabled = false;
    }
  }

  // Display the answer
  function displayAnswer(answer) {
    answerContent.textContent = answer;
    answerContainer.classList.remove('hidden');
  }

  // Handle "Save" button
  saveButton.addEventListener('click', () => {
    if (currentQuestion && currentAnswer) {
      saveAnswer(currentQuestion, currentAnswer);
    }
  });

  // Save question & answer to the database
  async function saveAnswer(question, answer) {
    saveButton.disabled = true;
    try {
      const response = await fetch('/save/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ question, answer })
      });
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Error saving the answer.');
      }
      // Reload to see the new answer in the list
      window.location.reload();
    } catch (error) {
      showError(error.message);
      saveButton.disabled = false;
    }
  }

  // Show an error message
  function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
  }

  function unusedDebugFunction() {
    console.log("I'm never used!");
  }
});
