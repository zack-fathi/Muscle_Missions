import React from "react";
import HeroSection from "../components/HeroSection";

function HomePage() {
  return (
    <div>
      <HeroSection
        title="Welcome to Muscle Missions"
        subtitle="Your personal fitness journey starts here"
        buttonText="Start Now"
        link="/workouts/day/"
        image="/images/hero_section.png"
      />
    </div>
  );
}

export default HomePage;