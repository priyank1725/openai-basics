# OpenAI Basics - AI/ML Learning Project

A comprehensive collection of Python scripts demonstrating various AI/ML concepts using Google's Gemini API, LangChain, and other modern AI tools.

## 🚀 Quick Start

### Prerequisites
- Python 3.13 or higher
- Poetry (for dependency management)
- Google Gemini API key

### Setup
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd openai-basics
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

## 📁 Project Structure

### Core AI Scripts

#### 1. **main.py** - Basic Gemini API Usage
- **Purpose**: Simple demonstration of Google Gemini API integration
- **Features**: Command-line prompt input, basic text generation
- **Run**: `python main.py "Your prompt here"`
- **Example**: `python main.py "Explain quantum computing in simple terms"`

#### 2. **chatbot.py** - Interactive Chatbot
- **Purpose**: Conversational AI chatbot with memory
- **Features**: Conversation history, LangChain integration, interactive chat loop
- **Run**: `python chatbot.py`
- **Usage**: Type your messages, type 'exit' or 'quit' to end

#### 3. **embeddings.py** - Text Embeddings & Similarity
- **Purpose**: Demonstrates text embeddings and cosine similarity
- **Features**: Sentence embeddings, similarity comparison, numpy operations
- **Run**: `python embeddings.py`
- **Output**: Shows similarity scores between different sentences

#### 4. **hybrid_embeddings.py** - Advanced Embeddings
- **Purpose**: Combines AI embeddings with custom features
- **Features**: Hybrid vectors, sentiment analysis, custom metrics
- **Run**: `python hybrid_embeddings.py`
- **Output**: Enhanced similarity analysis with custom features

#### 5. **rag_text.py** - Retrieval-Augmented Generation
- **Purpose**: RAG system for question-answering over documents
- **Features**: Document loading, text chunking, vector storage, QA chain
- **Run**: `python rag_text.py`
- **Usage**: Ask questions about the content in `data.txt`
- **Dependencies**: Requires `data.txt` file

#### 6. **multimodal_rag.py** - Image + Text Analysis
- **Purpose**: Multimodal AI that can analyze images and answer questions
- **Features**: Image processing, base64 encoding, vision-language model
- **Run**: `python multimodal_rag.py`
- **Requirements**: Needs `receipt.jpg` image file
- **Output**: Answers questions about image content

#### 7. **structured_output.py** - JSON Generation
- **Purpose**: Forces AI to generate structured JSON output
- **Features**: JSON parsing, structured prompts, error handling
- **Run**: `python structured_output.py`
- **Output**: Parsed JSON from AI response

#### 8. **agent_calculator.py** - AI Agent with Tools
- **Purpose**: Demonstrates AI agents with custom tools
- **Features**: Calculator tool, agent initialization, tool chaining
- **Run**: `python agent_calculator.py`
- **Output**: AI agent responses using available tools

### Data Files

#### 9. **data.txt** - Sample Text Data
- **Content**: Information about Mahatma Gandhi
- **Purpose**: Used by RAG systems for question-answering
- **Usage**: Referenced by `rag_text.py`

#### 10. **receipt.jpg** - Sample Image
- **Purpose**: Used by multimodal RAG system
- **Usage**: Referenced by `multimodal_rag.py`

### Configuration Files

#### 11. **pyproject.toml** - Project Configuration
- **Dependencies**: All required Python packages
- **Python Version**: 3.13+
- **Build System**: Poetry

#### 12. **poetry.lock** - Dependency Lock File
- **Purpose**: Ensures reproducible builds
- **Usage**: Automatically managed by Poetry

## 🔧 Dependencies

The project uses the following key libraries:
- **openai**: Google Gemini API client
- **langchain**: AI application framework
- **langchain-google-genai**: Google Gemini integration for LangChain
- **chromadb**: Vector database for embeddings
- **numpy**: Numerical computing
- **pillow**: Image processing
- **textblob**: Text processing and sentiment analysis
- **tiktoken**: Token counting
- **python-dotenv**: Environment variable management

## 🎯 Use Cases & Learning Path

### Beginner Level
1. Start with `main.py` to understand basic API usage
2. Try `chatbot.py` for interactive AI conversations
3. Explore `embeddings.py` for text similarity concepts

### Intermediate Level
1. Study `hybrid_embeddings.py` for advanced embedding techniques
2. Learn RAG with `rag_text.py`
3. Experiment with `structured_output.py` for data extraction

### Advanced Level
1. Dive into `multimodal_rag.py` for vision-language AI
2. Explore `agent_calculator.py` for AI agent development
3. Customize and extend the existing implementations

## 🚨 Important Notes

- **API Key**: Always keep your Google API key secure in `.env` file
- **Rate Limits**: Be aware of Google Gemini API rate limits
- **Python Version**: Requires Python 3.13+ due to modern dependency requirements
- **Image Files**: Some scripts require specific image files (e.g., `receipt.jpg`)

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're in the Poetry virtual environment
2. **API Key Errors**: Check your `.env` file and API key validity
3. **Missing Files**: Ensure `data.txt` and `receipt.jpg` exist for RAG scripts
4. **Python Version**: Verify you're using Python 3.13+

### Getting Help

- Check that all dependencies are installed: `poetry install`
- Verify your API key is working with a simple test
- Ensure you're running scripts from the project root directory

## 🎓 Learning Resources

This project demonstrates:
- **API Integration**: Working with Google's Gemini API
- **LangChain**: Building AI applications with LangChain framework
- **Embeddings**: Text vectorization and similarity
- **RAG Systems**: Retrieval-augmented generation
- **Multimodal AI**: Combining text and image analysis
- **AI Agents**: Creating AI agents with tools
- **Structured Output**: Generating and parsing structured data

## 📝 License

This project is for educational purposes. Please respect the terms of service for all APIs used.

## 🤝 Contributing

Feel free to extend this project with:
- Additional AI models and APIs
- New use cases and examples
- Improved documentation
- Bug fixes and optimizations
