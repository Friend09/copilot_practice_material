# Day 24: React API Integration

## Objective

Today you will learn how to integrate your React applications with APIs. You will practice making HTTP requests, handling loading states, managing errors, and displaying data from external sources, with GitHub Copilot assisting in implementing API calls and data management patterns.

## Prerequisites

For these exercises, you may want to install axios for easier HTTP requests:
```bash
npm install axios
```

## Exercises

### Exercise 1: Basic API Calls

Learn to make basic API requests and handle responses.

1.  **Fetch Users**: Create a component that fetches and displays a list of users from JSONPlaceholder API.
    -   *Prompting Hint*: `# React component to fetch and display users from API`
2.  **Fetch with Loading State**: Enhance the users component to show a loading indicator while fetching.
    -   *Prompting Hint*: `# React component with loading state for API calls`
3.  **Error Handling**: Add error handling to display error messages when API calls fail.
    -   *Prompting Hint*: `# React component with error handling for API calls`
4.  **Fetch Single Item**: Create a component that fetches and displays details for a single user by ID.
    -   *Prompting Hint*: `# React component to fetch single user details by ID`
5.  **Conditional Rendering**: Combine loading, error, and success states with conditional rendering.
    -   *Prompting Hint*: `# React component with conditional rendering for API states`

### Exercise 2: CRUD Operations with API

Implement Create, Read, Update, Delete operations with an API.

1.  **Create Post**: Create a form component that sends POST requests to create new posts.
    -   *Prompting Hint*: `# React form component to create posts via API`
2.  **Update Post**: Create a component that allows editing and updating existing posts.
    -   *Prompting Hint*: `# React component to update posts via API`
3.  **Delete Post**: Add delete functionality with confirmation dialog.
    -   *Prompting Hint*: `# React component to delete posts with confirmation`
4.  **Optimistic Updates**: Implement optimistic updates for better user experience.
    -   *Prompting Hint*: `# React component with optimistic updates for API calls`
5.  **Form Validation**: Add client-side validation before making API calls.
    -   *Prompting Hint*: `# React form with validation before API submission`

### Exercise 3: Advanced API Patterns

Explore more advanced patterns for API integration.

1.  **Search with Debouncing**: Create a search component that debounces API calls to avoid excessive requests.
    -   *Prompting Hint*: `# React search component with debounced API calls`
2.  **Pagination**: Implement pagination for large datasets from APIs.
    -   *Prompting Hint*: `# React component with API pagination`
3.  **Infinite Scrolling**: Create an infinite scrolling component that loads more data as the user scrolls.
    -   *Prompting Hint*: `# React infinite scrolling component with API`
4.  **Caching**: Implement basic caching to avoid redundant API calls.
    -   *Prompting Hint*: `# React component with basic API response caching`
5.  **Retry Logic**: Add retry logic for failed API requests.
    -   *Prompting Hint*: `# React component with retry logic for failed API calls`

### Exercise 4: Real-time Data and WebSockets

Explore real-time data updates (conceptual, as WebSocket setup requires backend).

1.  **Polling**: Implement polling to periodically fetch updated data.
    -   *Prompting Hint*: `# React component with polling for real-time updates`
2.  **WebSocket Connection**: Create a conceptual WebSocket component (explain the pattern).
    -   *Prompting Hint*: `# React component pattern for WebSocket connections`
3.  **Real-time Notifications**: Create a notification system that could work with real-time updates.
    -   *Prompting Hint*: `# React notification system for real-time updates`
4.  **Connection Status**: Create a component that monitors and displays connection status.
    -   *Prompting Hint*: `# React component to monitor API connection status`

## Challenge Exercise: Social Media Dashboard

Create a social media dashboard that demonstrates all the concepts learned:
-   Fetch and display posts from multiple users
-   Create new posts with form validation
-   Edit and delete posts with confirmation
-   Search posts with debouncing
-   Pagination or infinite scrolling
-   Real-time updates simulation with polling
-   Error handling and retry logic
-   Loading states and optimistic updates

*Prompting Hint*: `# Create React social media dashboard with full CRUD and advanced API features`

## Reflection

-   How did Copilot help you understand different patterns for API integration in React?
-   Were there any specific patterns Copilot suggested for handling loading states and errors?
-   How effective was Copilot in helping you implement advanced features like debouncing and caching?

