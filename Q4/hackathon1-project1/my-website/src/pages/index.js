import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HeroSlider from '@site/src/components/HeroSlider';

import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className="text--center">
          <div className={styles.logoContainer}>
            <img
              src={siteConfig.themeConfig.navbar.logo.src}
              alt="Robotics Logo"
              className={clsx(styles.mainLogo, styles.animateLogo)}
            />
          </div>
        </div>
        <Heading as="h1" className={clsx("hero__title text--center", styles.fadeIn)}>
          {siteConfig.title}
        </Heading>
        <p className={clsx("hero__subtitle text--center", styles.fadeIn, styles.delay1)}>
          {siteConfig.tagline}
        </p>
        <div className={clsx(styles.buttons, styles.fadeIn, styles.delay2)}>
          <Link
            className="button button--secondary button--lg"
            to="/book">
            Start Reading - Robotics Guide
          </Link>
          <Link
            className="button button--primary button--lg margin-left--md"
            to="/docs/module1-ros2">
            Begin with Module 1
          </Link>
        </div>
      </div>
    </header>
  );
}

function BookOverview() {
  return (
    <section className={clsx(styles.section, styles.bookOverview)}>
      <div className="container">
        <div className="row">
          <div className="col col--12 text--center">
            <Heading as="h2">Complete Guide to Modern Robotics</Heading>
            <p className="padding-horiz--md">
              This comprehensive guide takes you through the cutting-edge technologies
              that power modern robots, from foundational middleware to AI integration.
            </p>
          </div>
        </div>

        <div className="row padding-vert--lg">
          <div className="col col--4">
            <div className={styles.featureCard}>
              <h3>Module 1: ROS 2 - The Robotic Nervous System</h3>
              <p>Master the Robot Operating System 2, the middleware that connects all robot components.
                 Learn about nodes, topics, services, and how to bridge Python agents to ROS controllers.</p>
            </div>
          </div>
          <div className="col col--4">
            <div className={styles.featureCard}>
              <h3>Module 2: Digital Twins - Gazebo & Unity</h3>
              <p>Explore simulation technologies that create virtual replicas of physical robots.
                 Learn physics simulation, sensor modeling, and high-fidelity rendering.</p>
            </div>
          </div>
          <div className="col col--4">
            <div className={styles.featureCard}>
              <h3>Module 3: AI-Robot Brain - NVIDIA Isaac™</h3>
              <p>Discover NVIDIA's robotics platform with photorealistic simulation,
                 hardware-accelerated perception, and advanced navigation for humanoid robots.</p>
            </div>
          </div>
        </div>

        <div className="row padding-vert--lg">
          <div className="col col--12">
            <div className={styles.featureCard}>
              <h3>Module 4: Vision-Language-Action (VLA) - The Cognitive Interface</h3>
              <p>Experience the convergence of LLMs and robotics. Learn how robots understand voice commands,
                 plan actions using cognitive AI, and execute complex tasks autonomously.</p>
            </div>
          </div>
        </div>

        <div className="row padding-vert--lg">
          <div className="col col--12 text--center">
            <Link
              className="button button--primary button--lg"
              to="/book">
              Read the Complete Book
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

function LearningPath() {
  return (
    <section className={clsx(styles.section, styles.learningPath)}>
      <div className="container">
        <div className="row">
          <div className="col col--12 text--center">
            <Heading as="h2">Your Learning Journey</Heading>
            <p className="padding-horiz--md">
              Follow this structured path to master robotics from fundamentals to advanced AI integration.
            </p>
          </div>
        </div>

        <div className="row padding-vert--lg">
          <div className="col col--3 text--center">
            <div className={styles.stepCircle}>1</div>
            <h3>Foundation</h3>
            <p>ROS 2 concepts, nodes, topics, and services</p>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.stepCircle}>2</div>
            <h3>Simulation</h3>
            <p>Gazebo physics, Unity rendering & sensor modeling</p>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.stepCircle}>3</div>
            <h3>Perception & Navigation</h3>
            <p>NVIDIA Isaac, perception, and navigation</p>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.stepCircle}>4</div>
            <h3>AI Integration</h3>
            <p>Vision-Language-Action systems</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Home - ${siteConfig.title}`}
      description="Complete Guide to Modern Robotics: ROS 2, Digital Twins, NVIDIA Isaac, and Vision-Language-Action Systems">
      <HomepageHeader />
      <HeroSlider />
      <main>
        <BookOverview />
        <LearningPath />
      </main>
    </Layout>
  );
}
