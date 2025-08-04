# Day 23: React State and Hooks

## Objective

Today you will learn about React state management using hooks, particularly `useState` and `useEffect`. You will understand how to make your components interactive and responsive to user actions, with GitHub Copilot assisting in implementing state logic and side effects.

## Exercises

### Exercise 1: useState Hook

Learn to manage component state using the `useState` hook.

1.  **Counter Component**: Create a counter component with increment and decrement buttons.
    -   *Prompting Hint*: `# Create React counter component with useState`
2.  **Input State**: Create a component with an input field that displays the current input value in real-time.
    -   *Prompting Hint*: `# React component with input field using useState`
3.  **Toggle Component**: Create a component that toggles between "ON" and "OFF" states when clicked.
    -   *Prompting Hint*: `# React toggle component using useState`
4.  **Array State**: Create a component that manages a list of items (add/remove functionality).
    -   *Prompting Hint*: `# React component managing array state with add/remove`
5.  **Object State**: Create a form component that manages an object state (e.g., user profile with name, email, age).
    -   *Prompting Hint*: `# React form component managing object state`

### Exercise 2: useEffect Hook

Learn to handle side effects using the `useEffect` hook.

1.  **Component Mount Effect**: Create a component that logs a message when it mounts and unmounts.
    -   *Prompting Hint*: `# React component with useEffect for mount/unmount`
2.  **State-Dependent Effect**: Create a component where `useEffect` runs when a specific state variable changes.
    -   *Prompting Hint*: `# React useEffect that depends on state variable`
3.  **Timer Component**: Create a component with a timer that updates every second using `useEffect`.
    -   *Prompting Hint*: `# React timer component using useEffect and setInterval`
4.  **Data Fetching**: Create a component that fetches data from an API when it mounts.
    -   *Prompting Hint*: `# React component fetching data with useEffect`
5.  **Cleanup Function**: Create a component that sets up an event listener and cleans it up properly.
    -   *Prompting Hint*: `# React useEffect with cleanup function`

### Exercise 3: Combining useState and useEffect

Practice using both hooks together for more complex interactions.

1.  **Search Component**: Create a search component that filters a list of items based on user input.
    -   *Prompting Hint*: `# React search component with useState and useEffect`
2.  **Auto-Save Form**: Create a form that automatically saves data to localStorage when the user types.
    -   *Prompting Hint*: `# React auto-save form using useState and useEffect`
3.  **Dynamic Theme**: Create a component that changes theme (light/dark) and persists the preference.
    -   *Prompting Hint*: `# React theme switcher with localStorage persistence`
4.  **Real-time Validation**: Create a form with real-time validation that shows error messages.
    -   *Prompting Hint*: `# React form with real-time validation using hooks`

### Exercise 4: Custom Hooks

Learn to create reusable logic with custom hooks.

1.  **useCounter Hook**: Create a custom hook that encapsulates counter logic (increment, decrement, reset).
    -   *Prompting Hint*: `# Create custom useCounter hook in React`
2.  **useLocalStorage Hook**: Create a custom hook that syncs state with localStorage.
    -   *Prompting Hint*: `# Create custom useLocalStorage hook`
3.  **useFetch Hook**: Create a custom hook for data fetching with loading and error states.
    -   *Prompting Hint*: `# Create custom useFetch hook with loading and error states`
4.  **useToggle Hook**: Create a custom hook for toggle functionality.
    -   *Prompting Hint*: `# Create custom useToggle hook`

## Challenge Exercise: Todo List Application

Create a complete todo list application that demonstrates all the concepts learned:
-   Add new todos
-   Mark todos as complete/incomplete
-   Delete todos
-   Filter todos (all, active, completed)
-   Persist todos in localStorage
-   Show todo count

Use multiple hooks and consider creating custom hooks for reusable logic.

*Prompting Hint*: `# Create complete React todo list app with hooks and localStorage`

## Reflection

-   How did Copilot help you understand the useState and useEffect hooks?
-   Were there any specific patterns Copilot suggested for managing complex state or side effects?
-   How effective was Copilot in helping you create custom hooks and reusable logic?

