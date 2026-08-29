import { useEffect, useState } from 'react';

export default function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Exact URL: apne username aur repo name se REPLACE karein
    fetch('https://raw.githubusercontent.com/dakshanil01-stack/NeonXPlay/main/data.json')
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-6 bg-slate-900 min-h-screen text-white">
      <h1 className="text-2xl font-bold mb-4 text-cyan-400">Live Trending Topics</h1>
      <div className="grid gap-4">
        {items.map(item => (
          <a key={item.id} href={item.url} target="_blank" rel="noreferrer" className="p-4 bg-slate-800 rounded-lg hover:bg-slate-700 transition block">
            <p className="font-semibold">{item.id}. {item.title}</p>
          </a>
        ))}
      </div>
    </div>
  );
}
