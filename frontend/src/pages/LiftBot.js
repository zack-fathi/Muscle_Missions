import React, { useState, useEffect } from "react";
import {
  Container,
  FormControl,
  Button,
  Spinner,
  Alert,
} from "react-bootstrap";
import Layout from "../components/Layout";
import "../styles/LiftBot.css"; // Import external CSS
import { Helmet } from "react-helmet";

const authURL = process.env.REACT_APP_AUTH_URL;
const liftbotURL = process.env.REACT_APP_LIFTBOT_URL;

function LiftBot() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");
  
  // New states: loading check + login status
  const [loading, setLoading] = useState(true);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // 1. Check if user is logged in
  useEffect(() => {
    async function doCheck() {
      try {
        const res = await fetch(`${authURL}/auth/`, {
          credentials: "include",
        });
        if (res.ok) {
          const data = await res.json();
          setIsLoggedIn(data.logged_in);
        } else {
          setIsLoggedIn(false);
        }
      } catch (error) {
        console.error("Error checking auth:", error);
        setIsLoggedIn(false);
      } finally {
        setLoading(false);
      }
    }
    doCheck();
  }, []);

  // 2. If logged in, fetch initial data for LiftBot
  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const response = await fetch(`${liftbotURL}/`, {
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
          setMessages([initialMessage]);
        }
      } catch (error) {
        console.error("Error fetching LiftBot data:", error);
        setMessages([
          { text: "Error loading LiftBot. Try again later.", sender: "bot" },
        ]);
      }
    };

    // Only fetch if user is logged in
    if (isLoggedIn) {
      fetchInitialData();
    }
  }, [isLoggedIn]);

  const handleSendMessage = async () => {
    if (!userInput.trim()) return;

    const userMessage = { text: userInput, sender: "user" };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setUserInput(""); // Clear immediately

    try {
      // Show temporary “typing” spinner message
      const typingMessage = { text: "", sender: "bot", isTyping: true };
      setMessages((prevMessages) => [...prevMessages, typingMessage]);

      const response = await fetch(
        `${liftbotURL}/process_message/`,
        {
          method: "POST",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ message: userInput }),
        }
      );

      const data = await response.json();
      if (data.error) {
        throw new Error(data.error);
      }

      // Replace spinner with real bot response
      const botResponse = { text: data.response, sender: "bot" };
      setMessages((prevMessages) => {
        const newMessages = [...prevMessages];
        const typingIndex = newMessages.findIndex((msg) => msg.isTyping);
        if (typingIndex !== -1) {
          newMessages.splice(typingIndex, 1);
        }
        newMessages.push(botResponse);
        return newMessages;
      });
    } catch (error) {
      console.error("Error fetching response:", error);
      // Remove spinner, show error
      setMessages((prevMessages) => {
        const newMessages = [...prevMessages];
        const typingIndex = newMessages.findIndex((msg) => msg.isTyping);
        if (typingIndex !== -1) {
          newMessages.splice(typingIndex, 1);
        }
        newMessages.push({
          text: "Error processing message. Try again later.",
          sender: "bot",
        });
        return newMessages;
      });
    }
  };

  // 3. Rendering Logic
  return (
    <Layout>
      <Helmet>
        <title>LiftBot</title>
      </Helmet>
      <Container className="liftbot-container">
        {loading ? (
          // Show a spinner while checking auth
          <div className="text-center">
            <Spinner animation="border" role="status">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          </div>
        ) : !isLoggedIn ? (
          // Alert if NOT logged in
          <Alert variant="danger" className="text-center">
            You must be logged in to use LiftBot!
          </Alert>
        ) : (
          //  If logged in, show the chat UI
          <>
            <h2 className="text-center mb-4">Ask LiftBot Anything</h2>
            <div id="chat-area">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`message ${
                    message.sender === "user"
                      ? "user-message"
                      : "bot-message"
                  }`}
                >
                  {message.isTyping ? (
                    <Spinner animation="border" role="status" size="sm">
                      <span className="visually-hidden">Loading...</span>
                    </Spinner>
                  ) : (
                    message.text
                  )}
                </div>
              ))}
            </div>

            <div className="d-flex">
              <FormControl
                placeholder="Ask me anything about fitness..."
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
              />
              <Button variant="primary" onClick={handleSendMessage}>
                Send
              </Button>
            </div>
          </>
        )}
      </Container>
    </Layout>
  );
}

export default LiftBot;
