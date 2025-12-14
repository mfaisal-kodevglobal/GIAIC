<!--
Sync Impact Report:
Version change: 0.0.0 -> 1.0.0 (MAJOR: Initial creation/significant update)
List of modified principles: All principles updated/added based on user input.
Added sections: "Key Standards and Requirements", "Book and Chatbot Specifics"
Removed sections: None (placeholders were filled or removed as per template rules)
Templates requiring updates:
- .specify/templates/plan-template.md: ✅ updated
- .specify/templates/spec-template.md: ✅ updated
- .specify/templates/tasks-template.md: ✅ updated
- .specify/templates/commands/*.md: ⚠ pending (no command templates found)
Follow-up TODOs: None
-->
# Unified Book + RAG Chatbot on Physical AI & Humanoid Robotics Constitution

## Core Principles

### I. Technical Accuracy
All technical content, definitions, claims, and steps MUST be verified against official primary documentation (ROS 2, Gazebo, Unity, NVIDIA Isaac).

### II. Clarity for AI/Robotics Students
Content MUST be clear, concise, instructional, and engineering-focused, specifically tailored for students in AI and Robotics.

### III. Modularity and Maintainability
The project structure, especially for the Docusaurus book, MUST be modular and maintainable.

### IV. Code Correctness and Testability
All code examples (Python, ROS 2, FastAPI) MUST be fully validated for correctness and written with testability in mind.

### V. RAG-Grounded Responses
The RAG chatbot MUST provide responses grounded ONLY in the book content or user-selected text, preventing hallucinations.

## Key Standards and Requirements

*   All definitions, claims, and technical steps MUST be sourced from primary documentation.
*   Style: concise, instructional, engineering-focused.
*   Include code examples (Python, ROS 2, FastAPI) fully validated.
*   RAG chatbot MUST answer only from book content or user-selected text.
*   Include diagrams, architecture flows, and deployment steps.

## Book and Chatbot Specifics

**Book Requirements:**
*   Built with Spec-Kit Plus + Claude Code.
*   Deployed via GitHub Pages.
*   Content covers:
    *   ROS 2 nodes, topics, services, URDF.
    *   Gazebo & Unity simulation.
    *   NVIDIA Isaac Sim, VSLAM, Nav2.
    *   Vision-Language-Action robotics.
    *   Full humanoid robotics capstone.

**Chatbot Requirements:**
*   Powered by OpenAI Agents / ChatKit SDK.

## Governance

All definitions, claims, and technical steps MUST be sourced from primary documentation. All PRs/reviews must verify compliance.

**Version**: 1.0.0 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-09
