// day23_exercise4.jsx

// Exercise 4: Custom Hooks

import { useState, useEffect } from 'react';

// 1. Create custom useCounter hook in React



// 2. Create custom useLocalStorage hook



// 3. Create custom useFetch hook with loading and error states



// 4. Create custom useToggle hook



// Example components using the custom hooks:

// Component using useCounter
function CounterWithCustomHook() {
  const { count, increment, decrement, reset } = useCounter(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

// Component using useLocalStorage
function SettingsWithLocalStorage() {
  const [name, setName] = useLocalStorage('userName', '');
  
  return (
    <div>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <p>Hello, {name}!</p>
    </div>
  );
}

// Component using useFetch
function UserList() {
  const { data: users, loading, error } = useFetch('https://jsonplaceholder.typicode.com/users');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  
  return (
    <ul>
      {users?.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

// Component using useToggle
function ToggleWithCustomHook() {
  const [isVisible, toggleVisible] = useToggle(false);
  
  return (
    <div>
      <button onClick={toggleVisible}>
        {isVisible ? 'Hide' : 'Show'} Content
      </button>
      {isVisible && <p>This content is toggleable!</p>}
    </div>
  );
}

export { 
  useCounter, 
  useLocalStorage, 
  useFetch, 
  useToggle,
  CounterWithCustomHook,
  SettingsWithLocalStorage,
  UserList,
  ToggleWithCustomHook
};

