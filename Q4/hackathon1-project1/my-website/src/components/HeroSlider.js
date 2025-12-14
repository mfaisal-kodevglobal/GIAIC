import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from '../pages/index.module.css';

const slides = [
  {
    title: "ROS 2 - The Robotic Nervous System",
    subtitle: "Master the middleware connecting all robot components",
    description: "Learn about nodes, topics, services, and how to bridge Python agents to ROS controllers.",
  },
  {
    title: "Digital Twins - Gazebo & Unity",
    subtitle: "Simulation technologies for virtual robot replicas",
    description: "Explore physics simulation, sensor modeling, and high-fidelity rendering for safer development.",
  },
  {
    title: "NVIDIA Isaac™ - AI-Robot Brain",
    subtitle: "Hardware-accelerated perception and navigation",
    description: "Discover NVIDIA's platform with photorealistic simulation and advanced navigation for humanoid robots.",
  },
  {
    title: "Vision-Language-Action Systems",
    subtitle: "The cognitive interface for robots",
    description: "Experience the convergence of LLMs and robotics. Control robots with natural language.",
  }
];

export default function HeroSlider() {
  const [currentSlide, setCurrentSlide] = useState(0);

  // Auto-rotate slides
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const goToSlide = (index) => {
    setCurrentSlide(index);
  };

  return (
    <section className={styles.heroSlider}>
      <div className={styles.sliderContainer}>
        {slides.map((slide, index) => (
          <div 
            key={index} 
            className={clsx(
              styles.slide, 
              index === currentSlide ? styles.active : ''
            )}
          >
            <div className={styles.slideContent}>
              <div className={styles.slideText}>
                <h2 className={styles.slideTitle}>{slide.title}</h2>
                <h3 className={styles.slideSubtitle}>{slide.subtitle}</h3>
                <p className={styles.slideDescription}>{slide.description}</p>
                <div className={styles.slideButtons}>
                  <Link className="button button--primary" to="/book">
                    Explore This Module
                  </Link>
                </div>
              </div>
              <div className={styles.slideImage}>
                <div className={styles.robotImagePlaceholder}>
                  <div className={styles.robotIcon}>🤖</div>
                </div>
              </div>
            </div>
          </div>
        ))}
        <div className={styles.sliderNavigation}>
          {slides.map((_, index) => (
            <button 
              key={index} 
              className={clsx(
                styles.navDot, 
                index === currentSlide ? styles.active : ''
              )}
              onClick={() => goToSlide(index)}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </div>
    </section>
  );
}