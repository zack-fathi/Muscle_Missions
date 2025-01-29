import React, { useState } from "react";
import { Container, InputGroup, FormControl, Button } from "react-bootstrap";
import Layout from "../components/Layout";
import "../styles/LiftBot.css"; // Import external CSS

function LiftBot() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  const handleSendMessage = () => {
    if (!userInput.trim()) return;
  
    const userMessage = { text: userInput, sender: "user" };
    const botResponse = {
      text: `You said: "${userInput}". How can I assist further?`,
      sender: "bot",
    };
  
    // Update the messages array once with both messages
    setMessages((prevMessages) => [...prevMessages, userMessage, botResponse]);
    setUserInput("");
  };
  

  return (
    <Layout>
      <Container className="liftbot-container">
        <h2 className="text-center mb-4">Ask LiftBot Anything</h2>

        <div id="chat-area">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${
                message.sender === "user" ? "user-message" : "bot-message"
              }`}
            >
              {message.text}
            </div>
          ))}
        </div>

        <InputGroup className="mb-3">
          <FormControl
            placeholder="Ask me anything about fitness..."
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
          />
          <Button variant="primary" onClick={handleSendMessage}>
            Send
          </Button>
        </InputGroup>
      </Container>
    </Layout>
  );
}

export default LiftBot;
