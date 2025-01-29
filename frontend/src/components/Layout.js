import React from "react";
import Footer from "./Footer";
import CustomNavbar from "./Navbar"; // Assuming you have a Navbar component
import { Container } from "react-bootstrap";

function Layout({ children }) {
  return (
    <div className="d-flex flex-column min-vh-100">
      {/* Navbar */}
      <CustomNavbar />

      {/* Main Content */}
      <Container className="flex-grow-1 mt-3">{children}</Container>

      <Footer />
    </div>
  );
}

export default Layout;
