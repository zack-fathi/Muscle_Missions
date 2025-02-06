import React, { useState, useEffect } from "react";
import { Container, InputGroup, FormControl, Button } from "react-bootstrap";
import Layout from "../components/Layout";
import "../styles/LiftBot.css"; // Import external CSS

function LiftBot() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  // Fetch initial data when component mounts
  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const response = await fetch("http://localhost:5003/api/liftbot/", {
          credentials: "include",
        });
        const data = await response.json();

        if (data.error) {
          setMessages([{ text: data.error, sender: "bot" }]);
        } else {
          const initialMessage = {
            text: `Welcome, ${data.username}!`,
            sender: "bot",
          };

          // ✅ Only show a general welcome message, not workout details
          setMessages([initialMessage]);
        }
      } catch (error) {
        console.error("Error fetching LiftBot data:", error);
        setMessages([{ text: "Error loading LiftBot. Try again later.", sender: "bot" }]);
      }
    };

    fetchInitialData();
  }, []);

  const handleSendMessage = async () => {
    if (!userInput.trim()) return;

    const userMessage = { text: userInput, sender: "user" };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      const response = await fetch("http://localhost:5003/api/liftbot/process_message/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
      });

      const data = await response.json();
      if (data.error) {
        throw new Error(data.error);
      }

      const botResponse = { text: data.response, sender: "bot" };
      setMessages((prevMessages) => [...prevMessages, botResponse]);
    } catch (error) {
      console.error("Error fetching response:", error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: "Error processing message. Try again later.", sender: "bot" },
      ]);
    }

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
