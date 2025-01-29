import React from "react";
import { Container } from "react-bootstrap";

function Footer() {
  return (
    <footer className="bg-dark text-white text-center py-3 mt-4">
      <Container>
        <p className="mb-0">
          © {new Date().getFullYear()} Muscle Missions. All rights reserved.
        </p>
      </Container>
    </footer>
  );
}

export default Footer;
