import React from "react";
import { Card, Button } from "react-bootstrap";
import "../styles/IndexPage.css"; // ✅ Ensure styles are loaded

function CustomCard({ image, title, text, link, buttonText, className }) {
  return (
    <Card className={`h-100 text-center shadow-sm ${className}`}>
      <Card.Img
        variant="top"
        src={image}
        alt={title}
        className="index-card-img"
      />
      <Card.Body className="index-card-body">
        <Card.Title className="index-card-title">{title}</Card.Title>
        <Card.Text>{text}</Card.Text>
        <Button href={link} variant="primary">
          {buttonText}
        </Button>
      </Card.Body>
    </Card>
  );
}

export default CustomCard;
