"use client";

import { useEffect, useState } from "react";
import { useRouter, useParams } from "next/navigation";
import Spreadsheet from "@/components/tables/Spreadsheet";
import { useAuth } from "@/lib/auth/context";

interface Table {
  id: number;
  name: string;
}

export default function TablePage() {
  const params = useParams();
  const id = (params as any).id as string;
  const tableId = Number(id);
  const router = useRouter();
  const { loading: authLoading, isLoggedIn } = useAuth();
  const [table, setTable] = useState<Table | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    if (!isLoggedIn && !authLoading) router.replace("/auth/login");
  }, [isLoggedIn, authLoading]);

  useEffect(() => {
    if (!Number.isFinite(tableId)) return;
    const fetchTable = async () => {
      try {
        const res = await fetch(`/api/tables/${tableId}`, {
          cache: "no-store",
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data?.error || "Failed to load table");
        setTable(data.table);
      } catch (e: any) {
        setError(e?.message || "Failed to load table");
      } finally {
        setLoading(false);
      }
    };
    fetchTable();
  }, [tableId]);

  if (loading || authLoading) {
    return (
      <main className="min-h-screen flex items-center justify-center p-6">
        <p>Loading...</p>
      </main>
    );
  }

  if (error || !table) {
    return (
      <main className="min-h-screen flex items-center justify-center p-6">
        <div className="text-center">
          <p className="text-red-600 mb-3">{error || "Not found"}</p>
          <button
            onClick={() => router.back()}
            className="underline text-blue-600"
          >
            Go back
          </button>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen p-6">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-2xl font-semibold mb-4">{table.name}</h1>
        <Spreadsheet tableId={table.id} />
      </div>
    </main>
  );
}
