import React from "react";
import HeroSection from "../components/HeroSection";
import CustomCard from "../components/Card";
import { Container, Row, Col, Alert } from "react-bootstrap";
import Layout from "../components/Layout"; // Use Layout wrapper

function IndexPage() {
  const workout = true;

  const cards = [
    {
      image: "/images/Single_Workout.png",
      title: "Daily Custom Workout",
      text: "Tailored exercises to fit your daily schedule.",
      link: "/workouts/day/",
      buttonText: "Create Workout",
    },
    {
      image: "/images/Workout_Split_Plan.png",
      title: "Workout Split Plan",
      text: "Get a structured workout plan for your week.",
      link: "/workouts/split/",
      buttonText: "Get Plan",
    },
    {
      image: "/images/LiftBot.png",
      title: "Chat with LiftBot",
      text: "Need advice? Talk to our virtual trainer.",
      link: "/liftbot/",
      buttonText: "Start Chatting",
    },
  ];

  return (
    <Layout>
      <HeroSection
        title="Welcome to Muscle Missions"
        subtitle="Your personal fitness journey starts here"
        buttonText="Start Now"
        link="/workouts/day/"
        image="/images/hero_section.png"
      />

      {workout && (
        <Container className="mt-4">
          <Alert variant="success">Your workout has been saved!</Alert>
        </Container>
      )}

      <Container className="mt-5">
        <h2 className="text-center mb-4" style={{ fontWeight: "700" }}>
          Choose Your Path
        </h2>
        <Row className="g-4">
          {cards.map((card, index) => (
            <Col key={index} md={4}>
              <CustomCard {...card} />
            </Col>
          ))}
        </Row>
      </Container>
    </Layout>
  );
}

export default IndexPage;