import React from "react";
import CustomNavbar from "./Navbar"; // Assuming you have a Navbar component
import { Container } from "react-bootstrap";

function Layout({ children }) {
  return (
    <div className="d-flex flex-column min-vh-100">
      {/* Navbar */}
      <CustomNavbar />

      {/* Main Content */}
      <Container className="flex-grow-1 mt-3">{children}</Container>

      {/* Footer */}
      <footer className="bg-dark text-white text-center py-3 mt-4">
        <p className="mb-0">
          © {new Date().getFullYear()} Muscle Missions. All rights reserved.
        </p>
      </footer>
    </div>
  );
}

export default Layout;
