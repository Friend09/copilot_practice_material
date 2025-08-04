# Day 22: React Basics

## Objective

Today marks the beginning of our frontend journey with React. You will learn the fundamental concepts of React, including components, JSX, and rendering. GitHub Copilot will assist you in writing React code, understanding its syntax, and quickly scaffolding components.

## Prerequisites

To set up a React development environment, you can use Create React App or Vite. For simplicity in these exercises, we will focus on the component code itself, assuming a basic React setup. If you want to run these exercises, you can create a new React project:

```bash
npx create-react-app my-react-app
cd my-react-app
npm start
```

Or using Vite (recommended for faster setup):

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

## Exercises

### Exercise 1: Your First React Component

Learn to create and render simple functional components.

1.  **Hello World Component**: Create a functional component named `HelloWorld` that displays "Hello, React!" in an `<h1>` tag.
    -   *Prompting Hint*: `# Create a React functional component named HelloWorld`
2.  **Greeting Component with Prop**: Create a `Greeting` component that accepts a `name` prop and displays "Hello, [name]!".
    -   *Prompting Hint*: `# Create a React component that takes a 'name' prop`
3.  **Basic List Component**: Create a `ItemList` component that takes an array of strings as a prop and renders them as an unordered list (`<ul>`).
    -   *Prompting Hint*: `# Create a React component to display a list of items`
4.  **Conditional Rendering**: Create a `LoginStatus` component that displays "Welcome, User!" if `isLoggedIn` prop is true, and "Please Log In" otherwise.
    -   *Prompting Hint*: `# React component for conditional rendering based on login status`

### Exercise 2: JSX and Component Composition

Practice writing JSX and composing multiple components.

1.  **JSX Expressions**: In a component, use JavaScript expressions within JSX (e.g., display the result of a calculation).
    -   *Prompting Hint*: `# React component demonstrating JSX expressions`
2.  **Component Nesting**: Create a `UserProfile` component that uses `Avatar` and `UserInfo` sub-components.
    -   *Prompting Hint*: `# Create UserProfile component with nested Avatar and UserInfo`
3.  **Props Drilling**: Pass data through multiple levels of components using props.
    -   *Prompting Hint*: `# Demonstrate props drilling in React components`
4.  **Event Handling**: Create a `Button` component that logs a message to the console when clicked.
    -   *Prompting Hint*: `# React button component with onClick event handler`

### Exercise 3: Styling React Components

Explore basic ways to style your React components.

1.  **Inline Styles**: Apply inline styles to a component.
    -   *Prompting Hint*: `# Apply inline styles to a React component`
2.  **CSS Classes**: Apply CSS classes to a component using a separate CSS file.
    -   *Prompting Hint*: `# Apply CSS classes to React component`
3.  **Conditional Styling**: Apply different styles based on a component's state or props.
    -   *Prompting Hint*: `# Conditional styling in React based on prop`
4.  **Styled Components (Conceptual)**: Discuss or conceptually outline how you would use a library like Styled Components for styling.
    -   *Prompting Hint*: `# Explain how to use styled-components in React`

## Challenge Exercise: Simple Product Card

Create a `ProductCard` component that displays:
-   Product image
-   Product name
-   Product price
-   A button to "Add to Cart"

This component should take `product` (an object with `name`, `price`, `imageUrl`) as a prop. Use basic styling.

*Prompting Hint*: `# Create a React ProductCard component with image, name, price, and add to cart button`

## Reflection

-   How did Copilot assist you in understanding JSX syntax and component structure?
-   Were there any specific patterns Copilot suggested for creating functional components or handling props?
-   How effective was Copilot in helping you with basic styling and event handling in React?

