import React from "react";
import { Card, Button } from "react-bootstrap";

function CustomCard({ image, title, text, link, buttonText }) {
  return (
    <Card className="h-100 text-center shadow-sm" style={{ borderRadius: "15px" }}>
      <Card.Img
        variant="top"
        src={image}
        alt={title}
        style={{
          height: "200px",
          objectFit: "cover",
          borderTopLeftRadius: "15px",
          borderTopRightRadius: "15px",
        }}
      />
      <Card.Body>
        <Card.Title style={{ fontWeight: "700", fontSize: "1.25rem" }}>{title}</Card.Title>
        <Card.Text style={{ fontSize: "1rem", margin: "1rem 0" }}>{text}</Card.Text>
        <Button href={link} variant="outline-primary">
          {buttonText}
        </Button>
      </Card.Body>
    </Card>
  );
}

export default CustomCard;