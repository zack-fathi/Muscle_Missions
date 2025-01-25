import React from "react";
import { Button, Container } from "react-bootstrap";

function HeroSection({ title, subtitle, buttonText, link, image }) {
  return (
    <div
      className="hero-section"
      style={{
        background: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${image}) no-repeat center center/cover`,
        color: "white",
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        padding: "20px",
      }}
    >
      <Container>
        <h1 style={{ fontSize: "3.5rem", fontWeight: "700", marginBottom: "1rem" }}>
          {title}
        </h1>
        <p style={{ fontSize: "1.25rem", marginBottom: "2rem" }}>{subtitle}</p>
        <Button href={link} variant="primary" size="lg">
          {buttonText}
        </Button>
      </Container>
    </div>
  );
}

export default HeroSection;