"use client";

import { useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";

type TableRow = {
  id: number;
  name: string;
  user_id: number;
  created_at: string;
};

export default function TableManager() {
  const [tables, setTables] = useState<TableRow[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const router = useRouter();
  const [error, setError] = useState<string>("");
  const [name, setName] = useState<string>("");
  const [selectedId, setSelectedId] = useState<number | null>(null);
  const selected = useMemo(
    () => tables.find((t) => t.id === selectedId) || null,
    [tables, selectedId]
  );

  const loadTables = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/tables", {
        method: "GET",
        cache: "no-store",
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data?.error || "Failed to load tables");
      setTables(data.tables || []);
    } catch (e: any) {
      setError(e?.message || "Failed to load tables");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTables();
  }, []);

  const createTable = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/tables", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name.trim() }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data?.error || "Failed to create table");
      setName("");
      setTables((prev) => [data.table, ...prev]);
      // Redirect to newly created table page
      router.push(`/table/${data.table.id}`);
    } catch (e: any) {
      setError(e?.message || "Failed to create table");
    } finally {
      setLoading(false);
    }
  };

  const deleteTable = async (id: number) => {
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`/api/tables/${id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) throw new Error(data?.error || "Failed to delete table");
      setTables((prev) => prev.filter((t) => t.id !== id));
      if (selectedId === id) setSelectedId(null);
    } catch (e: any) {
      setError(e?.message || "Failed to delete table");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto">
      <h2 className="text-xl font-semibold mb-3">Your Tables</h2>
      <form onSubmit={createTable} className="flex gap-2 mb-4">
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="New table name"
          className="border rounded px-3 py-2 flex-1"
        />
        <button
          type="submit"
          disabled={loading || !name.trim()}
          className="bg-black text-white rounded px-4 py-2 disabled:opacity-50"
        >
          Create
        </button>
      </form>
      {error && (
        <div className="mb-3 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
          {error}
        </div>
      )}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="border rounded p-3">
          {loading ? (
            <p>Loading...</p>
          ) : tables.length === 0 ? (
            <p className="text-gray-600">
              No tables yet. Create your first one.
            </p>
          ) : (
            <ul className="space-y-2">
              {tables.map((t) => (
                <li
                  key={t.id}
                  className={`flex items-center justify-between border rounded px-3 py-2 ${
                    selectedId === t.id ? "bg-gray-50" : ""
                  }`}
                >
                  <button
                    onClick={() => router.push(`/table/${t.id}`)}
                    className="text-left flex-1 hover:underline"
                  >
                    {t.name}
                  </button>
                  <button
                    onClick={() => deleteTable(t.id)}
                    className="ml-3 text-sm text-red-600 hover:underline"
                  >
                    Delete
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
        <div className="border rounded p-3 min-h-[240px]">
          {!selected ? (
            <p className="text-gray-600">Select a table to start working.</p>
          ) : (
            <div>
              <h3 className="font-medium mb-2">{selected.name}</h3>
              <div className="text-gray-600 text-sm">
                Work area placeholder. We will render cells grid and editing
                tools here.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
