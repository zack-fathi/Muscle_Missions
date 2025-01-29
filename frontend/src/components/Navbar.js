import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';

function CustomNavbar() {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">Muscle Missions</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarNav" />
        <Navbar.Collapse id="navbarNav">
          <Nav className="me-auto">
            <Nav.Link href="/saved_workouts/">Your Workout</Nav.Link>
            <Nav.Link href="/liftbot/">LiftBot</Nav.Link>
            <Nav.Link href="/accounts/edit/">Edit Account</Nav.Link>
          </Nav>
          <Nav className="ms-auto">
            <Nav.Link href="/accounts/logout/">Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default CustomNavbar;