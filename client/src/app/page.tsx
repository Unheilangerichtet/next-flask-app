// 'use client';

// import { useState } from 'react';

// export default function Home() {
//   const [name, setName] = useState('');
//   const [user, setUser] = useState<{ id: number, name: string } | null>(null);
//   const [error, setError] = useState('');

//   const createUser = async () => {
//     try {
//       const res = await fetch('http://localhost:5000/users', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ name })
//       });

//       if (!res.ok) {
//         throw new Error(`HTTP error ${res.status}`);
//       }

//       const data = await res.json();
//       setUser(data);
//       setError('');
//     } catch (err) {
//       console.error('Failed to create user:', err);
//       setError('Failed to create user');
//     }
//   };

//   return (
//     <div>
//       <h1>Create User</h1>
//       <input value={name} onChange={e => setName(e.target.value)} placeholder="Enter name" />
//       <button onClick={createUser}>Create</button>

//       {user && (
//         <div>
//           <h2>User Created</h2>
//           <p>ID: {user.id}</p>
//           <p>Name: {user.name}</p>
//         </div>
//       )}

//       {error && <p style={{ color: 'red' }}>{error}</p>}
//     </div>
//   );
// }

import React from "react";

const HomePage = () => {
  return <div>page</div>;
};

export default HomePage;
